import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [lessons, setLessons] = useState([])

  useEffect(() => {
    fetch('http://localhost:8000/lesson/')
      .then(res => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then(data => setLessons(data))
      .catch(err => console.log(err))
  }, [])

  return (
    <>
      {lessons.map(lesson => (
        <h1>{lesson.name}</h1>
      ))}
    </>
  )
}

export default App
