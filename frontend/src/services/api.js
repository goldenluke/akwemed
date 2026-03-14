import axios from "axios"

const api = axios.create({
    baseURL:"http://localhost:8000/api"
})

export const consult = async(text)=>{

    const res = await api.post("/consult/",{
        text
    })

    return res.data
}
