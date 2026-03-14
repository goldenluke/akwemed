export default function Message({role,text}){

    return(

        <div className={`max-w-md p-4 rounded-lg ${
            role==="user"
            ? "bg-blue-600 ml-auto"
            : "bg-slate-700"
        }`}>

        {text}

        </div>

    )

}
