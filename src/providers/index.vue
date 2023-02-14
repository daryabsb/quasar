<script setup lang="ts">
import { ref, provide, readonly } from 'vue';
import Fetches from "./Fetches.vue"
import Modals from "./Modals.vue"


const isSearchOpen = ref(false)
const toggleSearch = () => isSearchOpen.value = !isSearchOpen.value

provide("isSearchOpen", readonly(isSearchOpen))
provide("toggleSearch", toggleSearch)

// Refactored
interface Client {
  id: number;
  name: string;
  dob: string;
  gender: string;
  description: string;
  phone: string;
  email: string;
  image: string;
  status: boolean;
}

interface QuickViewOperations {
  open: boolean;
  clientID: number;
  toggleQuickView(info?: Client): void;
}

// QUICK VIEW
const open = ref(false);
const clientID = ref(0);

const toggleQuickView = (id?: number) => {
  if (id) {
    clientID.value = id;
  }
  open.value = !open.value;
}

provide("quickview", {
  open,
  clientID,
  toggleQuickView
});
</script>
<template>
  <Fetches />
  <Modals />
  <slot />
</template>
