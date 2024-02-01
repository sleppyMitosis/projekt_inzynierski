<script setup lang="ts">
import { ref, Ref } from "vue";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import userService from "@/services/user/userService";
import { useRouter } from "vue-router";
import { Route } from "@/router/route";
import DatePicker from "@vuepic/vue-datepicker";

const showSuccessAlert = ref(false);
const username = ref("");
const password = ref("");
const email = ref("");
const phoneNumber = ref("");
const vetPhoneNumber = ref("");
const router = useRouter();
const show1 = ref<boolean>(false);

const rules = {
  required: (value: string) => !!value || "Pole jest wymagane",
  positiveNumber: (value: number) =>
    value > 0 || "Wartość musi być większa niż 0",
};
const registerUser = async (isActive: Ref<boolean>) => {
  const response = await userService.registerUser({
    username: username.value,
    password: password.value,
    email: email.value,
    phone_number: phoneNumber.value,
    vet_phone_number: vetPhoneNumber.value,
  });
  if (response.status === 200 || response.status === 201) {
    showSuccessAlert.value = true;
    setTimeout(() => {
      router.push({ name: "loginForm" });
    }, 3000);
  }
};
</script>
<template>
  <div
    class="flex justify-center items-center h-screen w-screen bg-gradient-to-r from-indigo-300 via-sky-300 to-emerald-200"
  >
    <v-alert type="success" v-model="showSuccessAlert" dismissible>
      Konto zostało stworzone!
    </v-alert>
    <div
      class="w-[700px] h-[7000px] bg-white/[0.4] rounded-xl flex flex-col items-center justify-center"
    >
      <div class="text-4xl text-center pb-5">Rejestracja</div>
      <div class="flex flex-col gap-2 items-center">
        <div class="w-96 rounded">
          <v-text-field
            v-model="username"
            label="Login"
            variant="outlined"
            bg-color="#fff"
            :rules="[rules.required]"
          ></v-text-field>
        </div>
        <div class="w-[460px] rounded pl-[38px]">
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
        <div class="w-96 rounded">
          <v-text-field
            v-model="email"
            label="E-mail"
            variant="outlined"
            bg-color="#fff"
            :rules="[rules.required]"
          ></v-text-field>
        </div>
        <div class="w-96 rounded">
          <v-text-field
            v-model="phoneNumber"
            label="Numer telefonu"
            variant="outlined"
            bg-color="#fff"
            :rules="[rules.required]"
          ></v-text-field>
        </div>
        <div class="w-96 rounded">
          <v-text-field
            v-model="vetPhoneNumber"
            label="Numer telefonu weterynarza"
            variant="outlined"
            bg-color="#fff"
            :rules="[rules.required]"
          ></v-text-field>
        </div>
      </div>

      <div class="rounded flex items-center justify-center pt-4">
        <ButtonItem @click="registerUser">Zarejestruj się</ButtonItem>
      </div>
    </div>
  </div>
</template>
