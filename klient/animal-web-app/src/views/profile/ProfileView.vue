<script setup lang="ts">
import { onMounted } from "vue";
import EditPassword from "@/views/profile/EditUser.vue";
import { useUserStore } from "@/stores/profileStore";
import { storeToRefs } from "pinia";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import EditUser from "@/views/profile/EditUser.vue";
import { useRouter } from "vue-router";

const router = useRouter();
const userStore = useUserStore();
const { isEditPasswordOpen, username, email, phone_number, vet_phone_number } =
  storeToRefs(userStore);

const deleteAccount = async () => {
  await userStore.deleteUser();
  router.push({ name: "loginForm" });
};

onMounted(() => {
  if (!userStore.userIsLoaded) {
    userStore.getUserFromApi();
  }
});
</script>

<template>
  <div class="bg-[#F1F1F1] flex h-full w-full p-10 justify-between">
    <div
      class="p-4 bg-sky-100 border rounded-2xl flex flex-col w-[550px] shadow-xl"
    >
      <p class="text-[32px] text-black font-bold opacity-100">Moje konto</p>
      <div class="text-black mt-4">
        <p class="font-bold text-base py-2">Adres email: {{ email }}</p>
        <p class="font-bold text-base py-2">Login: {{ username }}</p>
        <p class="font-bold text-base py-2">
          Numer telefonu: {{ phone_number }}
        </p>
        <p class="font-bold text-base py-2">
          Numer telefonu do weterynarza: {{ vet_phone_number }}
        </p>
        <div class="flex py-15 gap-20">
          <div
            class="justify-center items-center align-center flex flex-row px-2 gap-3"
          >
            <ButtonItem
              size="medium"
              type="tertiary"
              @click="isEditPasswordOpen = true"
              >Edytuj profil</ButtonItem
            >
            <v-dialog width="500">
              <template v-slot:activator="{ props }">
                <div class="flex">
                  <button
                    class="bg-red-600 rounded-lg font-semibold text-sm py-3 px-4 text-white border-red-600 enabled:hover:bg-red-700 enabled:hover:border-red-700"
                    v-bind="props"
                  >
                    Usuń profil
                  </button>
                </div>
              </template>

              <template v-slot:default="{ isActive }">
                <v-card title="Usuń konto">
                  <v-card-text>
                    Jesteś pewnien, że chcesz usunąć konto?
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <ButtonItem @click="isActive.value = false" type="tertiary"
                      >Anuluj</ButtonItem
                    >
                    <button
                      @click="deleteAccount"
                      class="bg-red-600 rounded-lg font-semibold text-sm py-3 px-4 text-white border-red-600 enabled:hover:bg-red-700 enabled:hover:border-red-700"
                    >
                      Usuń konto
                    </button>
                  </v-card-actions>
                </v-card>
              </template>
            </v-dialog>
          </div>
          <v-expand-x-transition>
            <div
              v-if="isEditPasswordOpen"
              class="absolute top-0 right-0 z-10 w-[500px] h-screen"
            >
              <EditUser />
            </div>
          </v-expand-x-transition>
        </div>
      </div>
    </div>
  </div>
</template>
