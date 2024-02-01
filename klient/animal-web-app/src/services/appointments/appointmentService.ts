import apiClient from "@/services/apiClient";
import {
  Appointment,
  AppointmentResponse,
  CreateAppointment,
} from "@/services/appointments/appointment.model";
import { AnimalResponse } from "@/services/animals/animals.model";

export default {
  async getAppointments(): Promise<AppointmentResponse> {
    return apiClient.get("/appointments/appointments/");
  },

  async getAnimals(): Promise<AnimalResponse> {
    return apiClient.get("/animal-profiles/animals/");
  },

  async editAppointment(
    appointmentId: number,
    updatedAppointment: CreateAppointment,
  ): Promise<AppointmentResponse> {
    const response = await apiClient.put(
      `/appointments/appointments/${appointmentId}/`,
      { ...updatedAppointment },
    );
    return response.data;
  },

  async deleteAppointment(appointmentId: number): Promise<AppointmentResponse> {
    return await apiClient.delete(
      `/appointments/appointments/${appointmentId}/`,
      {},
    );
  },

  async postAppointment(
    appointmentBody: CreateAppointment,
  ): Promise<AppointmentResponse> {
    const response = await apiClient.post("/appointments/appointments/", {
      ...appointmentBody,
    });
    return response.data;
  },
};
