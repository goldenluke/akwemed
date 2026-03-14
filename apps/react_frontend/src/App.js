import { useState } from "react"
import axios from "axios"

export default function App(){

    const [text,setText] = useState("")
    const [result,setResult] = useState(null)

    const analyze = async ()=>{

        const res = await axios.post(
            "http://localhost:8000/api/consult/",
            { text }
        )

        setResult(res.data)
    }

    return(

        <div className="min-h-screen bg-slate-900 text-white p-10">

        <h1 className="text-4xl font-bold mb-8">
        AKWEMED
        </h1>

        <h2 className="text-xl mb-4">
        Assistente Clínico Intercultural
        </h2>

        <div className="flex gap-4 mb-10">

        <input
        className="p-3 text-black w-96 rounded"
        placeholder="Relato do paciente em Xerente"
        value={text}
        onChange={(e)=>setText(e.target.value)}
        />

        <button
        className="bg-blue-600 px-6 py-3 rounded"
        onClick={analyze}
        >
        Analisar
        </button>

        </div>

        {result && (

            <div className="grid grid-cols-2 gap-6">

            <div className="bg-slate-800 p-6 rounded">

            <h3 className="text-lg mb-3">
            Interpretação Linguística
            </h3>

            <p>{result.interpreted}</p>

            </div>

            <div className="bg-slate-800 p-6 rounded">

            <h3 className="text-lg mb-3">
            Análise Clínica
            </h3>

            <p>{result.analysis}</p>

            </div>

            <div className="bg-slate-800 p-6 rounded col-span-2">

            <h3 className="text-lg mb-3">
            Protocolo Clínico
            </h3>

            <p>{result.protocol}</p>

            </div>

            </div>

        )}

        </div>

    )
}
