import type { AxiosResponse } from "axios";

export interface LoginBody {
  username: string;
  password: string;
}

export interface LoginResponseData {
  username: string;
  success: boolean;
}

export type LoginResponse = AxiosResponse<LoginResponseData>;
