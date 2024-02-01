import type { AxiosResponse } from "axios";
import { Animal } from "@/services/animals/animals.model";

export interface Appointment {
  id?: number;
  name: string;
  animal?: Animal | null;
  description?: string;
  appointment_date: string;
  appointment_time: string;
}

export interface CreateAppointment {
  id?: number;
  name: string;
  animal_id: number | undefined;
  description?: string;
  appointment_date: string;
  appointment_time: string;
}

export type AppointmentResponse = AxiosResponse<Appointment[]>;
