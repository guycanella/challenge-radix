
import { useContext } from "react"
import { Context } from "../App"

const Menu = () => {
  const { hours } = useContext(Context)

  const returnLink = (val: number) => {
    if (val === 0) return '/'

    return `/?period=${val}`
  }

  return (
    <div className="px-2 py-4 mb-8 bg-gradient-to-r from-[#2A1844] to-[#532F88]">
        <ul className="flex gap-8 flex-wrap">
            {hours.map((option) => (
                <li key={option.id} className="w-max">
                    <a
                        href={returnLink(option.value)}
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