export default function AiMessage({data}){

    return(

        <div className="flex justify-start">

        <div className="bg-white shadow p-4 rounded-xl max-w-lg space-y-2">

        <div className="text-blue-600 font-semibold">
        Interpretação
        </div>

        <div>
        {data.interpreted}
        </div>

        <div className="text-red-600 font-semibold">
        Protocolo Clínico
        </div>

        <div>
        {data.protocol}
        </div>

        <div className="text-gray-600">
        {data.recommendation}
        </div>

        </div>

        </div>

    )

}
