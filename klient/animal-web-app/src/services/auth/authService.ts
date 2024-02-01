import apiClient from "@/services/apiClient";
import router from "@/router";

const login = async (username: string, password: string) => {
  try {
    const response = await apiClient.post("/user/api/login/", {
      username,
      password,
    });
    if (response.data && response.data.token) {
      localStorage.removeItem("token");
      delete apiClient.defaults.headers.common["Authorization"];

      localStorage.setItem("token", response.data.token);
      apiClient.defaults.headers.common[
        "Authorization"
      ] = `Token ${response.data.token}`;
    }
    return response;
  } catch (error) {
    console.error("Login error:", error);
    throw error;
  }
};

const logout = async () => {
  try {
    await apiClient.post("/user/api/logout/");
    localStorage.removeItem("token");
    delete apiClient.defaults.headers.common["Authorization"];
    router.push({ name: "loginForm" });
  } catch (error) {
    console.error("Logout failed:", error);
  }
};

export default {
  login,
  logout,
};
