<template>
  <div
    class="bg-white min-w-[180px] w-full h-screen flex flex-col items-center justify-start gap-2 text-left text-sm text-black border border-r"
  >
    <div class="h-[88px] w-full flex items-start justify-end"></div>
    <SideMenuElement title="Widok Główny" url="/dashboard">
      <font-awesome-icon :icon="['fas', 'house']" style="color: #000000" />
    </SideMenuElement>
    <SideMenuElement title="Wizyty" url="/calendar">
      <font-awesome-icon
        :icon="['fas', 'calendar-days']"
        style="color: #000000"
      />
    </SideMenuElement>
    <SideMenuElement title="Pierwsza pomoc" url="/first-aid">
      <font-awesome-icon
        :icon="['fas', 'hand-holding-heart']"
        style="color: #000000"
      />
    </SideMenuElement>
    <SideMenuElement title="Leki" url="/drugs">
      <font-awesome-icon
        :icon="['fas', 'prescription-bottle-medical']"
        style="color: #000000"
      />
    </SideMenuElement>
    <SideMenuElement title="Zwierzaki" url="/animals">
      <font-awesome-icon :icon="['fas', 'paw']" style="color: #000000"
    /></SideMenuElement>
    <SideMenuElement title="Profil" url="/profile">
      <font-awesome-icon :icon="['fas', 'user']" style="color: #000000"
    /></SideMenuElement>
    <div class="absolute bottom-5 p-4 z-10">
      <ButtonItem @click="logout">Wyloguj</ButtonItem>
    </div>
  </div>
</template>

<script setup lang="ts">
import SideMenuElement from "./SideMenuElement.vue";
import ButtonItem from "@/components/button-item/ButtonItem.vue";
import { Route } from "@/router/route";
import authService from "@/services/auth/authService";
import { useRouter } from "vue-router";

const router = useRouter();

const logout = async () => {
  await authService.logout();
};
</script>
