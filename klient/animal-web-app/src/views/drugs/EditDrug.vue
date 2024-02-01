<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import DatePicker from "@vuepic/vue-datepicker";
import { useDrugsStore } from "@/stores/drugsStore";
import { storeToRefs } from "pinia";
import { ref } from "vue";

const drugsStore = useDrugsStore();
const { isEditDrugOpen, animalOptions, selectedDrug } = storeToRefs(drugsStore);
drugsStore.getAnimals();

const rules = {
  required: (value: string) => !!value || "Pole jest wymagane",
  positiveNumber: (value: number) =>
    value > 0 || "Wartość musi być większa niż 0",
};

const name = ref(selectedDrug.value?.name || "");
const animal_id = ref(selectedDrug.value?.animal?.id);
const start_date = ref(selectedDrug.value?.start_date || "");
const end_date = ref(selectedDrug.value?.end_date || "");
const dosage_count = ref(selectedDrug.value?.dosage_count || 0);
const showAlertError = ref(false);

const addNewDrug = async () => {
  const newDrug = {
    name: name.value,
    animal_id: animal_id.value,
    start_date: formatDate(start_date.value),
    end_date: formatDate(end_date.value),
    dosage_count: dosage_count.value,
  };

  await drugsStore.postDrug(newDrug);
  isEditDrugOpen.value = false;
};

const onSaveEdit = async () => {
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
  if (selectedDrug.value && selectedDrug.value.id !== undefined) {
    const drugId = selectedDrug.value.id;
    const drugData = {
      name: name.value,
      animal_id: animal_id.value,
      start_date: formatDate(start_date.value),
      end_date: formatDate(end_date.value),
      dosage_count: dosage_count.value,
    };
    await drugsStore.editDrug(drugId, drugData);
    drugsStore.getDrugs();
    isEditDrugOpen.value = false;
  }
};

const onClickDeleteDrug = async () => {
  if (selectedDrug.value && selectedDrug.value.id !== undefined) {
    const drugId = selectedDrug.value.id;
    await drugsStore.deleteDrug(drugId);
    isEditDrugOpen.value = false;
  }
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
        @click="isEditDrugOpen = false"
      />
    </div>
    <div
      class="relative bg-color-white w-full flex flex-col items-start justify-start px-6 box-border gap-[8px] text-left text-sm text-colors-text-field-standard font-body-standard-regular"
    >
      <div class="flex gap-6 w-full pb-4">
        <p class="text-[28px]">Edytuj lek</p>
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
              <v-card title="Usuń lek">
                <v-card-text>
                  Jesteś pewnien, że chcesz usunąć lek:
                  {{ selectedDrug?.name }}
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <ButtonItem @click="isActive.value = false" type="tertiary"
                    >Anuluj</ButtonItem
                  >
                  <ButtonItem size="medium" @click="onClickDeleteDrug"
                    >Usuń lek</ButtonItem
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
        <DatePicker
          :enable-time-picker="false"
          placeholder="Data rozpoczęcia dawkowania"
          format="yyyy-MM-dd"
          locale="pl"
          v-model="start_date"
          :rules="[rules.required]"
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
      <ButtonItem @click="onSaveEdit">Zapisz zmiany</ButtonItem>
      <ButtonItem type="tertiary">Anuluj</ButtonItem>
    </div>
  </div>
</template>

<style scoped></style>
