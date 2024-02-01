<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useDrugsStore } from "@/stores/drugsStore";

const props = defineProps({
  index: Number,
  drugId: Number,
});
const emits = defineEmits(["update:taken"]);

const drugsStore = useDrugsStore();
const isTaken = ref(false);

const loadTakenState = async () => {
  if (typeof props.drugId === "number" && typeof props.index === "number") {
    const drug = await drugsStore.getDrugById(props.drugId);
    if (drug && Array.isArray(drug.dosage_states)) {
      isTaken.value = drug.dosage_states[props.index] || false;
    }
  }
};

const toggleTaken = async () => {
  if (typeof props.drugId === "number" && typeof props.index === "number") {
    isTaken.value = !isTaken.value;
    await drugsStore.updateDosageState(
      props.drugId,
      props.index,
      isTaken.value,
    );
    emits("update:taken", { index: props.index, taken: isTaken.value });
  }
};

onMounted(loadTakenState);
</script>

<template>
  <div
    class="w-5 h-5 border border-sky-700 flex justify-center items-center cursor-pointer rounded transition-all duration-300"
    :class="{ 'bg-green-500 border-green-700': isTaken, 'bg-white': !isTaken }"
    @click="toggleTaken"
  >
    <span v-if="isTaken" class="text-white font-bold">✔</span>
  </div>
</template>
