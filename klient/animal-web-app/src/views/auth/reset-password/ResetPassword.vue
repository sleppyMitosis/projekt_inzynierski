<script setup lang="ts">
import { ref } from "vue";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { useUserStore } from "@/stores/profileStore";
import { AxiosError } from "axios";
import { type ErrorResponse } from "@/models/common.model";

const email = ref("");
const username = ref("");
const showAlert = ref(false);
const userStore = useUserStore();

const submitResetRequest = async () => {
  try {
    await userStore.resetPassword({
      email: email.value,
      username: username.value,
    });
    showAlert.value = true;
    setTimeout(() => {
      showAlert.value = false;
    }, 3000);
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
        Wiadomość o zresetowaniu hasła została wysłana!
      </v-alert>
      <div
        class="w-[550px] h-[500px] bg-white/[0.4] rounded-xl flex flex-col items-center justify-center"
      >
        <div class="text-4xl text-center">Zresetuj hasło</div>
        <div class="flex flex-col gap-2 pt-8 items-center">
          <p class="pb-6 px-6 flex justify-center text-center">
            Wpisz swój adres e-mail, który był przez Ciebie użyty do
            rejestracji. Wyślemy do Ciebie wiadomość do resetowanie hasła.
          </p>
          <div class="w-80 h-10 rounded">
            <v-text-field
              label="Adres email"
              variant="outlined"
              bg-color="#fff"
              v-model="email"
            ></v-text-field>
          </div>
        </div>

        <div class="rounded flex items-center justify-center pt-8">
          <ButtonItem @click="submitResetRequest">Resetuj hasło</ButtonItem>
        </div>
      </div>
    </div>
  </div>
</template>
