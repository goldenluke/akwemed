import { useState } from "react"

export default function ChatInput({ onSend }) {

    const [text, setText] = useState("")

    const handleSend = () => {

        if (!text) return

            onSend(text)

            setText("")

    }

    return (

        <div className="flex p-4 border-t border-gray-700">

        <input
        className="flex-1 bg-gray-800 rounded-lg px-4 py-2"
        placeholder="Digite o sintoma..."
        value={text}
        onChange={e => setText(e.target.value)}
        />

        <button
        onClick={handleSend}
        className="ml-3 px-4 py-2 bg-blue-600 rounded-lg"
        >
        Enviar
        </button>

        </div>

    )

}
