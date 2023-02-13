<template>
  <div class="col-gap-10 row-gap-6" :cols="['auto', '1/2']">
    <div>
      <div class="row items-center justify-between p-2">
        <q-btn flat color="grey-6" @click="prevMonth">
          <q-icon name="chevron_left"></q-icon>
        </q-btn>
        <q-header v-if="vuecal" level="2" class="text-grey-9">{{ currentMonth }}</q-header>

        <q-btn flat color="grey-6" @click="nextMonth">
          <q-icon name="chevron_right"></q-icon>
        </q-btn>
      </div>

      <vue-cal ref="vuecal" @cell-click="selectDate($event)" :events="data.results" xsmall :time="false"
        hide-view-selector active-view="month" :selected-date="selectedDate" :disable-views="['years', 'year', 'week']"
        style="max-width: 450px;height: 350px" :hideTitleBar="true">

      </vue-cal>
    </div>

    <div class="mt-12">
      <q-header level="2" class="text-grey-9">Schedule for <time> {{
        moment(selectedDate).format("MMMM DD, YYYY")
      }}</time></q-header>

      <q-list class="mt-4 text-grey-5">
        <q-item v-for="item in appointments" :key="item.id" @click="toggleQuickView(item.client)">
          <q-item-section>
            <q-avatar :src="getClient(item.client).image" size="50px"></q-avatar>
            <q-item-label>
              <q-header level="4" class="text-grey-9">{{ getClient(item.client).name }}</q-header>
              <q-header level="5" class="mt-0.5">
                <time :datetime="moment(item.start).format('HH:mm')">{{ item.start }}</time> - <time
                  :datetime="item.end">{{ item.end }}</time>
              </q-header>
            </q-item-label>
          </q-item-section>
          <q-toolbar>
            <q-btn flat color="grey-6">
              <q-icon name="more_vert"></q-icon>
            </q-btn>
            <div>
              <q-item>
                <q-item-label>
                  <q-btn color="primary" @click="edit">Edit</q-btn>
                </q-item-label>
              </q-item>
              <q-item>
                <q-item-label>
                  <q-btn color="negative" @click="remove">Remove</q-btn>
                </q-item-label>
              </q-item>
            </div>
          </q-toolbar>
        </q-item>
      </q-list>
    </div>
  </div>
</template>
<script setup  lang="ts">
import { ref, onMounted, computed, inject } from "vue"
import { Appointment, Client } from "../../composables/interfaces"
import moment from "moment"

import VueCal from 'vue-cal'

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
const getClient = (id: number) => {
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
@import url("vue-cal/dist/vuecal.css");

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
