export const getSensorData = async (period: string | null) => {
    const optionalParameter = period ? `?period=${period}` : ''
    const response = await fetch(`http://127.0.0.1:8000/data-sensor${optionalParameter}`)

    return response.json()
}