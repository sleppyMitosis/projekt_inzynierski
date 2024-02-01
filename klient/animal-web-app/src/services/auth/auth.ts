import router from "@/router";
import { Route } from "@/router/route";
import type { LoginBody } from "@/services/auth/auth.model";
import userService from "@/services/auth/authService";
import { useUserStore } from "@/stores/profileStore";

export default {
  login(body: LoginBody): Promise<void> {
    const userStore = useUserStore();

    return userService.login(body.username, body.password).then((response) => {
      if (response.status === 200) {
        userStore.getUserFromApi();
        router.push(Route.calendar.path);
      }
    });
  },

  isAuthenticated(): boolean {
    const userStore = useUserStore();
    return userStore.isUserLoggedIn;
  },
};
