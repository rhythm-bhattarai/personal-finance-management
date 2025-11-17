import {useState} from "react"
import {loginUser} from "../services/AuthServices/AuthService"

interface LoginData{
    email:string;
    password:string;
}

export function useUserLogin(){
    const [formData, setFormData] = useState<LoginData>({
        email:"",
        password:"",
    })

    const [error, setError] = useState<string>("")
    const [loading, setLoading] = useState<boolean>(false)

    const handleChange = (e:React.ChangeEvent<HTMLInputElement>)=>{
        const {name, value} = e.target
        setFormData({...formData, [name]:value})
    }

    const handleSubmit = async (e:React.FormEvent)=>{
        e.preventDefault()
        setError("")
        setLoading(true)
        try{
            const response = await loginUser({
                email:formData.email,
                password:formData.password,
            })
            localStorage.setItem("token", response.accessToken)
        } catch(err:any){
            setError(err.response?.data?.message || "Login failed")
        } finally{
            setLoading(false)
        }
    }
    return {
        formData,
        error,
        loading,
        handleChange,
        handleSubmit,
    }
}