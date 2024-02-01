<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import DatePicker from "@vuepic/vue-datepicker";
import { useDrugsStore } from "@/stores/drugsStore";
import { storeToRefs } from "pinia";
import { ref, computed, watch } from "vue";

const drugsStore = useDrugsStore();
const { isNewDrugOpen, animalOptions, selectedDrug } = storeToRefs(drugsStore);
drugsStore.getAnimals();

const name = ref("");
const animal_id = ref(undefined);
const start_date = ref("");
const end_date = ref("");
const dosage_count = ref(1);
const showAlertError = ref(false);

const rules = {
  required: (value: string) => !!value || "Pole jest wymagane",
  positiveNumber: (value: number) =>
    value > 0 || "Wartość musi być większa niż 0",
};

watch(dosage_count, (newValue) => {
  if (newValue < 0) {
    dosage_count.value = 1;
  }
});

const addNewDrug = async () => {
  if (
    !name.value ||
    !animal_id.value ||
    !start_date.value ||
    !end_date.value ||
    !dosage_count.value
  ) {
    showAlertError.value = true;
    setTimeout(() => {
      showAlertError.value = false;
    }, 6000);
    return;
  }
  const newDrug = {
    name: name.value,
    animal_id: animal_id.value,
    start_date: formatDate(start_date.value),
    end_date: formatDate(end_date.value),
    dosage_count: dosage_count.value,
  };

  await drugsStore.postDrug(newDrug);
  isNewDrugOpen.value = false;
};

function formatDate(dateString: string | null): string {
  if (!dateString) return "";
  const date = new Date(dateString);
  if (isNaN(date.getTime())) {
    return "";
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
      <v-alert type="error" v-model="showAlertError" dismissible>
        Pola nazwa leku, zwierzę, data rozpoczęcia, data zakończenia i liczba
        dawek są wymagane!
      </v-alert>
    </div>
    <div class="flex justify-end">
      <font-awesome-icon
        :icon="['fas', 'xmark']"
        style="color: #000000"
        size="2xl"
        @click="isNewDrugOpen = false"
      />
    </div>
    <div
      class="relative bg-color-white w-full flex flex-col items-start justify-start px-6 box-border gap-[8px] text-left text-sm text-colors-text-field-standard font-body-standard-regular"
    >
      <div class="flex gap-6 w-full pb-4">
        <p class="text-[28px]">Dodaj lek</p>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          variant="outlined"
          density="compact"
          label="Nazwa leku"
          placeholder="Nazwa leku"
          v-model="name"
          :rules="[rules.required]"
        ></v-text-field>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start pb-4"
      >
        <v-select
          variant="outlined"
          bg-color="#fff"
          :items="animalOptions"
          item-title="label"
          item-value="value"
          density="compact"
          label="Zwierzę"
          hide-details
          v-model="animal_id"
          clearable
          :rules="[rules.required]"
        ></v-select>
      </div>
      <div class="flex items-center gap-4 pb-4">
        <div class="flex items-center gap-4 pb-4">
          <DatePicker
            :enable-time-picker="false"
            placeholder="Data rozpoczęcia dawkowania"
            format="yyyy-MM-dd"
            locale="pl"
            v-model="start_date"
          />
          <span>-</span>
          <DatePicker
            :enable-time-picker="false"
            placeholder="Data zakończenia dawkowania"
            format="yyyy-MM-dd"
            locale="pl"
            v-model="end_date"
          />
        </div>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          variant="outlined"
          density="compact"
          label="Liczba dawek"
          placeholder="Liczba dawek"
          v-model.number="dosage_count"
          :rules="[rules.required]"
        ></v-text-field>
      </div>
    </div>
    <div class="flex justify-center flex-col w-full pt-6">
      <ButtonItem @click="addNewDrug">Zapisz zmiany</ButtonItem>
      <ButtonItem type="tertiary" @click="isNewDrugOpen = false"
        >Anuluj</ButtonItem
      >
    </div>
  </div>
</template>
