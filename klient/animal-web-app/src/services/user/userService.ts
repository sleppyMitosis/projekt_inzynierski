import apiClient from "@/services/apiClient";
import router from "@/router";
import type {
  UserResponse,
  UserEditData,
  UserRegistrationData,
} from "@/services/user/user.model";
import { PasswordResetBody } from "@/services/user/user.model";

export default {
  getUserDetail(): Promise<UserResponse> {
    return apiClient.get("/user/api/user-detail/");
  },

  async deleteUser() {
    try {
      const response = await apiClient.delete("user/api/delete-user/");
      localStorage.removeItem("token");
      delete apiClient.defaults.headers.common["Authorization"];
      router.push({ name: "loginForm" });
      return response;
    } catch (error) {
      console.error("Error deleting user:", error);
    }
  },

  async updateProfile(updatedProfile: UserEditData) {
    const response = await apiClient.put("user/api/edit-profile/", {
      ...updatedProfile,
    });
    return response.data;
  },

  async registerUser(userData: UserRegistrationData) {
    return apiClient.post("/user/api/register/", userData);
  },

  async resetPasswordRequest(resetPassword: PasswordResetBody) {
    return apiClient.post("/user/api/password-reset-request/", resetPassword);
  },

  async editPassword(uid: string, token: string, newPassword: string) {
    const response = await apiClient.post(
      `/user/api/password-reset-confirm/${uid}/${token}/`,
      {
        password: newPassword,
      },
    );
    return response;
  },
};
