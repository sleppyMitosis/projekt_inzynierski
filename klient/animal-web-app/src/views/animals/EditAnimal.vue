<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { storeToRefs } from "pinia";
import { useAnimalsStore } from "@/stores/animalsStore";
import { ref } from "vue";
import DatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";
import { AxiosError } from "axios";
import { type ErrorResponse } from "@/models/common.model";

const animalStore = useAnimalsStore();
const { animals, isEditAnimalOpen, isNewAnimalOpen, selectedAnimal } =
  storeToRefs(animalStore);

const name = ref(selectedAnimal.value?.name || "");
const species = ref(selectedAnimal.value?.species || "");
const chip = ref(selectedAnimal.value?.chip_number || "");
const birthday = ref(selectedAnimal.value?.date_of_birth || "");
const pedigree = ref(selectedAnimal.value?.pedigree_number || "");
const showAlertError = ref(false);

const onSaveEditAnimal = async () => {
  if (!name.value || !species.value || !birthday.value) {
    showAlertError.value = true;
    setTimeout(() => {
      showAlertError.value = false;
    }, 3000);
    return;
  }
  if (selectedAnimal.value && selectedAnimal.value.id !== undefined) {
    const animalId = selectedAnimal.value.id;
    const updatedAnimal = {
      name: name.value,
      species: species.value,
      chip_number: chip.value,
      date_of_birth: formatDate(birthday.value),
      pedigree_number: pedigree.value,
    };
    await animalStore.editAnimal(animalId, updatedAnimal);
    animalStore.getAnimals();
    isEditAnimalOpen.value = false;
  }
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

const onClickDeleteAnimal = async () => {
  if (selectedAnimal.value && selectedAnimal.value.id !== undefined) {
    const animalId = selectedAnimal.value.id;
    await animalStore.deleteAnimal(animalId);
    isEditAnimalOpen.value = false;
  }
};
</script>

<template>
  <div
    class="overflow-y-auto bg-white w-full h-full flex flex-col px-6 pt-6 pb-6 text-left text-base border-l border-solid border-grey-two"
  >
    <div class="h-5 pb-20">
      <v-alert type="error" v-model="showAlertError" dismissible>
        Pola imię, gatuken i data urodzenia są wymagane!
      </v-alert>
    </div>
    <div class="flex justify-end">
      <font-awesome-icon
        :icon="['fas', 'xmark']"
        style="color: #000000"
        size="2xl"
        @click="isEditAnimalOpen = false"
      />
    </div>
    <div
      class="relative bg-color-white w-full flex flex-col items-start justify-start px-6 box-border gap-[8px] text-left text-sm text-colors-text-field-standard font-body-standard-regular"
    >
      <div class="flex gap-6 w-full pb-4">
        <p class="text-[28px]">Edytuj zwierzaka</p>
        <div class="mt-[-10px]">
          <v-dialog width="500">
            <template v-slot:activator="{ props }">
              <v-btn
                icon="mdi-delete-outline"
                class="bg-sky-300"
                v-bind="props"
              ></v-btn>
            </template>

            <template v-slot:default="{ isActive }">
              <v-card title="Usuń zwierzaka">
                <v-card-text>
                  Jesteś pewnien, że chcesz usunąć zwierzaka:
                  {{ selectedAnimal?.name }}
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <ButtonItem @click="isActive.value = false" type="tertiary"
                    >Anuluj</ButtonItem
                  >
                  <ButtonItem @click="onClickDeleteAnimal" size="medium"
                    >Usuń zwierzaka</ButtonItem
                  >
                </v-card-actions>
              </v-card>
            </template>
          </v-dialog>
        </div>
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
      <ButtonItem @click="onSaveEditAnimal">Zapisz zmiany</ButtonItem>
      <ButtonItem type="tertiary" @click="isEditAnimalOpen = false"
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
