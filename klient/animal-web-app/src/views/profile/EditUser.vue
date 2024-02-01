<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { useUserStore } from "@/stores/profileStore";
import { storeToRefs } from "pinia";

const rules = {
  required: (value: string) => !!value || "Pole jest wymagane",
  positiveNumber: (value: number) =>
    value > 0 || "Wartość musi być większa niż 0",
};

const userStore = useUserStore();
const {
  isEditPasswordOpen,
  email,
  first_name,
  last_name,
  phone_number,
  vet_phone_number,
} = storeToRefs(userStore);

const saveChanges = async () => {
  const updatedData = {
    first_name: first_name.value,
    last_name: last_name.value,
    email: email.value,
    phone_number: phone_number.value,
    vet_phone_number: vet_phone_number.value,
  };

  await userStore.editProfile(updatedData);
  userStore.getUserFromApi();
  isEditPasswordOpen.value = false;
};
</script>

<template>
  <div
    class="overflow-y-auto bg-white w-full h-full flex flex-col px-6 pt-6 pb-6 text-left text-base border-l border-solid border-grey-two"
  >
    <div class="flex justify-end">
      <font-awesome-icon
        :icon="['fas', 'xmark']"
        style="color: #000000"
        size="2xl"
        @click="isEditPasswordOpen = false"
      />
    </div>
    <div
      class="relative bg-color-white w-full flex flex-col items-start justify-start py-4 px-6 box-border gap-[8px] text-left text-sm text-colors-text-field-standard font-body-standard-regular"
    >
      <div class="flex gap-2 w-full">
        <p class="text-[28px] pb-4">Edytuj profil</p>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          v-model="email"
          variant="outlined"
          density="compact"
          label="Adres e-mail"
          placeholder="Adres e-mail"
          :rules="[rules.required]"
        ></v-text-field>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          v-model="phone_number"
          variant="outlined"
          density="compact"
          label="Numer telefonu"
          placeholder="Numer telefonu"
          :rules="[rules.required]"
        ></v-text-field>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          v-model="vet_phone_number"
          variant="outlined"
          density="compact"
          label="Numer telefonu weterynarza"
          placeholder="Numer telefonu weterynarza"
          :rules="[rules.required]"
        ></v-text-field>
      </div>
    </div>
    <div class="flex justify-center flex-col w-full pt-6">
      <ButtonItem @click="saveChanges">Zapisz zmiany</ButtonItem>
      <ButtonItem type="tertiary" @click="isEditPasswordOpen = false"
        >Anuluj</ButtonItem
      >
    </div>
  </div>
</template>
