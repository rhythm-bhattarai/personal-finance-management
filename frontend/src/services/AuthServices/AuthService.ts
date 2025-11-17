import apiClient from "../apiClient";

interface RegisterData {
    username: string;
    email: string;
    password: string;
    first_name: string;
    last_name: string;
}

interface LoginData {
    email: string;
    password: string;
}

export async function registerUser(data: RegisterData): Promise<any> {
    const response = await apiClient.post("/users/", data);
    return response.data;
}

export async function loginUser(data: LoginData): Promise<any> {
    const response = await apiClient.post("/users/login", data);
    return response.data;
}