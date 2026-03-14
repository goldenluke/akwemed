import InterpretationCard from "./InterpretationCard"
import ProtocolCard from "./ProtocolCard"

export default function ClinicalPanel({analysis}){

    if(!analysis){

        return(

            <div className="p-10 text-slate-400">

            Aguardando consulta clínica...

            </div>

        )

    }

    return(

        <div className="p-8 space-y-6">

        <InterpretationCard data={analysis}/>

        <ProtocolCard data={analysis}/>

        </div>

    )

}
