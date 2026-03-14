export default function ProtocolCard({data}){

    return(

        <div className="bg-slate-800 p-6 rounded-xl">

        <h2 className="text-xl mb-4">

        Protocolo Clínico

        </h2>

        <p>{data.protocol}</p>

        </div>

    )

}
