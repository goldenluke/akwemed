import { useState } from "react"
import ChatInput from "./ChatInput"
import UserMessage from "./UserMessage"
import AiMessage from "./AiMessage"
import api from "../services/api"

export default function ChatContainer() {

    const [messages, setMessages] = useState([])

    const sendMessage = async (text) => {

        const userMsg = { type: "user", text }

        setMessages(prev => [...prev, userMsg])

        try {

            const response = await api.post("/consult/", { text })

            const aiMsg = {
                type: "ai",
                data: response.data
            }

            setMessages(prev => [...prev, aiMsg])

        } catch (err) {

            console.error(err)

        }

    }

    return (

        <div className="flex flex-col h-screen bg-gray-950 text-white">

        <div className="flex-1 overflow-y-auto p-6 space-y-4">

        {messages.map((m, i) =>

            m.type === "user"
            ? <UserMessage key={i} text={m.text}/>
            : <AiMessage key={i} data={m.data}/>

        )}

        </div>

        <ChatInput onSend={sendMessage}/>

        </div>

    )

}
