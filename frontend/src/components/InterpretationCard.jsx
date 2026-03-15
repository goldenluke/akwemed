export default function InterpretationCard({ data }) {

    return (

        <div className="bg-gray-900 p-3 rounded-lg">

        <h3 className="text-blue-400 text-sm font-bold mb-1">

        Interpretação

        </h3>

        <p>{data.interpretation}</p>

        </div>

    )

}
