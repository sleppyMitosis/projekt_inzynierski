<script setup lang="ts">
import { useUserStore } from "@/stores/profileStore";
import { storeToRefs } from "pinia";
import { onMounted } from "vue";
import { useRouter } from "vue-router";

const userStore = useUserStore();
const {
  isEditPasswordOpen,
  username,
  email,
  first_name,
  last_name,
  phone_number,
  vet_phone_number,
} = storeToRefs(userStore);

const router = useRouter();

onMounted(() => {
  if (!userStore.userIsLoaded) {
    userStore.getUserFromApi();
  }
});

const navigate = (path: string) => {
  router.push(path);
};
</script>

<template>
  <div class="bg-[#F1F1F1] flex h-screen w-full flex-col p-5 overflow-y-auto">
    <div class="flex flex-col gap-6 py-6">
      <p class="text-[32px]">Witaj {{ username }}</p>
    </div>
    <div class="flex flex-row flex-wrap gap-5">
      <div
        class="p-4 bg-sky-100 border rounded-2xl flex flex-col w-[250px] h-[250px] shadow-xl hover:scale-105 hover:bg-sky-200"
        @click="navigate('/calendar')"
      >
        <div class="flex flex-col justify-center items-center flex-grow">
          <font-awesome-icon
            :icon="['fas', 'calendar-days']"
            size="2xl"
            style="color: #000000"
          />
          <p class="font-semibold text-[22px] pt-4">Wizyty</p>
        </div>
      </div>
      <div
        @click="navigate('/first-aid')"
        class="p-4 bg-sky-100 border rounded-2xl flex flex-col w-[250px] h-[250px] shadow-xl hover:scale-105 hover:bg-sky-200"
      >
        <div class="flex flex-col justify-center items-center flex-grow">
          <font-awesome-icon
            :icon="['fas', 'hand-holding-heart']"
            size="2xl"
            style="color: #000000"
          />
          <p class="font-semibold text-[22px] pt-4">Pierwsza pomoc</p>
        </div>
      </div>
      <div
        @click="navigate('/drugs')"
        class="p-4 bg-sky-100 border rounded-2xl flex flex-col w-[250px] h-[250px] shadow-xl hover:scale-105 hover:bg-sky-200"
      >
        <div class="flex flex-col justify-center items-center flex-grow">
          <font-awesome-icon
            :icon="['fas', 'prescription-bottle-medical']"
            size="2xl"
            style="color: #000000"
          />
          <p class="font-semibold text-[22px] pt-4">Leki</p>
        </div>
      </div>
      <div
        @click="navigate('/animals')"
        class="p-4 bg-sky-100 border rounded-2xl flex flex-col w-[250px] h-[250px] shadow-xl hover:scale-105 hover:bg-sky-200"
      >
        <div class="flex flex-col justify-center items-center flex-grow">
          <font-awesome-icon
            :icon="['fas', 'paw']"
            size="2xl"
            style="color: #000000"
          />
          <p class="font-semibold text-[22px] pt-4">Zwierzaki</p>
        </div>
      </div>
      <div
        @click="navigate('/profile')"
        class="p-4 bg-sky-100 border rounded-2xl flex flex-col w-[250px] h-[250px] shadow-xl hover:scale-105 hover:bg-sky-200"
      >
        <div class="flex flex-col justify-center items-center flex-grow">
          <font-awesome-icon
            :icon="['fas', 'user']"
            size="2xl"
            style="color: #000000"
          />
          <p class="font-semibold text-[22px] pt-4">Profil</p>
        </div>
      </div>
    </div>
  </div>
</template>
