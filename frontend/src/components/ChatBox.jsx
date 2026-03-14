import {useState} from "react"
import {consult} from "../services/api"
import Message from "./Message"
import InputBar from "./InputBar"

export default function ChatBox(){

    const [messages,setMessages] = useState([])
    const [analysis,setAnalysis] = useState(null)

    const send = async(text)=>{

        const res = await consult(text)

        setMessages([
            ...messages,
            {role:"user",text:text},
            {role:"ai",text:res.analysis}
        ])

        setAnalysis(res)

    }

    return(

        <div className="flex flex-col h-full">

        <div className="flex-1 overflow-y-auto p-6 space-y-4">

        {messages.map((m,i)=>(
            <Message key={i} {...m}/>
        ))}

        </div>

        <InputBar onSend={send}/>

        </div>

    )

}
