<script setup lang="ts">
defineProps<{
  title: string;
  url: string;
}>();
</script>

<template>
  <router-link :to="url" v-slot="{ navigate, isActive }" class="w-full">
    <div
      @click="navigate"
      class="flex items-center py-1 pr-1 pl-2 justify-start gap-1 cursor-pointer"
      :class="isActive ? 'bg-anti-flash-white border-r-4 border-sky-300' : ''"
    >
      <slot></slot>
      <div class="leading-4">{{ title }}</div>
    </div>
  </router-link>
</template>
