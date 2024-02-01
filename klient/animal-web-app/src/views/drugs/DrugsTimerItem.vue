<script setup lang="ts">
import { onMounted, ref, watch, computed } from "vue";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { Medication } from "@/services/drugs/drugs.model";
import { useDrugsStore } from "@/stores/drugsStore";
import DosageVisualization from "@/views/drugs/DosageVisualization.vue";
import { storeToRefs } from "pinia";

const props = defineProps<{ drug: Medication }>();
const drugsStore = useDrugsStore();
const { selectedDrug, isEditDrugOpen, drugs } = storeToRefs(drugsStore);

const takenDosages = ref<boolean[]>([]);

const validatedDosageCount = computed(() => {
  return props.drug.dosage_count >= 0 ? props.drug.dosage_count : 0;
});

onMounted(async () => {
  try {
    const response = await drugsStore.getDrugById(props.drug.id);
    takenDosages.value =
      response.dosage_states || Array(validatedDosageCount.value).fill(false);
  } catch (error) {
    console.error("Error fetching dosage states:", error);
  }
});

watch(
  () => props.drug.dosage_states,
  (newStates) => {
    takenDosages.value =
      newStates || Array(validatedDosageCount.value).fill(false);
  },
  { deep: true },
);

const onClick = () => {
  isEditDrugOpen.value = true;
  selectedDrug.value = props.drug;
};

const handleDosageUpdate = async ({
  index,
  taken,
}: {
  index: number;
  taken: boolean;
}) => {
  takenDosages.value[index] = taken;

  while (takenDosages.value.length < props.drug.dosage_count) {
    takenDosages.value.push(false);
  }

  const updatedDrug = { ...props.drug, dosage_states: takenDosages.value };
};
</script>

<template>
  <div
    class="p-4 bg-sky-100 border rounded-2xl flex flex-col w-[400px] shadow-xl"
  >
    <div class="text-black mt-4 flex flex-col justify-center items-center">
      <div class="flex flex-row">
        <p class="font-bold text-semibold pt-2.5 text-center px-2">Lek:</p>
        <p class="font-bold text-lg py-2 text-sky-900 py-2 text-center">
          {{ drug?.name }}
        </p>
      </div>
      <div class="flex flex-row">
        <p class="font-bold text-semibold pt-2.5 text-center px-2">Zwierzę:</p>
        <p class="font-bold text-lg py-2 text-sky-900 py-2 text-center">
          {{ drug?.animal?.name }}
        </p>
      </div>
      <div class="flex flex-row">
        <p class="font-bold text-semibold pt-2.5 text-center px-2">
          Liczba dawek:
        </p>
        <p class="font-bold text-lg py-2 text-sky-900 py-2 text-center">
          {{ drug?.dosage_count }}
        </p>
      </div>
      <p class="font-bold text-base py-2">
        Lek powinien być podawany w dniach:
      </p>
      <p class="font-bold text-lg py-2 text-sky-900">
        {{ drug.start_date }} - {{ drug.end_date }}
      </p>
      <p class="font-bold text-base py-2"></p>
      <div class="flex flex-row py-5">
        <div class="justify-center items-center align-center">
          <div class="flex flex-wrap gap-1">
            <div class="flex gap-1 flex-wrap">
              <DosageVisualization
                v-for="index in props.drug.dosage_count"
                :key="index"
                :drugId="drug.id"
                :index="index"
                :isTaken="takenDosages[index]"
                @update:taken="handleDosageUpdate"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="flex justify-center align-baseline items-center">
        <ButtonItem type="tertiary" @click="onClick">Edytuj lek</ButtonItem>
      </div>
    </div>
  </div>
</template>
