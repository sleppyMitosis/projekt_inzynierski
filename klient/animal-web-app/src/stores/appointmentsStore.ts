import { ref } from "vue";
import { defineStore, storeToRefs } from "pinia";
import type { Appointment } from "@/services/appointments/appointment.model";
import { type CreateAppointment } from "@/services/appointments/appointment.model";
import appointmentService from "@/services/appointments/appointmentService";
import drugsService from "@/services/drugs/drugsService";
import { SelectOption } from "@/models/common.model";
import animalsService from "@/services/animals/animalsService";

export const useAppointmentStore = defineStore("appointment", () => {
  const appointments = ref<Appointment[]>([]);
  const selectedAppointment = ref<Appointment>();
  const isNewAppointmentOpen = ref<boolean>(false);
  const isEditAppoitmentOpen = ref<boolean>(false);
  const animalOptions = ref<SelectOption<number>[]>([]);

  async function getAppointments() {
    const response = await appointmentService.getAppointments();
    appointments.value = response.data;
  }

  async function postAppointment(appointmentBody: CreateAppointment) {
    const response = await appointmentService.postAppointment(appointmentBody);
    await getAppointments();
  }

  const getAnimals = async () => {
    const options = await drugsService.getAnimals();
    animalOptions.value = options.data.map((option) => ({
      label: `${option.name}`,
      value: option.id as number,
    }));
  };

  async function editAppointment(
    appointmentId: number,
    updatedAppointment: CreateAppointment,
  ) {
    const { data } = await appointmentService.editAppointment(
      appointmentId,
      updatedAppointment,
    );
  }

  async function deleteAppointment(appointmentId: number) {
    const { data } = await appointmentService.deleteAppointment(appointmentId);
    appointments.value = appointments.value.filter(
      (appointment) => appointment.id !== appointmentId,
    );
  }

  return {
    deleteAppointment,
    getAppointments,
    editAppointment,
    getAnimals,
    postAppointment,
    appointments,
    selectedAppointment,
    isEditAppoitmentOpen,
    isNewAppointmentOpen,
    animalOptions,
  };
});
