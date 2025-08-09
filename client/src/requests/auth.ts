import type { StoreApi } from "zustand";
import type { LoginState, registerUser } from "../store/authStore";

import { api } from "../utils/api";

export const handle_login = async (
  set: StoreApi<LoginState>["setState"],
  username: string,
  password: string
) => {
  set({ loading: true, error: null });
  try {
    const res = await api.post("/auth/login", {
      username: username,
      password: password,
    });
    if (res) {
      set({
        user: {
          username: res.data.user.username,
          email: res.data.user.email,
          fullname: res.data.user.fullname,
        },
        loading: false,
        token: res.data.access_token,
      });
      return {
        success: true,
        message: "Login successful",
      };
    }
  } catch (error) {
    set({
      error: "Invalid username or password",
      loading: false,
    });
  }
return { success: false, message: "Login failed" };
};

export const handle_register = async (
  set: StoreApi<LoginState>["setState"],
  registerUser: registerUser
) => {
  set({ loading: true, error: null });
  try {
    await api.post("/auth/register", registerUser);
    set({ loading: false, error: null });
    return { success: true, message: "Registration successful" };
  } catch (error) {
    set({
      error: "Registration failed. Please try again.",
      loading: false,
    });
    return {
      success: false,
      message: "Registration failed. Please try again.",
    };
  }
};
