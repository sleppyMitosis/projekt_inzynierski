<script setup lang="ts">
import { useAppointmentStore } from "@/stores/appointmentsStore";
import { type Appointment } from "@/services/appointments/appointment.model";
import { storeToRefs } from "pinia";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { computed } from "vue";

const props = defineProps<{ appointment: Appointment }>();
const appointmentStore = useAppointmentStore();

const { appointments, selectedAppointment, isEditAppoitmentOpen } =
  storeToRefs(appointmentStore);

const formattedTime = computed(() => {
  const time = props.appointment.appointment_time;
  return time ? time.substring(0, 5) : "";
});

const onClick = () => {
  isEditAppoitmentOpen.value = true;
  selectedAppointment.value = props.appointment;
};

const onClickAppointment = () => {
  selectedAppointment.value = props.appointment;
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
    class="w-full flex py-3 px-2 text-base gap-2 border-b border-r border-l hover:bg-white"
  >
    <div class="">
      <v-dialog width="500">
        <template v-slot:activator="{ props }">
          <ButtonItem
            class="shrink-1 text-xs py-3"
            size="small"
            v-bind="props"
            @click="onClickAppointment"
            >Wizyta zakończona?</ButtonItem
          >
        </template>

        <template v-slot:default="{ isActive }">
          <v-card title="Zakończ wizytę">
            <v-card-text> Chcesz usunąć wizytę? </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <ButtonItem @click="isActive.value = false" type="tertiary"
                >Anuluj</ButtonItem
              >
              <ButtonItem @click="onClickDeleteAppointment" size="medium"
                >Zakończ wizytę</ButtonItem
              >
            </v-card-actions>
          </v-card>
        </template>
      </v-dialog>
    </div>
    <div class="flex flex-row">
      <div
        class="flex items-center w-[120px] shrink-1 text-sky-800 font-semibold pl-2"
      >
        {{ appointment.appointment_date }}
      </div>
      <div class="flex items-center w-[100px] shrink-1 font-semibold">
        {{ formattedTime }}
      </div>
      <div class="flex items-center w-[160px] shrink-1">
        {{ appointment.name }}
      </div>
      <div
        class="flex items-center w-[130px] shrink-1 font-semibold text-sky-800"
      >
        {{ appointment?.animal?.name }}
      </div>
      <div class="flex items-center w-[250px] shrink-1">
        {{ appointment.description }}
      </div>
      <div class="flex-1 flex flex-row items-start justify-end">
        <div class="rounded flex flex-row items-center justify-center shrink-1">
          <ButtonItem type="tertiary" @click="onClick"
            >Edytuj wizytę</ButtonItem
          >
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
