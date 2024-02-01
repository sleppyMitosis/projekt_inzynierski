<template>
  <div class="h-screen flex">
    <div class="flex flex-col justify-start gap-2 text-sm">
      <div class="flex flex-row flex-1"></div>
    </div>
    <div class="flex flex-col flex-1 overflow-auto">
      <div class="flex flex-1 overflow-auto">
        <div class="flex">
          <router-view name="sideMenu" />
        </div>
        <router-view name="main" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SideMenu from "@/components/side-menu/SideMenu.vue";
</script>
