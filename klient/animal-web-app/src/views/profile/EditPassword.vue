<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useUserStore } from "@/stores/profileStore";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { AxiosError } from "axios";
import { ErrorResponse } from "@/models/common.model";

const newPassword = ref("");
const confirmPassword = ref("");
const router = useRouter();
const route = useRoute();
const userStore = useUserStore();
const showAlert = ref(false);

let uid = "";
let token = "";

onMounted(() => {
  uid = (route.params.uid as string) ?? "";
  token = (route.params.token as string) ?? "";

  if (!uid || !token) {
    console.error("Invalid or missing UID and token");
    router.push({ name: "loginForm" });
  }
});

const submitNewPassword = async () => {
  const editPasswordData = {
    uid,
    token,
    password: newPassword.value,
  };
  try {
    showAlert.value = true;
    await userStore.editPassword(editPasswordData);
    setTimeout(() => {
      showAlert.value = false;
    }, 3000);
    setTimeout(() => {
      router.push({ name: "loginForm" });
    }, 4000);
  } catch (error) {
    const axiosError = error as AxiosError<ErrorResponse>;
  }
};
</script>
<template>
  <div
    class="flex justify-center items-center h-screen w-screen bg-gradient-to-r from-indigo-300 via-sky-300 to-emerald-200"
  >
    <div class="flex flex-col gap-5">
      <v-alert type="success" v-model="showAlert" dismissible>
        Hasło zostało zmienione.
      </v-alert>
      <div
        class="w-[550px] h-[500px] bg-white/[0.4] rounded-xl flex flex-col items-center justify-center"
      >
        <div class="text-4xl text-center">Zresetuj hasło</div>
        <div class="flex flex-col gap-2 pt-8 items-center">
          <p class="pb-6 px-6 flex justify-center text-center">
            Podaj nowe hasło
          </p>
          <div class="w-80 h-10 rounded pb-20">
            <div class="relative">
              <input
                type="password"
                id="password"
                placeholder="Hasło"
                class="bg-white rounded py-6 px-6 peer placeholder-transparent h-10 w-full border border-gray-800 focus:border-black text-gray-900"
                v-model="newPassword"
              />
              <label
                for="password"
                class="absolute left-4 -top-3.5 text-gray-900 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 peer-focus:-top-4 peer-focus:text-black peer-focus:text-sm"
                >Hasło</label
              >
            </div>
          </div>
          <div class="w-80 h-10 rounded">
            <div class="relative">
              <input
                type="password"
                id="confirm-password"
                placeholder="Powtórz hasło"
                class="bg-white rounded py-6 px-6 peer placeholder-transparent h-10 w-full border border-gray-800 focus:border-black text-gray-900"
              />
              <label
                for="confirm-password"
                class="absolute left-4 -top-3.5 text-gray-900 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 peer-focus:-top-4 peer-focus:text-black peer-focus:text-sm"
                >Powtórz hasło</label
              >
            </div>
          </div>
        </div>
      </div>
      <div class="rounded flex items-center justify-center pt-8">
        <ButtonItem @click="submitNewPassword">Resetuj hasło</ButtonItem>
      </div>
    </div>
  </div>
</template>
