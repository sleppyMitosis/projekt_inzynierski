<template>
  <button
    class="rounded-lg font-semibold text-sm disabled:bg-silver disabled:text-white"
    :class="{
      'py-3.5 px-6 text-base': size === 'big',
      'py-3 px-4': size === 'medium',
      'p-2': size === 'small',
      'border-sky-500 bg-sky-500 text-white enabled:hover:bg-sky-600 enabled:hover:border-sky-600':
        type === 'primary',
      'border-sky-500 border-solid border-[2px] text-sky-500 enabled:hover:text-sky-600 enabled:hover:border-sky-600':
        type === 'secondary',
      'text-sky-600 [text-decoration:underline] enabled:hover:text-sky-700':
        type === 'tertiary',
    }"
    :disabled="disabled"
    @click.stop.prevent="handleClick"
  >
    <slot />
  </button>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { type PropType } from "vue";

export default defineComponent({
  emits: {
    onClick: () => true,
  },
  props: {
    disabled: { type: Boolean, default: false },
    type: {
      type: String as PropType<"primary" | "secondary" | "tertiary">,
      default: "primary",
    },
    size: {
      type: String as PropType<"big" | "medium" | "small">,
      default: "big",
    },
    //animation: { type: Boolean, default: true },
  },
  methods: {
    handleClick() {
      this.$emit("onClick");
    },
  },
});
</script>
