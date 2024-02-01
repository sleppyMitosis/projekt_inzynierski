import type { AxiosResponse } from "axios";

export interface Animal {
  id?: number;
  name: string;
  species: string;
  chip_number?: string | null;
  pedigree_number?: string | null;
  date_of_birth: string | null;
}

export type AnimalResponse = AxiosResponse<Animal[]>;
