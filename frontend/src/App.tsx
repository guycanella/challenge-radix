import { createContext, useMemo } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import Home from './components/Home'
import Menu from './components/Menu'
import NotFound from './components/NotFound'

const HOURS = [
  {
      id: 'T-all',
      label: 'Todos os dados',
      value: 0
  },
  {
      id: 'T-24',
      label: 'últimas 24 horas',
      value: 24
  },
  {
      id: 'T-48',
      label: '48 horas',
      value: 48
  },
  {
      id: 'T-168',
      label: '1 semana',
      value: 168
  },
  {
      id: 'T-720',
      label: '1 mês',
      value: 720
  }
]

type HoursType = typeof HOURS[0]

type ContextData = {
  hours: HoursType[]
}

export const Context = createContext({} as ContextData)

function App() {
  const value = useMemo(() => {
    return { hours: HOURS }
  }, [])

  return (
    <main className='xs:w-[90%] md:w-[80%] mx-auto min-h-screen py-4'>
      <h1
        className='xs:text-2xl sm:text-3xl font-bold py-8 px-2 bg-gradient-to-r from-[#2A1844] to-[#532F88] text-white'
      >
        Dados dos sensores
      </h1>

      <Context.Provider value={value}>
        <Menu />

        <Router>
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='*' element={<NotFound />} />
          </Routes>
        </Router>
      </Context.Provider>
    </main>
  )
}

export default App
