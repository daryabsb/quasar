<template>
  <!--
    This example requires updating your template:

    ```
    <html class="h-full bg-gray-100">
    <body class="h-full">
    ```
  -->
  <div class="min-h-full bg-zinc-100 pt-6">
    <Breadcrumbs :breadcrumbs="[
      { name: 'Clients', route: '/clients' },
      { name: client && client.name ? client.name : '', route: '#' }
    ]" />

    <main v-if="client && details" class="py-4">
      <!-- Page header -->

      <div class=" max-w-7xl mx-auto overflow-hidden rounded-lg bg-white shadow">
        <h2 class="sr-only" id="profile-overview-title">Profile Overview</h2>
        <div class="bg-white pr-6">
          <div class="sm:flex sm:items-center sm:justify-between">
            <q-card flat>


              <q-card-section horizontal>
                <img class="col w-40 aspect-1 object-cover object-center" :src="client.image" />

                <q-card-section class=" overflow-hidden">
                  <div class="text-xl font-bold text-gray-900 sm:text-2xl mb-2">{{ client.name }}</div>
                  <q-item-label caption>Age: <span class="capitalize font-semibold text-zinc-900">{{
                    client.age
                  }}</span></q-item-label>
                  <q-item-label caption>Sex: <span class="capitalize font-semibold text-zinc-900">{{
                    client.gender
                  }}</span>
                  </q-item-label>
                  <q-item-label caption>Height: <span class="capitalize font-semibold text-zinc-900">{{
                    status.height
                  }}</span>
                  </q-item-label>
                  <q-item-label caption>Weight: <span class="capitalize font-semibold text-zinc-900">{{
                    status.weight
                  }}</span>
                  </q-item-label>
                </q-card-section>
                <q-card-actions vertical dense class="justify-around">
                  <!-- <q-btn flat round color="red" icon="favorite" />
                    <q-btn flat round color="accent" icon="bookmark" />
                    <q-btn flat round color="primary" icon="share" /> -->
                  <q-list>
                    <q-item dense clickable>
                      <q-item-section avatar>
                        <q-icon color="red" name="favorite" />
                      </q-item-section>
                      <q-item-section>
                        <q-item-label>Heart: <q-item-label caption class="text-green-600">{{
                          status.heart_condition
                        }}</q-item-label></q-item-label>
                      </q-item-section>
                    </q-item>
                    <q-item dense clickable>
                      <q-item-section avatar>
                        <q-icon color="primary" name="bookmark" />
                      </q-item-section>
                      <q-item-section>
                        <q-item-label>Bar XYZ: <q-item-label caption>30%</q-item-label></q-item-label>
                      </q-item-section>
                    </q-item>
                    <q-item dense clickable>
                      <q-item-section avatar>
                        <q-icon color="green" name="share" />
                      </q-item-section>
                      <q-item-section>
                        <q-item-label>Bar XYZ: <q-item-label caption>30%</q-item-label></q-item-label>
                      </q-item-section>
                    </q-item>
                  </q-list>
                </q-card-actions>
                <q-card-actions vertical dense class="justify-around">
                  <!-- <q-btn flat round color="red" icon="favorite" />
                    <q-btn flat round color="accent" icon="bookmark" />
                    <q-btn flat round color="primary" icon="share" /> -->
                  <q-list>
                    <q-item dense clickable>
                      <q-item-section avatar>
                        <q-icon color="red" name="favorite" />
                      </q-item-section>
                      <q-item-section>
                        <q-item-label>Heart: <q-item-label caption class="text-green-600">{{
                          status.heart_condition
                        }}</q-item-label></q-item-label>
                      </q-item-section>
                    </q-item>
                    <q-item dense clickable>
                      <q-item-section avatar>
                        <q-icon color="primary" name="bookmark" />
                      </q-item-section>
                      <q-item-section>
                        <q-item-label>Bar XYZ: <q-item-label caption>30%</q-item-label></q-item-label>
                      </q-item-section>
                    </q-item>
                    <q-item dense clickable>
                      <q-item-section avatar>
                        <q-icon color="green" name="share" />
                      </q-item-section>
                      <q-item-section>
                        <q-item-label>Bar XYZ: <q-item-label caption>30%</q-item-label></q-item-label>
                      </q-item-section>
                    </q-item>
                  </q-list>
                </q-card-actions>
              </q-card-section>
            </q-card>
            <q-separator spaced vertical />

            <div class="sm:flex sm:space-x-5">

              <!-- <div class="flex-shrink-0">
                                <img class="mx-auto h-24 w-24 rounded-full object-cover object-top" :src="client.image"
                                    alt="" />
                            </div> -->
              <!--
                                {
    "id": 1,
    "heart_condition": "good",
    "blood_sugar": 105,
    "blood_pressure": "14/8",
    "weight": 78.0,
    "height": 176.0,
    "smoking_status": false,
    "alcohol_consumption": true,
    "physical_activity": "None",
    "notes": "He is cute, smiles most of the time, gorgous",
    "client": 129
}
                             -->
              <div class="mt-6 text-center sm:mt-0 sm:pt-1 sm:text-left sm:py-6">
                <p class="text-xl font-bold text-gray-900 sm:text-2xl">{{ client.name }}</p>
                <p class="text-sm font-medium text-gray-600">{{
                  client.age + ' ' + client.gender
                }} Weight: {{ status.weight }} Height:
                  {{ status.height }}
                </p>
                <p class="text-md mt-2 font-medium text-gray-600">
                  <span :class="[
                    status.heart_condition === 'good'
                      ? 'text-green-600'
                      : 'text-red-600'
                  ]">Heart: {{ status.heart_condition }}</span>
                  {{ ' | ' }}
                  <span :class="[
                    status.blood_sugar >= 105
                      ? 'text-green-600'
                      : 'text-red-600'
                  ]">Blood sugar: {{ status.blood_sugar }}</span>
                  {{ ' | ' }}
                  <span>Blood pressure: {{ status.blood_pressure }}</span>
                  {{ ' | ' }}
                  <span :class="[
                    status.blood_sugar >= 105
                      ? 'text-green-600'
                      : 'text-red-600'
                  ]">Blood sugar: {{ status.blood_sugar }}</span>
                  {{ ' | ' }}
                  <span :class="[
                    status.blood_sugar >= 105
                      ? 'text-green-600'
                      : 'text-red-600'
                  ]">Blood sugar: {{ status.blood_sugar }}</span>
                </p>
              </div>
            </div>
            <div class="mt-5 flex flex-col justify-center sm:mt-0">
              <p class="text-gray-900 block">{{ client.email }}</p>
              <p class="text-gray-900 block">{{ client.phone }}</p>
            </div>
          </div>
        </div>
        <div
          class="grid grid-cols-1 divide-y divide-gray-200 border-t border-gray-200 bg-gray-50 sm:grid-cols-6 sm:divide-y-0 sm:divide-x">
          <div class="px-6 py-2 text-center text-sm font-medium">
            <p class="text-gray-900">Heart: {{ status.heart_condition }}</p>
          </div>
          <div class="px-6 py-2 text-center text-sm font-medium">
            <p class="text-gray-900">Blood sugar: {{ status.blood_sugar }}</p>
          </div>
          <div class="px-6 py-2 text-center text-sm font-medium">
            <p class="text-gray-900">Blood pressure: {{ status.blood_pressure }}</p>
          </div>
          <div class="px-6 py-2 text-center text-sm font-medium">
            <p class="text-gray-900">Smoking Status: {{ status.smoking_status ? 'Smoking' : 'Not smoking' }}
            </p>
          </div>
          <div class="px-6 py-2 text-center text-sm font-medium">
            <p class="text-gray-900">Heart: {{ status.heart_condition }}</p>
          </div>
        </div>
      </div>







      <div class="mx-auto mt-3 grid max-w-3xl grid-cols-1 gap-6 lg:max-w-7xl lg:grid-flow-col-dense lg:grid-cols-3">
        <div class="space-y-4 lg:col-span-2 lg:col-start-1">
          <!-- Description list-->
          <section aria-labelledby="applicant-information-title">
            <div class="bg-white shadow sm:rounded-lg">

              <div class="border-t border-gray-200 px-4 py-3 sm:px-6">
                <dl class="grid grid-cols-1 gap-x-4 gap-y-8 divide-y sm:grid-cols-4">
                  <div class="sm:col-span-4">
                    <Examination :examinations="examination" />
                  </div>





                  <div class="sm:col-span-4">
                    <dt class="text-sm font-medium text-gray-500">Attachments</dt>
                    <dd class="mt-1 text-sm text-gray-900">
                      <ul v-if="attachments" role="list"
                        class="divide-y divide-gray-200 rounded-md border border-gray-200">
                        <li v-for="attachment in attachments" :key="attachment.filename"
                          class="flex items-center justify-between py-3 pl-3 pr-4 text-sm">
                          <div class="flex w-0 flex-1 items-center">
                            <PaperClipIcon class="h-5 w-5 flex-shrink-0 text-gray-400" aria-hidden="true" />
                            <span class="ml-2 w-0 flex-1 truncate">{{
                              attachment.filename
                            }}</span>
                          </div>

                          <div class="ml-4 flex-shrink-0">
                            <a :href="attachment.file"
                              class="font-medium text-blue-600 hover:text-blue-500">Download</a>
                          </div>
                        </li>
                      </ul>
                    </dd>
                  </div>
                </dl>
              </div>
              <div>
                <a href="#"
                  class="block bg-gray-50 px-4 py-4 text-center text-sm font-medium text-gray-500 hover:text-gray-700 sm:rounded-b-lg">Read
                  full application</a>
              </div>
            </div>
          </section>
        </div>

        <section aria-labelledby="timeline-title" class="lg:col-span-1 lg:col-start-3">
          <div class="bg-white px-4 py-5 shadow sm:rounded-lg sm:px-6">
            <h2 id="timeline-title" class="text-lg font-medium text-gray-900">Timeline</h2>

            <!-- Activity Feed -->
            <div class="mt-6 flow-root">
              <ul role="list" class="-mb-8">
                <li v-for="(item, itemIdx) in timeline" :key="item.id">
                  <div class="relative pb-8">
                    <span v-if="itemIdx !== timeline.length - 1"
                      class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200" aria-hidden="true" />
                    <div class="relative flex space-x-3">
                      <div>
                        <span
                          :class="[item.type.bgColorClass, 'h-8 w-8 rounded-full flex items-center justify-center ring-8 ring-white']">
                          <component :is="item.type.icon" class="h-5 w-5 text-white" aria-hidden="true" />
                        </span>
                      </div>
                      <div class="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5">
                        <div>
                          <p class="text-sm text-gray-500">
                            {{ item.content }} <a href="#" class="font-medium text-gray-900">{{ item.target }}</a>
                          </p>
                        </div>
                        <div class="whitespace-nowrap text-right text-sm text-gray-500">
                          <time :datetime="item.datetime">{{ item.date }}</time>
                        </div>
                      </div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
            <div class="justify-stretch mt-6 flex flex-col">
              <button type="button"
                class="inline-flex items-center justify-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">Advance
                to offer</button>
            </div>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import Examinations from "../../components/Examinations.vue"
import Examination from "../../components/Examination.vue"
// import fetchClientData from "../../composables/useFetchClientDetails"
import fetchClientAppointmentsData from "../../composables/useFetchAppointmentDetail"
import fetchClientData from "../../composables/useFetchClientDetails"

import axios from "axios"
import {
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  Popover,
  PopoverButton,
  PopoverOverlay,
  PopoverPanel,
  TransitionChild,
  TransitionRoot,
} from '@headlessui/vue'
import {
  ArrowLongLeftIcon,
  CheckIcon,
  HandThumbUpIcon,
  HomeIcon,
  MagnifyingGlassIcon,
  PaperClipIcon,
  QuestionMarkCircleIcon,
  EllipsisVerticalIcon,
  UserIcon,
} from '@heroicons/vue/20/solid'
import { Bars3Icon, BellIcon, XMarkIcon } from '@heroicons/vue/24/outline'
import Breadcrumbs from "../../components/Navbar/BreadCrumbs.vue"
import { useClientStore } from "../../stores/client"
const store = useClientStore()
const props = defineProps({
  id: { type: String, required: true }
})
// const fetchPerson = async () => {
//     const url = `http://127.0.0.1:8000/clients/clients/${props.id}`
//     const res = await axios.get(url, store.useConfig)
//     client.value = res.data
//     console.log(client.value)
// }
const client = ref(null)
const status = ref(null)
const examination = ref(null)
const attachments = ref([])
const details = ref(null)

onMounted(async () => {
  const { client: clientData, status: statusData, attachments: attachmentsData, examination: examinationData, details: detailsData } = await fetchClientData(props.id);
  client.value = clientData;
  status.value = statusData;
  examination.value = examinationData;
  attachments.value = attachmentsData;
  details.value = detailsData;
});
const user = {
  name: 'Whitney Francis',
  email: 'whitney@example.com',
  imageUrl:
    'https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=256&h=256&q=80',
}
const navigation = [
  { name: 'Dashboard', href: '#' },
  { name: 'Jobs', href: '#' },
  { name: 'Applicants', href: '#' },
  { name: 'Company', href: '#' },
]

const userNavigation = [
  { name: 'Your Profile', href: '#' },
  { name: 'Settings', href: '#' },
  { name: 'Sign out', href: '#' },
]
const projects = [
  { name: 'Graph API', initials: 'GA', href: '#', members: 16, bgColor: 'bg-pink-600' },
  { name: 'Component Design', initials: 'CD', href: '#', members: 12, bgColor: 'bg-purple-600' },
  { name: 'Templates', initials: 'T', href: '#', members: 16, bgColor: 'bg-yellow-500' },
  { name: 'React Components', initials: 'RC', href: '#', members: 8, bgColor: 'bg-green-500' },
]
const eventTypes = {
  applied: { icon: UserIcon, bgColorClass: 'bg-gray-400' },
  advanced: { icon: HandThumbUpIcon, bgColorClass: 'bg-blue-500' },
  completed: { icon: CheckIcon, bgColorClass: 'bg-green-500' },
}
const timeline = [
  {
    id: 1,
    type: eventTypes.applied,
    content: 'Applied to',
    target: 'Front End Developer',
    date: 'Sep 20',
    datetime: '2020-09-20',
  },
  {
    id: 2,
    type: eventTypes.advanced,
    content: 'Advanced to phone screening by',
    target: 'Bethany Blake',
    date: 'Sep 22',
    datetime: '2020-09-22',
  },
  {
    id: 3,
    type: eventTypes.completed,
    content: 'Completed phone screening with',
    target: 'Martha Gardner',
    date: 'Sep 28',
    datetime: '2020-09-28',
  },
  {
    id: 4,
    type: eventTypes.advanced,
    content: 'Advanced to interview by',
    target: 'Bethany Blake',
    date: 'Sep 30',
    datetime: '2020-09-30',
  },
  {
    id: 5,
    type: eventTypes.completed,
    content: 'Completed interview with',
    target: 'Katherine Snyder',
    date: 'Oct 4',
    datetime: '2020-10-04',
  },
]
const comments = [
  {
    id: 1,
    name: 'Leslie Alexander',
    date: '4d ago',
    imageId: '1494790108377-be9c29b29330',
    body: 'Ducimus quas delectus ad maxime totam doloribus reiciendis ex. Tempore dolorem maiores. Similique voluptatibus tempore non ut.',
  },
  {
    id: 2,
    name: 'Michael Foster',
    date: '4d ago',
    imageId: '1519244703995-f4e0f30006d5',
    body: 'Et ut autem. Voluptatem eum dolores sint necessitatibus quos. Quis eum qui dolorem accusantium voluptas voluptatem ipsum. Quo facere iusto quia accusamus veniam id explicabo et aut.',
  },
  {
    id: 3,
    name: 'Dries Vincent',
    date: '4d ago',
    imageId: '1506794778202-cad84cf45f1d',
    body: 'Expedita consequatur sit ea voluptas quo ipsam recusandae. Ab sint et voluptatem repudiandae voluptatem et eveniet. Nihil quas consequatur autem. Perferendis rerum et.',
  },
]

const stats = [
  { label: 'Vacation days left', value: 12 },
  { label: 'Sick days left', value: 4 },
  { label: 'Personal days left', value: 2 },
]
const perks = [
  {
    name: 'Free returns',
    imageUrl: 'https://tailwindui.com/img/ecommerce/icons/icon-returns-light.svg',
    description: 'Soap',
  },
  {
    name: 'Same day delivery',
    imageUrl: 'https://tailwindui.com/img/ecommerce/icons/icon-calendar-light.svg',
    description:
      'Normal',
  },
  {
    name: 'All year discount',
    imageUrl: 'https://tailwindui.com/img/ecommerce/icons/icon-gift-card-light.svg',
    description: 'Clasic',
  },
  {
    name: 'For the planet',
    imageUrl: 'https://tailwindui.com/img/ecommerce/icons/icon-planet-light.svg',
    description: 'Type 2',
  },
  {
    name: 'Free returns',
    imageUrl: 'https://tailwindui.com/img/ecommerce/icons/icon-returns-light.svg',
    description: 'Exceptional',
  },
  {
    name: 'Same day delivery',
    imageUrl: 'https://tailwindui.com/img/ecommerce/icons/icon-calendar-light.svg',
    description:
      'Type 1',
  },
  {
    name: 'All year discount',
    imageUrl: 'https://tailwindui.com/img/ecommerce/icons/icon-gift-card-light.svg',
    description: 'Classic',
  },
  {
    name: 'For the planet',
    imageUrl: 'https://tailwindui.com/img/ecommerce/icons/icon-planet-light.svg',
    description: 'Normal',
  },
]
</script>

<style scoped>
html {
  @apply h-full bg-gray-100;
}

body {
  @apply h-full
}
</style>
