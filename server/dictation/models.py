from django.db import models
from pydub import AudioSegment
from pydub.silence import split_on_silence
from io import BytesIO
from django.core.files.base import ContentFile

class Topic(models.Model):
    LEVEL = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard')
    ]

    name = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=LEVEL)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    full_audio = models.FileField(upload_to='audio/lesson/')
    full_transcript = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.full_audio:
            audio = AudioSegment.from_file(self.full_audio.path)

            chunks = split_on_silence(audio, min_silence_len=400, silence_thresh=-40)
            self.dictations.all().delete()
            list_transcript = self.full_transcript.split('\n')
            # Tạo các Dictation mới từ các đoạn cắt
            for i, chunk in enumerate(chunks):
                if i == 0:
                    continue
                
                # Lưu đoạn audio nhỏ thành file MP3
                buffer = BytesIO()
                chunk.export(buffer, format="mp3")
                audio_file = ContentFile(buffer.getvalue(), name=f'dictation_{self.id}_{i+1}.mp3')

                # Tạo bản ghi Dictation
                transcript = list_transcript[i-1] if i - 1 < len(list_transcript) else 'transcript'
                Dictation.objects.create(
                    lesson=self,
                    audio_file=audio_file,
                    transcript=f"{transcript}"  # Placeholder cho transcript
                )

class Dictation(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='dictations', on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio/diction/')
    transcript = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.transcript