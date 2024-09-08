import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './components/Home'
import Menu from './components/Menu'

function App() {
  return (
    <main className='w-[80%] mx-auto min-h-screen py-4'>
      <h1
        className='text-3xl font-bold py-8 px-2 bg-gradient-to-r from-[#2A1844] to-[#532F88] text-white'
      >
        Dados dos sensores
      </h1>

      <Menu />

      <Router>
        <Routes>
          <Route path='/' element={<Home />} />
        </Routes>
      </Router>
    </main>
  )
}

export default App
