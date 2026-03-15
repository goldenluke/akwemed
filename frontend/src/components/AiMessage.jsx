import InterpretationCard from "./InterpretationCard"
import ProtocolCard from "./ProtocolCard"
import DynamicsCard from "./DynamicsCard"

export default function AiMessage({ data }) {

    return (

        <div className="flex justify-start">

        <div className="bg-gray-800 p-4 rounded-xl max-w-xl space-y-3">

        <InterpretationCard data={data}/>

        <ProtocolCard data={data}/>

        <DynamicsCard data={data}/>

        </div>

        </div>

    )

}
