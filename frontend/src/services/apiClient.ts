import axios from "axios"

const {REACT_APP_BASE_API_URL} = process.env

const apiClient = axios.create({
    baseURL: REACT_APP_BASE_API_URL,
    headers: {
        "Authorization": `Bearer ${localStorage.getItem("token")}`,
        withCredentials: "true"
    }
})

async function refreshToken(): Promise<string> {
    try {
        const response = await axios.post(`${REACT_APP_BASE_API_URL}/auth/refresh`, {}, {
            withCredentials: true
        })
        return response.data.accessToken
    } catch (error) {
        console.error("Failed to refresh token", error)
        throw error
    }
}

axios.interceptors.request.use(
    res => res,
    async error => {
        if (error.response && error.response.status === 401) {
            const newaccessToken = await refreshToken()
            
            localStorage.setItem("token", newaccessToken)

            error.config.headers["Authorization"] = `Bearer ${newaccessToken}`
            return axios(error.config)
        }
        return Promise.reject(error)
    }
)



export default apiClient