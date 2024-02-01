import type { AxiosResponse } from "axios";

export interface SelectOption<T> {
  value: T;
  label: string;
}

export interface ErrorResponse {
  data: {
    name: string;
  };
}
