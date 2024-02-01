<script setup lang="ts">
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { useDrugsStore } from "@/stores/drugsStore";
import DrugsTimerItem from "@/views/drugs/DrugsTimerItem.vue";
import { storeToRefs } from "pinia";
import NewDrug from "@/views/drugs/NewDrug.vue";
import EditDrug from "@/views/drugs/EditDrug.vue";

const drugsStore = useDrugsStore();
drugsStore.getDrugs();

const { drugs, selectedDrug, isNewDrugOpen, isEditDrugOpen } =
  storeToRefs(drugsStore);
</script>

<template>
  <div class="bg-[#F1F1F1] flex h-full w-full flex-col p-5">
    <div class="flex flex-col gap-6 py-6">
      <p class="text-[32px]">Wszystkie leki</p>
      <ButtonItem class="w-[180px]" @click="isNewDrugOpen = true"
        >Dodaj lek dla zwierzaka</ButtonItem
      >
      <v-expand-x-transition>
        <div
          v-if="isNewDrugOpen"
          class="absolute top-0 right-0 z-10 w-[500px] h-screen"
        >
          <NewDrug />
        </div>
      </v-expand-x-transition>
      <v-expand-x-transition>
        <div
          v-if="isEditDrugOpen"
          class="absolute top-0 right-0 z-10 w-[500px] h-screen"
        >
          <EditDrug />
        </div>
      </v-expand-x-transition>
    </div>
    <div v-if="drugs && drugs.length > 0" class="flex flex-row gap-5">
      <DrugsTimerItem v-for="drug in drugs" :drug="drug" :key="drug.id" />
    </div>
    <div
      class="flex justify-center items-center align-center text-[20px] font-base py-4"
      v-else
    >
      Brak śledzonych dawek leków. Dodaj nowy lek.
    </div>
  </div>
</template>
