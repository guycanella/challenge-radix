import { memo } from 'react'
import { useSearchParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'

import { getSensorData } from '../api/fetch'
import { SensorDataResponse } from '../api/api'
import Graph from './Graph'
import Loading from './Loading'

const Home = () => {
  const [searchParams] = useSearchParams()
  const period = searchParams.get('period')

  const { data, error, isLoading } =
    useQuery<SensorDataResponse>({
      queryKey: ['queryGetSensorData', period],
      queryFn: () => getSensorData(period)
    })

  if (!data && isLoading) {
    return (
        <Loading />
    )
  }

  if (!data && !isLoading && error) {
    console.log({ error })

    return (
        <h1 className='text-3xl font-bold'>
            Desculpe, mas algum erro ocorreu.
        </h1>
    )
  }

  return (
    <div className="information-section">
        <Graph data={data} />
    </div>
  )
}

export default memo(Home)