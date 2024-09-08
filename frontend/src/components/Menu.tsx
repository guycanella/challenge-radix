const HOURS = [
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

const Menu = () => {
  return (
    <div className="px-2 py-4 mb-4 bg-gradient-to-r from-[#2A1844] to-[#532F88]">
        <ul className="flex gap-8">
            <li className="w-max">
                <a
                    href="/"
                    className="p-3 bg-[#bada55] rounded-md hover:bg-[#fa960d] hover:text-white transition-all duration-500"
                >
                    Todos dados
                </a>
            </li>
            {HOURS.map((option) => (
                <li key={option.id} className="w-max">
                    <a
                        href={`/?period=${option.value}`}
                        className="p-3 bg-[#bada55] rounded-md hover:bg-[#fa960d] hover:text-white transition-all duration-500"
                    >
                        {option.label}
                    </a>
                </li>
            ))}
        </ul>
    </div>
  )
}

export default Menu