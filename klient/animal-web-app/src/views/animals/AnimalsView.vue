<script setup lang="ts">
import AnimalItem from "@/views/animals/AnimalItem.vue";
import { useAnimalsStore } from "@/stores/animalsStore";
import { storeToRefs } from "pinia";
import EditAnimal from "@/views/animals/EditAnimal.vue";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import NewAnimal from "@/views/animals/NewAnimal.vue";
import { onUnmounted } from "vue";

const animalStore = useAnimalsStore();
animalStore.getAnimals();

const { animals, isEditAnimalOpen, isNewAnimalOpen, selectedAnimal } =
  storeToRefs(animalStore);

onUnmounted(() => animalStore.$reset());
</script>
<template>
  <div class="bg-[#F1F1F1] flex h-screen w-full flex-col p-5 overflow-y-auto">
    <v-expand-x-transition>
      <div
        v-if="isEditAnimalOpen"
        class="absolute top-0 right-0 z-10 w-[500px] h-screen"
      >
        <EditAnimal />
      </div>
    </v-expand-x-transition>
    <v-expand-x-transition>
      <div
        v-if="isNewAnimalOpen"
        class="absolute top-0 right-0 z-10 w-[500px] h-screen"
      >
        <NewAnimal />
      </div>
    </v-expand-x-transition>
    <div class="flex flex-col gap-6 py-6">
      <p class="text-[32px]">Wszystkie zwierzaki</p>
      <ButtonItem class="w-[180px]" @click="isNewAnimalOpen = true"
        >Dodaj zwierzaka</ButtonItem
      >
    </div>

    <div
      v-if="animals && animals.length > 0"
      class="flex flex-row gap-5 flex-wrap"
    >
      <AnimalItem v-for="animal in animals" :animal="animal" :key="animal.id" />
    </div>
    <div
      class="flex justify-center items-center align-center text-[20px] font-base py-4"
      v-else
    >
      Brak zwierzaków. Dodaj nowego zwierzaka.
    </div>
  </div>
</template>
