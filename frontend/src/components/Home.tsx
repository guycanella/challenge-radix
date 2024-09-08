import { memo } from 'react'
import { useSearchParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'

import { getSensorData } from '../api/fetch'
import { SensorDataResponse } from '../api/api'

const Home = () => {
  const [searchParams] = useSearchParams()
  const period = searchParams.get('period')

  const { data } = useQuery<SensorDataResponse>({ queryKey: ['queryGetSensorData'], queryFn: () => getSensorData(period) })

  console.log(data)

  if (!data) return null

  return (
      <>
        {JSON.stringify(data)}
      </>
  )
}

export default memo(Home)