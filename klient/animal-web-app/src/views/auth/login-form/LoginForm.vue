<script lang="ts">
import { defineComponent, ref } from "vue";
import auth from "@/services/auth/auth";
import { useRouter } from "vue-router";
import { Route } from "@/router/route";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
export default defineComponent({
  components: { ButtonItem },
  setup() {
    const login = ref("");
    const password = ref("");
    const router = useRouter();

    const sendLoginRequest = async () => {
      try {
        await auth.login({ username: login.value, password: password.value });
        router.push(Route.dashboard.path);
      } catch (error) {
        console.error("Login failed:", error);
      }
    };

    const navigateToNewUser = () => {
      router.push({ name: "newUser" });
    };

    const navigateToResetPassword = () => {
      router.push({ name: "resetPassword" });
    };

    return {
      login,
      password,
      sendLoginRequest,
      navigateToNewUser,
      navigateToResetPassword,
    };
  },

  data: () => ({
    rules: {
      required: (value: string) => !!value || "Pole jest wymagane",
    },
    show1: false,
  }),
});
</script>
<template>
  <div
    class="flex justify-center items-center h-screen w-screen bg-gradient-to-r from-indigo-300 via-sky-300 to-emerald-200"
  >
    <div
      class="w-[550px] h-[500px] bg-white/[0.4] rounded-xl flex flex-col items-center justify-center"
    >
      <div class="text-4xl text-center">Zaloguj się</div>
      <div class="flex flex-col gap-2 pt-8 items-center">
        <div class="w-80 h-10 rounded">
          <v-text-field
            v-model="login"
            label="Login"
            variant="outlined"
            bg-color="#fff"
            :rules="[rules.required]"
          ></v-text-field>
        </div>
        <div class="w-[395px] rounded pt-8 pl-[35px]">
          <v-text-field
            v-model="password"
            label="Hasło"
            variant="outlined"
            bg-color="#fff"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show1 ? 'text' : 'password'"
            @click:append="show1 = !show1"
            :rules="[rules.required]"
          ></v-text-field>
        </div>
      </div>
      <p
        class="flex [text-decoration:underline] font-semibold justify-center pl-36 py-2 cursor-pointer"
        @click="navigateToResetPassword"
      >
        Nie pamiętasz hasła?
      </p>
      <p
        class="flex [text-decoration:underline] font-semibold justify-center pl-36 py-2 cursor-pointer"
        @click="navigateToNewUser"
      >
        Nie masz konta?
      </p>

      <div class="rounded flex items-center justify-center pt-8">
        <ButtonItem @click="sendLoginRequest">Zaloguj</ButtonItem>
      </div>
    </div>
  </div>
</template>
