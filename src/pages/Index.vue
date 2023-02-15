<template>
  <!--
    This example requires updating your template:

    ```
    <html class="h-full bg-gray-100">
    <body class="h-full">
    ```
  -->
  <q-layout>

    <div class="flex items-center justify-center py-12 ">
      <div class="max-w-7xl mx-auto py-2 pt-1 ">

        <main class="mx-auto">
          <!-- Replace with your content -->
          <div class="flex px-4 py-2 sm:px-0">
            <div class=" rounded-lg border-4 border-dashed border-gray-200 p-4">
              <calendar />
            </div>

          </div>
          <!-- /End replace -->
        </main>
      </div>
    </div>

  </q-layout>
</template>

<script setup>
import { ref, onMounted } from "vue"
// import axios from "axios"
// import config from "../services/CONFIG"
// import { clients, appointments } from "../samples/clients"
import { useUserStore } from "../stores/user"
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from "@headlessui/vue";
// import {clients, appointments} from "@/samples/clients"
import { Bars3Icon, BellIcon, XMarkIcon } from "@heroicons/vue/24/outline";
import Calendar from "../components/Home/Calendar.vue";

// appointments.forEach((appointment) => {
//   setTimeout(async () => {
//     try {
//       const res = await axios.post("http://127.0.0.1:8000/clients/appointments/", appointment, config())
//       console.log(res.data);
//     } catch (error) {
//       console.log(error);
//     }
//   }, 1000)

// })



const user = {
  name: "Tom Cook",
  email: "tom@example.com",
  imageUrl:
    "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
};
const navigation = [
  { name: "Dashboard", href: "#", current: true },
  { name: "Team", href: "#", current: false },
  { name: "Projects", href: "#", current: false },
  { name: "Calendar", href: "#", current: false },
];
const userNavigation = [
  { name: "Your Profile", href: "#" },
  { name: "Settings", href: "#" },
  { name: "Sign out", href: "#" },
];

const eve = ref([

  {
    ready: {
      view: "week",
      startDate: "2018-11-18T21:00:00.000Z",
      endDate: "2018-11-23T20:59:59.000Z",
      events: [
        {
          _eid: "2606_3",
          start: "2018-11-19T07:35:00.000Z",
          startTimeMinutes: 635,
          end: "2018-11-19T08:30:00.000Z",
          endTimeMinutes: 690,
          title: "Doctor appointment",
          content: '<i class="w-icon material-icons">local_hospital</i>',
          background: false,
          allDay: false,
          daysCount: 1,
          class: "health",
          split: 1,
        },
        {
          _eid: "2606_4",
          start: "2018-11-19T15:30:00.000Z",
          startTimeMinutes: 1110,
          end: "2018-11-19T16:15:00.000Z",
          endTimeMinutes: 1155,
          title: "Dentist appointment",
          content: '<i class="w-icon material-icons">local_hospital</i>',
          background: false,
          allDay: false,
          daysCount: 1,
          class: "health",
          split: 2,
        },
        {
          _eid: "2606_5",
          start: "2018-11-20T15:30:00.000Z",
          startTimeMinutes: 1110,
          end: "2018-11-20T17:30:00.000Z",
          endTimeMinutes: 1230,
          title: "Crossfit",
          content: '<i class="w-icon material-icons">fitness_center</i>',
          background: false,
          allDay: false,
          daysCount: 1,
          class: "sport",
          split: 2,
        },
        {
          _eid: "2606_6",
          start: "2018-11-21T08:00:00.000Z",
          startTimeMinutes: 660,
          end: "2018-11-21T10:00:00.000Z",
          endTimeMinutes: 780,
          title: "Brunch with Jane",
          content: '<i class="w-icon material-icons">local_cafe</i>',
          background: false,
          allDay: false,
          daysCount: 1,
          class: "leisure",
          split: 1,
        },
        {
          _eid: "2606_7",
          start: "2018-11-21T16:30:00.000Z",
          startTimeMinutes: 1170,
          end: "2018-11-21T20:00:00.000Z",
          endTimeMinutes: 1380,
          title: "Swimming lesson",
          content: '<i class="w-icon material-icons">pool</i>',
          background: false,
          allDay: false,
          daysCount: 1,
          class: "sport",
          split: 2,
        },
        {
          _eid: "2606_8",
          start: "2018-11-23T09:30:00.000Z",
          startTimeMinutes: 750,
          end: "2018-11-23T10:00:00.000Z",
          endTimeMinutes: 780,
          title: "Macca's with Mark",
          content: '<i class="w-icon material-icons">fastfood</i>',
          background: false,
          allDay: false,
          daysCount: 1,
          class: "leisure",
          split: 2,
        },
        {
          _eid: "2606_9",
          start: "2018-11-23T18:00:00.000Z",
          startTimeMinutes: 1260,
          end: "2018-11-23T20:30:00.000Z",
          endTimeMinutes: 1410,
          title: "Movie time",
          content: '<i class="w-icon material-icons">local_play</i>',
          background: false,
          allDay: false,
          daysCount: 1,
          class: "leisure",
          split: 1,
        }
      ],
      week: 47,
    }
  }]

);
</script>
