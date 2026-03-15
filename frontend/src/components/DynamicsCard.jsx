export default function DynamicsCard({ data }) {

    return (

        <div className="bg-gray-900 p-3 rounded-lg">

        <h3 className="text-purple-400 text-sm font-bold mb-1">

        Dinâmica do Sistema

        </h3>

        <div className="grid grid-cols-3 gap-2 text-sm">

        <div>
        <span className="text-gray-400">Estado</span>
        <p>{data.metastable_state}</p>
        </div>

        <div>
        <span className="text-gray-400">Volatilidade</span>
        <p>{Number(data.volatility).toFixed(3)}</p>
        </div>

        <div>
        <span className="text-gray-400">Complexidade</span>
        <p>{Number(data.complexity).toFixed(3)}</p>
        </div>

        </div>

        </div>

    )

}
