import UserMessage from "./UserMessage"
import AiMessage from "./AiMessage"

export default function ChatContainer({messages}){

    return(

        <div className="flex-1 overflow-y-auto p-6 space-y-4">

        {messages.map((m,i)=>{

            if(m.role==="user"){
                return <UserMessage key={i} text={m.text}/>
            }

            return <AiMessage key={i} data={m.data}/>

        })}

        </div>

    )

}
