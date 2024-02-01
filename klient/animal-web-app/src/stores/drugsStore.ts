import { defineStore, storeToRefs } from "pinia";
import { ref } from "vue";
import {
  CreateMedication,
  type Medication,
} from "@/services/drugs/drugs.model";
import drugsService from "@/services/drugs/drugsService";
import type { SelectOption } from "@/models/common.model";

export const useDrugsStore = defineStore("drugs", () => {
  const drugs = ref<Medication[]>([]);
  const selectedDrug = ref<Medication>();
  const isNewDrugOpen = ref<boolean>(false);
  const isEditDrugOpen = ref<boolean>(false);
  const animalOptions = ref<SelectOption<number>[]>([]);

  async function getDrugs() {
    const response = await drugsService.getDrugs();
    drugs.value = response.data;
  }

  const getAnimals = async () => {
    const options = await drugsService.getAnimals();
    animalOptions.value = options.data.map((option) => ({
      label: `${option.name}`,
      value: option.id as number,
    }));
  };

  async function postDrug(drugBody: CreateMedication) {
    const response = await drugsService.postDrug(drugBody);
    await getDrugs();
  }

  async function deleteDrug(drugId: number) {
    const { data } = await drugsService.deleteDrug(drugId);
    drugs.value = drugs.value.filter((drug) => drug.id !== drugId);
  }

  async function editDrug(drugId: number, updatedDrug: CreateMedication) {
    await drugsService.editDrug(drugId, updatedDrug);
    await getDrugs();
  }

  async function decrementDrugDosage(drugId: number) {
    const drugToDecrement = drugs.value.find((drug) => drug.id === drugId);
    if (drugToDecrement && drugToDecrement.dosage_count > 0) {
      const updatedDrug = {
        ...drugToDecrement,
        dosage_count: drugToDecrement.dosage_count - 1,
      };
      await editDrug(drugId, updatedDrug);
      await getDrugs();
    }
  }

  async function updateDosageState(
    drugId: number,
    index: number,
    taken: boolean,
  ) {
    const drug = drugs.value.find((d) => d.id === drugId);
    if (drug) {
      const updatedStates = [...(drug.dosage_states || [])];
      updatedStates[index] = taken;
      await editDrug(drugId, { ...drug, dosage_states: updatedStates });
    }
  }

  async function getDrugById(drugId: number): Promise<Medication> {
    const response = await drugsService.getDrugById(drugId);
    return response;
  }

  return {
    postDrug,
    getDrugs,
    getAnimals,
    editDrug,
    deleteDrug,
    decrementDrugDosage,
    getDrugById,
    updateDosageState,
    drugs,
    selectedDrug,
    isNewDrugOpen,
    animalOptions,
    isEditDrugOpen,
  };
});
