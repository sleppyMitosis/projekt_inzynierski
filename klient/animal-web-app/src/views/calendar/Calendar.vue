<script setup="ts">
import { useAppointmentStore } from "@/stores/appointmentsStore";
import { storeToRefs } from "pinia";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import AppoitmentItem from "@/views/calendar/AppoitmentItem.vue";
import NewAppoitment from "@/views/calendar/NewAppoitment.vue";
import { computed } from "vue";
import EditAppoitment from "@/views/calendar/EditAppoitment.vue";

const appointmentStore = useAppointmentStore();
appointmentStore.getAppointments();

const {
  appointments,
  isNewAppointmentOpen,
  isEditAppoitmentOpen,
  selectedAppointment,
} = storeToRefs(appointmentStore);

const sortedAppointments = computed(() => {
  return appointments.value.slice().sort((a, b) => {
    const dateA = new Date(`${a.appointment_date}T${a.appointment_time}`);
    const dateB = new Date(`${b.appointment_date}T${b.appointment_time}`);
    return dateA - dateB;
  });
});
</script>

<template>
  <div class="bg-[#F1F1F1] flex h-full w-full flex-col p-5">
    <div class="flex flex-col gap-6 py-6">
      <p class="text-[32px]">Wszystkie wizyty</p>
      <ButtonItem class="w-[180px]" @click="isNewAppointmentOpen = true"
        >Dodaj wizytę</ButtonItem
      >
    </div>
    <v-expand-x-transition>
      <div
        v-if="isNewAppointmentOpen"
        class="absolute top-0 right-0 z-10 w-[500px] h-screen"
      >
        <NewAppoitment />
      </div>
    </v-expand-x-transition>
    <v-expand-x-transition>
      <div
        v-if="isEditAppoitmentOpen"
        class="absolute top-0 right-0 z-10 w-[500px] h-screen"
      >
        <EditAppoitment />
      </div>
    </v-expand-x-transition>
    <div
      class="bg-sky-100 w-full flex py-3 items-center gap-2 border rounded shrink-1"
    >
      <div class="w-[150px] text-lg shrink-1 pl-4">Stan</div>
      <div class="w-[100px] text-lg shrink-1">Data</div>
      <div class="w-[90px] text-lg shrink-1">Godzina</div>
      <div class="w-[160px] text-lg shrink-1">Nazwa wizyty</div>
      <div class="w-[120px] text-lg shrink-1">Zwierzak</div>
      <div class="w-[200px] text-lg shrink-1">Opis</div>
    </div>
    <div
      v-if="sortedAppointments && sortedAppointments.length > 0"
      class="flex flex-row gap-5 flex-wrap"
    >
      <AppoitmentItem
        v-for="appointment in sortedAppointments"
        :appointment="appointment"
        :key="appointment.id"
      />
    </div>
    <div
      class="flex justify-center items-center align-center text-[20px] font-base py-4"
      v-else
    >
      Brak wizyt. Dodaj nową wizytę.
    </div>
  </div>
</template>
