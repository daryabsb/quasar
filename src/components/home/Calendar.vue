<template>


  <div class="md:grid md:grid-cols-2 md:divide-x md:divide-gray-200">
    <div class="md:pr-14">
      <div class="flex items-center px-2 py-4">
        <h2 v-if="vuecal" class="flex-auto text-2xl font-semibold text-gray-900">{{ currentMonth }}</h2>
        <button type="button"
          class="-my-1.5 flex flex-none items-center justify-center p-1.5 text-gray-400 hover:text-gray-500"
          @click="prevMonth">
          <!-- @click="vuecal.previous()"> -->
          <span class="sr-only">Previous month</span>
          <ChevronLeftIcon class="h-5 w-5" aria-hidden="true" />
        </button>
        <button type="button"
          class="-my-1.5 -mr-1.5 ml-2 flex flex-none items-center justify-center p-1.5 text-gray-400 hover:text-gray-500"
          @click="nextMonth">
          <span class="sr-only">Next month</span>
          <ChevronRightIcon class="h-5 w-5" aria-hidden="true" />
        </button>
      </div>
      <vue-cal ref="vuecal" @cell-click="selectDate($event)" :events="data.results" xsmall :time="false"
        hide-view-selector active-view="month" :selected-date="selectedDate" :disable-views="['years', 'year', 'week']"
        style="max-width: 450px;height: 350px" :hideTitleBar="true">

      </vue-cal>
    </div>
    <section class="mt-12 md:mt-0 md:pl-14 ">
      <h1 class=" font-semibold text-3xl text-gray-900 pb-2">Schedule for <time> {{
        moment(selectedDate).format("MMMM DD, YYYY")
      }}</time>
      </h1>
      <q-separator></q-separator>
      <ol class="mt-4 space-y-1 text-sm leading-6  text-gray-500">
        <li v-for="item in appointments" :key="item.id"
          class="group relative flex items-center space-x-4 rounded-xl py-2 px-4 focus-within:bg-gray-100 hover:bg-gray-100"
          @click="toggleQuickView(item.client)">
          <img :src="getClient(item.client).image" alt=""
            class="h-10 w-10 flex-none transition-all object-cover hover:scale-150 rounded-full" />
          <div class="flex-auto">
            <Suspense>
              <p class="text-gray-900">{{ getClient(item.client).name }}</p>
              <template #fallback>
                Comming...
              </template>
            </Suspense>
            <p class="mt-0.5">
              <time :datetime="moment(item.start).format('HH:mm')">{{ item.start }}</time> -
              <time :datetime="item.end">{{ item.end }}</time>
            </p>
          </div>
          <Menu as="div" class="relative opacity-0 focus-within:opacity-100 group-hover:opacity-100">
            <div>
              <MenuButton class="-m-2 flex items-center rounded-full p-1.5 text-gray-500 hover:text-gray-600">
                <span class="sr-only">Open options</span>
                <EllipsisVerticalIcon class="h-6 w-6" aria-hidden="true" />
              </MenuButton>
            </div>
            <transition enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95">
              <MenuItems
                class="absolute right-0 z-10 mt-2 w-36 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <div class="py-1">
                  <MenuItem v-slot="{ active }">
                  <a href="#"
                    :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">Edit</a>
                  </MenuItem>
                  <MenuItem v-slot="{ active }">
                  <a href="#"
                    :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']">Cancel</a>
                  </MenuItem>
                </div>
              </MenuItems>
            </transition>
          </Menu>
        </li>
      </ol>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, inject } from "vue"
import { Appointment, Client } from "../../composables/interfaces"
import moment from "moment"
import { ChevronLeftIcon, ChevronRightIcon } from '@heroicons/vue/20/solid'
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { EllipsisVerticalIcon } from '@heroicons/vue/24/outline'
import useFetchData from '../../composables/useFetchData'
import { useClientStore } from "../../stores/client"

const store = useClientStore()
const { open, toggleQuickView } = inject("quickview")
const currentMonth = ref('')
const month = computed({
  get: () => currentMonth.value,
  set: (value) => currentMonth.value = value
});

const title = ref('')
const vuecal = ref(null)
const selectedDate = ref(new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate()))
const selectDate = (e) => {
  selectedDate.value = new Date(new Date(e).getFullYear(), new Date(e).getMonth(), new Date(e).getDate())
};

const today = ref(new Date())
const { data, error } = useFetchData(month)

onMounted(() => {
  today.value = new Date(selectedDate.value)
  currentMonth.value = moment(new Date).format("MMMM YYYY");
})



const appointments = computed(() => {
  const todayDate = selectedDate.value.getDate();
  const todayMonth = selectedDate.value.getMonth();
  return data.value.results.filter((item: Appointment) => {
    const itemDate = new Date(item.date).getDate();
    const itemStart = new Date(item.start).getDate();
    const itemMonth = new Date(item.start).getMonth();
    return itemDate === todayDate && itemMonth === todayMonth || itemStart === todayDate && itemMonth === todayMonth;
  })
})
const getClient = (id) => {
  return store.useClients.find((client: Client) => client.id === id)
}
const prevMonth = () => {
  vuecal.value.previous();
  currentMonth.value = vuecal.value.viewTitle;
};

const nextMonth = () => {
  vuecal.value.next();
  currentMonth.value = vuecal.value.viewTitle;
};
</script>

<style>
.vuecal__cell--selected {
  background-color: #ca1c90;
  color: beige;
  z-index: 2;
}

.vuecal__cell-events-count {
  position: absolute;
  left: 20%;
  top: 0%;
  transform: translate(-50%);
  min-width: 22px;
  height: 22px;
  line-height: 12px;
  padding: 0 3px;
  background: #999;
  color: #fff;
  border-radius: 12px;
  font-size: 10px;
  box-sizing: border-box;
}
</style>