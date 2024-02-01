<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import EditPassword from "@/views/profile/EditUser.vue";
import { Animal } from "@/services/animals/animals.model";
import { useAnimalsStore } from "@/stores/animalsStore";
import { storeToRefs } from "pinia";

const props = defineProps<{ animal: Animal }>();
const animalStore = useAnimalsStore();

const { animals, isEditAnimalOpen, isNewAnimalOpen, selectedAnimal } =
  storeToRefs(animalStore);

const onClick = () => {
  isEditAnimalOpen.value = true;
  selectedAnimal.value = props.animal;
};
</script>

<template>
  <div
    class="p-4 bg-sky-100 border rounded-2xl flex flex-col w-[400px] shadow-xl"
  >
    <div class="text-black mt-4">
      <p class="font-bold text-base py-2">Imię: {{ animal.name }}</p>
      <p class="font-bold text-base py-2">Gatunek: {{ animal.species }}</p>
      <p class="font-bold text-base py-2">
        Data urodzenia: {{ animal.date_of_birth }}
      </p>
      <p class="font-bold text-base py-2">
        Numer chipa: {{ animal.chip_number }}
      </p>
      <p class="font-bold text-base py-2">
        Numer rodowodu: {{ animal.pedigree_number }}
      </p>
      <p class="font-bold text-base py-2"></p>
      <div class="flex flex-row py-10">
        <div class="justify-center items-center align-center"></div>
      </div>
      <div class="flex justify-center align-baseline items-center">
        <ButtonItem type="tertiary" @on-click="onClick"
          >Edytuj zwierzaka</ButtonItem
        >
      </div>
    </div>
  </div>
</template>

<style scoped></style>
