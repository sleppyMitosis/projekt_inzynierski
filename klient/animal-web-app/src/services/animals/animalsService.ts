import apiClient from "@/services/apiClient";
import { Animal, AnimalResponse } from "@/services/animals/animals.model";

export default {
  async getAnimals(): Promise<AnimalResponse> {
    return apiClient.get("/animal-profiles/animals/");
  },

  async postAnimal(animalBody: Animal): Promise<AnimalResponse> {
    const response = await apiClient.post("/animal-profiles/animals/", {
      ...animalBody,
    });
    return response.data;
  },

  async deleteAnimal(animalId: number): Promise<AnimalResponse> {
    return await apiClient.delete(`/animal-profiles/animals/${animalId}/`, {});
  },

  async editAnimal(
    animalId: number,
    updatedAnimal: Animal,
  ): Promise<AnimalResponse> {
    const response = await apiClient.put(
      `/animal-profiles/animals/${animalId}/`,
      {
        ...updatedAnimal,
      },
    );
    return response.data;
  },
};
