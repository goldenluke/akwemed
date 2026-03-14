import {useState} from "react"
import ChatContainer from "../components/ChatContainer"
import ChatInput from "../components/ChatInput"
import {consult} from "../services/api"

export default function Dashboard(){

    const [messages,setMessages] = useState([])

    const handleSend = async(text)=>{

        const userMessage = {
            role:"user",
            text
        }

        setMessages(m=>[...m,userMessage])

        const res = await consult(text)

        const aiMessage = {
            role:"ai",
            data:res
        }

        setMessages(m=>[...m,aiMessage])
    }

    return(

        <div className="h-screen flex flex-col bg-gray-100">

        <div className="bg-medical text-white p-4 font-bold text-xl shadow">
        AKWEMED • Assistente Clínico Akwẽ
        </div>

        <ChatContainer messages={messages}/>

        <ChatInput onSend={handleSend}/>

        </div>

    )

}
