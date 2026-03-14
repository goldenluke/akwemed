import {useState} from "react"
import {FiSend} from "react-icons/fi"

export default function InputBar({onSend}){

    const [text,setText] = useState("")

    const submit=()=>{

        if(!text)return

            onSend(text)
            setText("")
    }

    return(

        <div className="p-4 border-t border-slate-700 flex gap-3">

        <input
        className="flex-1 p-3 rounded bg-slate-800"
        placeholder="Relato em Xerente..."
        value={text}
        onChange={(e)=>setText(e.target.value)}
        />

        <button
        onClick={submit}
        className="bg-blue-600 p-3 rounded"
        >

        <FiSend/>

        </button>

        </div>

    )

}
