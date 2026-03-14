export default function UserMessage({text}){

    return(

        <div className="flex justify-end">

        <div className="bg-medical text-white p-3 rounded-xl max-w-md">
        {text}
        </div>

        </div>

    )

}
