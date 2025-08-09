import axios  from "axios";

export const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    timeout: 5000
});

api.interceptors.request.use((config)=>{
    let token = localStorage.getItem('access_token')
    if (token){
        config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config
})