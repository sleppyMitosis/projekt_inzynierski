import type { AxiosResponse } from "axios";

export interface ApiSuccessData {
  status: string;
  message: string;
}

export type ApiSuccessResponse = AxiosResponse<ApiSuccessData>;
