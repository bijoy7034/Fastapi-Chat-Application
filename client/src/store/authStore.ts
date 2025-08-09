import { create } from "zustand";
import { handle_login, handle_register } from "../requests/auth";

interface User {
    username : string;
    email : string;
    fullname : string
}

export type registerUser = {
    username : string;
    email : string,
    fullname :string,
    password : string,
    confirm_password : string
}
type ApiResponse = {
    success: boolean;
    message: string;
};

export interface LoginState {
    user : User | null;
    error : string | null;
    token : string | null;
    loading : boolean;
    login: (username : string, password: string) => Promise<ApiResponse>;
    register: (registerUser: registerUser) => Promise<ApiResponse>;
}

export const useAuthStore = create<LoginState> ((set)=> ({
    user : null,
    error: null,
    token: null,
    loading : false,
    login : (username, password)=> handle_login(set, username, password),
    register: (registerUser: registerUser)=> handle_register(set, registerUser)
}))