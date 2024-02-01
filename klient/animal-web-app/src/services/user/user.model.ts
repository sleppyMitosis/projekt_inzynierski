import type { AxiosResponse } from "axios";

export interface UserData {
  id: number;
  username: string;
  email: string;
  phone_number: string;
  vet_phone_number: string;
}

export interface UserEditData {
  email: string;
  phone_number: string;
  vet_phone_number: string;
}

export interface UserRegistrationData {
  username: string;
  password: string;
  email: string;
  phone_number: string;
  vet_phone_number: string;
}

export interface PasswordResetBody {
  email: string;
  username?: string;
}

export interface EditPasswordBody {
  uid: string;
  token: string;
  password: string;
}

export type UserResponse = AxiosResponse<UserData>;
