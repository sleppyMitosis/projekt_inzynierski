<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { storeToRefs } from "pinia";
import { useAnimalsStore } from "@/stores/animalsStore";
import { ref, onMounted } from "vue";
import DatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";
import { AxiosError } from "axios";
import { type ErrorResponse } from "@/models/common.model";

const animalStore = useAnimalsStore();
const { animals, isNewAnimalOpen, selectedAnimal } = storeToRefs(animalStore);

const showAlert = ref(false);
const showAlertError = ref(false);
const name = ref("");
const species = ref("");
const chip = ref("");
const birthday = ref("");
const pedigree = ref("");

const addNewanimal = async () => {
  if (!name.value || !species.value || !birthday.value) {
    showAlertError.value = true;
    setTimeout(() => {
      showAlertError.value = false;
    }, 3000);
    return;
  }
  try {
    const isNameTaken = animals.value.some(
      (animal) => animal.name.toLowerCase() === name.value.toLowerCase(),
    );

    if (isNameTaken) {
      showAlert.value = true;
      setTimeout(() => {
        showAlert.value = false;
      }, 3000);
    }
    const newAnimal = {
      name: name.value,
      species: species.value,
      chip_number: chip.value,
      date_of_birth: formatDate(birthday.value),
      pedigree_number: pedigree.value,
    };
    await animalStore.postAnimal(newAnimal);
    animalStore.getAnimals();
    isNewAnimalOpen.value = false;
  } catch (error) {
    const axiosError = error as AxiosError<ErrorResponse>;

    if (axiosError.response && axiosError.response.data) {
    }
  }
};

const rules = {
  required: (value: string) => !!value || "Pole jest wymagane",
  positiveNumber: (value: number) =>
    value > 0 || "Wartość musi być większa niż 0",
};

function formatDate(dateString: string | null): string | null {
  if (!dateString) return null;
  const date = new Date(dateString);

  if (isNaN(date.getTime())) {
    return null;
  }

  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const day = date.getDate().toString().padStart(2, "0");

  return `${year}-${month}-${day}`;
}
</script>

<template>
  <div
    class="overflow-y-auto bg-white w-full h-full flex flex-col px-6 pt-6 pb-6 text-left text-base border-l border-solid border-grey-two"
  >
    <div class="h-5 pb-20">
      <v-alert type="warning" v-model="showAlert" dismissible>
        Zwierzę o takim imieniu już istnieje!
      </v-alert>
      <v-alert type="error" v-model="showAlertError" dismissible>
        Pola imię, gatuken i data urodzenia są wymagane!
      </v-alert>
    </div>
    <div class="flex justify-end">
      <font-awesome-icon
        :icon="['fas', 'xmark']"
        style="color: #000000"
        size="2xl"
        @click="isNewAnimalOpen = false"
      />
    </div>
    <div
      class="relative bg-color-white w-full flex flex-col items-start justify-start px-6 box-border gap-[8px] text-left text-sm text-colors-text-field-standard font-body-standard-regular"
    >
      <div class="flex gap-6 w-full pb-4">
        <p class="text-[28px]">Dodaj zwierzaka</p>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          variant="outlined"
          density="compact"
          label="Imię"
          placeholder="Imię"
          v-model="name"
          :rules="[rules.required]"
        ></v-text-field>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          variant="outlined"
          density="compact"
          label="Gatunek"
          placeholder="Gatunek"
          v-model="species"
          :rules="[rules.required]"
        ></v-text-field>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start pb-5"
      >
        <DatePicker
          :enable-time-picker="false"
          placeholder="Data Urodzenia"
          :format="'yyyy-MM-dd'"
          locale="pl"
          v-model="birthday"
          :rules="[rules.required]"
        ></DatePicker>
      </div>

      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          variant="outlined"
          density="compact"
          label="Numer chipa (opcjonlane)"
          placeholder="Numer chipa (opcjonlane)"
          v-model="chip"
        ></v-text-field>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          variant="outlined"
          density="compact"
          label="Numer rodowodu (opcjonalene)"
          placeholder="Numer rodowodu (opcjonalene)"
          v-model="pedigree"
        ></v-text-field>
      </div>
    </div>
    <div class="flex justify-center flex-col w-full pt-6">
      <ButtonItem @click="addNewanimal">Zapisz zmiany</ButtonItem>
      <ButtonItem type="tertiary" @click="isNewAnimalOpen = false"
        >Anuluj</ButtonItem
      >
    </div>
  </div>
</template>

<style>
.dp__theme_light {
  --dp-border-color: #aaaeb7;
  --dp-border-color-hover: #222226;
  --dp-primary-text-color: #222226;
  --dp-primary-color: #0ea5e9;
}
:root {
  --dp-input-padding: 9px 30px 9px 12px;
}
</style>
