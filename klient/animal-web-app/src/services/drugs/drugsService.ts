import apiClient from "@/services/apiClient";
import {
  Medication,
  DrugsResponse,
  CreateMedication,
} from "@/services/drugs/drugs.model";
import { AnimalResponse } from "@/services/animals/animals.model";

export default {
  async getDrugs(): Promise<DrugsResponse> {
    return apiClient.get("medications/medications/");
  },

  async getAnimals(): Promise<AnimalResponse> {
    return apiClient.get("/animal-profiles/animals/");
  },

  async editDrug(
    drugId: number,
    updatedDrug: CreateMedication,
  ): Promise<DrugsResponse> {
    const response = await apiClient.put(
      `/medications/medications/${drugId}/`,
      {
        ...updatedDrug,
      },
    );
    return response.data;
  },

  async deleteDrug(drugId: number): Promise<DrugsResponse> {
    return await apiClient.delete(`/medications/medications/${drugId}/`, {});
  },

  async postDrug(drugBody: CreateMedication): Promise<DrugsResponse> {
    const response = await apiClient.post("/medications/medications/", {
      ...drugBody,
    });
    return response.data;
  },

  async getDrugById(drugId: number): Promise<Medication> {
    const response = await apiClient.get(`/medications/medications/${drugId}/`);
    return response.data;
  },
};
