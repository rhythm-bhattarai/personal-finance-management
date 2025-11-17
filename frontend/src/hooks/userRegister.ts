import {useState} from "react"
import {registerUser} from "../services/AuthServices/AuthService"

interface RegisterFormData {
    username: string;
    email: string;
    password: string;
    confirmPassword: string;
    firstName: string;
    lastName: string;
}

export function useUserRegister() {
    const [formData, setFormData] = useState<RegisterFormData>({
        username: "",
        email: "",
        password: "",
        confirmPassword: "",
        firstName: "",
        lastName: "",
    })

    const [error, setError] = useState<string>("")
    const [loading, setLoading] = useState<boolean>(false)

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const {name, value} = e.target
        setFormData({...formData, [name]: value})
    }

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        if (formData.password !== formData.confirmPassword) {
            setError("Passwords do not match")
            return
        }
        setError("")
        setLoading(true)
        try {
            await registerUser({
                username: formData.username,
                email: formData.email,
                password: formData.password,
                first_name: formData.firstName,
                last_name: formData.lastName,
            })
        } catch (err: any) {
            setError(err.response?.data?.message || "Registration failed")
        } finally {
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