<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import DatePicker from "@vuepic/vue-datepicker";
import { useAppointmentStore } from "@/stores/appointmentsStore";
import { storeToRefs } from "pinia";
import { ref, watch } from "vue";

const appointmentStore = useAppointmentStore();
appointmentStore.getAppointments();
appointmentStore.getAnimals();

const {
  appointments,
  selectedAppointment,
  isEditAppoitmentOpen,
  animalOptions,
} = storeToRefs(appointmentStore);

const name = ref(selectedAppointment.value?.name || "");
const animal_id = ref(selectedAppointment.value?.animal?.id);
const description = ref(selectedAppointment.value?.description || "");
const appointment_time = ref(selectedAppointment.value?.appointment_time || "");
const appointment_date = ref(selectedAppointment.value?.appointment_date || "");

function formatTime(timeString: string): string {
  if (!timeString) return "";
  const time = new Date(`1970-01-01T${timeString}`);

  if (isNaN(time.getTime())) {
    return "";
  }

  const hours = time.getHours().toString().padStart(2, "0");
  const minutes = time.getMinutes().toString().padStart(2, "0");

  return `${hours}:${minutes}`;
}

const onSaveEdit = async () => {
  if (selectedAppointment.value && selectedAppointment.value.id !== undefined) {
    const appointmentId = selectedAppointment.value.id;
    const appointmentData = {
      name: name.value,
      animal_id: animal_id.value,
      description: description.value,
      appointment_time: formatTime(appointment_time.value),
      appointment_date: formatDate(appointment_date.value),
    };
    await appointmentStore.editAppointment(appointmentId, appointmentData);
    appointmentStore.getAppointments();
    isEditAppoitmentOpen.value = false;
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

const rules = {
  required: (value: string) => !!value || "Pole jest wymagane",
  positiveNumber: (value: number) =>
    value > 0 || "Wartość musi być większa niż 0",
};

const onClickDeleteAppointment = async () => {
  if (selectedAppointment.value && selectedAppointment.value.id !== undefined) {
    const appointmentId = selectedAppointment.value.id;
    await appointmentStore.deleteAppointment(appointmentId);
    isEditAppoitmentOpen.value = false;
  }
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
        @click="isEditAppoitmentOpen = false"
      />
    </div>
    <div
      class="relative bg-color-white w-full flex flex-col items-start justify-start px-6 box-border gap-[8px] text-left text-sm text-colors-text-field-standard font-body-standard-regular"
    >
      <div class="flex gap-6 w-full pb-4">
        <p class="text-[28px]">Edytuj wizytę</p>
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
              <v-card title="Usuń wizytę">
                <v-card-text>
                  Jesteś pewnien, że chcesz usunąć wizytę:
                  {{ selectedAppointment?.name }} z dnia
                  {{ selectedAppointment?.appointment_date }}
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <ButtonItem @click="isActive.value = false" type="tertiary"
                    >Anuluj</ButtonItem
                  >
                  <ButtonItem @click="onClickDeleteAppointment" size="medium"
                    >Usuń wizytę</ButtonItem
                  >
                </v-card-actions>
              </v-card>
            </template>
          </v-dialog>
        </div>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start pb-5"
      >
        <DatePicker
          :enable-time-picker="false"
          placeholder="Data wizyty"
          format="yyyy-MM-dd"
          locale="pl"
          v-model="appointment_date"
          :rules="[rules.required]"
        ></DatePicker>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start pb-5"
      >
        <input
          type="time"
          v-model="appointment_time"
          class="border-2 border-gray-900 border rounded px-3 py-2 w-full"
          placeholder="Godzina wizyty"
          :rules="[rules.required]"
        />
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          v-model="name"
          variant="outlined"
          density="compact"
          label="Nazwa wizyty"
          placeholder="Nazwa wizyty"
          :rules="[rules.required]"
        ></v-text-field>
      </div>
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start pb-5"
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
      <div
        class="self-stretch rounded bg-color-white flex flex-row items-center justify-start"
      >
        <v-text-field
          v-model="description"
          variant="outlined"
          density="compact"
          label="Opis wizyty"
          placeholder="Opis wizyty"
          :rules="[rules.required]"
        ></v-text-field>
      </div>
    </div>
    <div class="flex justify-center flex-col w-full pt-6">
      <ButtonItem @click="onSaveEdit">Zapisz zmiany</ButtonItem>
      <ButtonItem type="tertiary" @click="isEditAppoitmentOpen = false"
        >Anuluj</ButtonItem
      >
    </div>
  </div>
</template>
