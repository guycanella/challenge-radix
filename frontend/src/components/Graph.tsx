import { useContext } from 'react'
import { useSearchParams } from 'react-router-dom'
import {
    CartesianGrid,
    Legend,
    Line,
    LineChart,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from 'recharts'

import type { SensorDataResponse } from '../api/api'
import { Context } from '../App'

type GraphProps = {
    data: SensorDataResponse | undefined
}

const Graph = ({ data }: GraphProps) => {
  const { hours } = useContext(Context)
  const [searchParams] = useSearchParams()
  const period = searchParams.get('period')

  const onTitle = (period: string | null) => {
    if (!period) {
        const title = hours.find((hour) => hour.id === 'T-all')

        return title?.label
    }

    const title = hours.find((hour) => hour.value === Number(period))

    return title?.label
  }

  return (
    <>
        <h2 className='flex justify-center text-xl font-bold'>{onTitle(period)}</h2>

        <div className='xs:w-[90%] pt-8 md:w-[70%] h-[400px] mx-auto'>
            <ResponsiveContainer>
                <LineChart data={data?.data}>
                    <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
                    <XAxis dataKey="equipmentId" />
                    <YAxis
                        label={{
                            value: "Valor médio por sensor",
                            angle: -90,
                            position: 'outsideLeft',
                            dx: -20
                        }}
                        className='px-6'
                    />
                    <Tooltip animationDuration={500} />
                    <Legend />
                    <Line
                        type="monotone"
                        dataKey="value"
                        stroke="#532F88"
                        activeDot={{
                            stroke: "#bada55",
                            fill: "#bada55"
                        }}
                    />
                </LineChart>
            </ResponsiveContainer>
        </div>
    </>
  )
}

export default Graph