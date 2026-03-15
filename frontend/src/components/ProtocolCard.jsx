export default function ProtocolCard({ data }) {

    return (

        <div className="bg-gray-900 p-3 rounded-lg">

        <h3 className="text-green-400 text-sm font-bold mb-1">

        Protocolo Clínico

        </h3>

        <p className="font-semibold">

        {data.protocol}

        </p>

        <p className="text-gray-300 text-sm">

        {data.recommendation}

        </p>

        </div>

    )

}
