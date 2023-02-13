<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          Dashboard
        </q-toolbar-title>
        <q-menu>
          <q-btn flat dense round icon="menu" aria-label="Open navigation menu"></q-btn>
          <q-list dense class="bg-white">
            <q-item v-for="item in navigation" :key="item.name" :class="{ 'text-indigo-500': item.current }"
              @click="goToPage(item.href)">
              {{ item.name }}
            </q-item>
          </q-list>
        </q-menu>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <div class="flex justify-center">
        <calendar />
      </div>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useUserStore } from "../stores/user"
import Calendar from "../components/Home/Calendar.vue";


const navigation = [
  { name: "Dashboard", href: "#", current: true },
  { name: "Team", href: "#", current: false },
  { name: "Projects", href: "#", current: false },
  { name: "Calendar", href: "#", current: false },
];

</script>



