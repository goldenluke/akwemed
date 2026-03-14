import {useState} from "react"

export default function ChatInput({onSend}){

    const [text,setText] = useState("")

    const send = ()=>{

        if(!text) return

            onSend(text)

            setText("")
    }

    return(

        <div className="p-4 bg-white border-t flex gap-2">

        <input
        className="flex-1 border rounded-lg p-2"
        placeholder="Digite o sintoma em Xerente..."
        value={text}
        onChange={e=>setText(e.target.value)}
        />

        <button
        onClick={send}
        className="bg-medical text-white px-4 rounded-lg"
        >
        Enviar
        </button>

        </div>

    )

}
