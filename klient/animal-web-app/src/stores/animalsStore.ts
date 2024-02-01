import { defineStore, storeToRefs } from "pinia";
import { AnimalResponse } from "@/services/animals/animals.model";
import type { Animal } from "@/services/animals/animals.model";
import { ref } from "vue";
import animalsService from "@/services/animals/animalsService";

export const useAnimalsStore = defineStore("animals", () => {
  const animals = ref<Animal[]>([]);
  const selectedAnimal = ref<Animal>();
  const isEditAnimalOpen = ref<boolean>(false);
  const isNewAnimalOpen = ref<boolean>(false);

  async function getAnimals() {
    const response = await animalsService.getAnimals();
    animals.value = response.data;
  }

  async function deleteAnimal(animalId: number) {
    const { data } = await animalsService.deleteAnimal(animalId);
    animals.value = animals.value.filter((animal) => animal.id !== animalId);
  }

  async function editAnimal(animalId: number, updatedAnimal: Animal) {
    const { data } = await animalsService.editAnimal(animalId, updatedAnimal);
  }

  async function postAnimal(animalBody: Animal) {
    const response = await animalsService.postAnimal(animalBody);
    await getAnimals();
  }

  function $reset() {
    animals.value = [];
    isEditAnimalOpen.value = false;
    isNewAnimalOpen.value = false;
  }

  return {
    getAnimals,
    animals,
    selectedAnimal,
    isEditAnimalOpen,
    isNewAnimalOpen,
    deleteAnimal,
    editAnimal,
    postAnimal,
    $reset,
  };
});
