<template>
    <div class="bg-white">
        <div class="mx-auto max-w-7xl py-12 px-6 text-center lg:px-8 lg:py-16">
            <div class="space-y-6 sm:space-y-8">
                <div class="space-y-2 sm:mx-auto sm:max-w-xl sm:space-y-1 lg:max-w-5xl">
                    <h2 class="text-3xl font-bold tracking-tight sm:text-4xl">Clients</h2>
                    <!-- <p class="text-xl text-gray-500">Risus velit condimentum vitae tincidunt tincidunt. Mauris ridiculus
                        fusce amet urna nunc. Ut nisl ornare diam in.</p> -->
                </div>
                <ul role="list"
                    class="mx-auto h-[32rem] overflow-y-auto grid grid-cols-2 gap-x-1 gap-y-2 sm:grid-cols-4 md:gap-x-2 lg:max-w-6xl lg:gap-x-4 lg:gap-y-2 xl:grid-cols-6">
                    <li v-for="person in people" :key="person.name">
                        <div class="relative space-y-2">
                            <div class="absolute top-8 left-12 group flex items-end p-8">
                                <button type="button"
                                    class="relative z-10 w-full rounded-md bg-white bg-blend-multiply bg-opacity-30  px-2 text-sm text-gray-900 opacity-0 focus:opacity-100 group-hover:opacity-100"
                                    @click="toggleQuickView(+person.id)">Quick View<span class="sr-only">,
                                        {{ person.name }}</span></button>
                            </div>
                            <img class="mx-auto h-20 w-20 rounded-full lg:h-24 lg:w-24 object-cover object-top"
                                :src="person.image" alt="" />
                            <div class="space-y-1">
                                <div class="text-xs font-medium lg:text-sm">
                                    <h3>{{ person.name }}</h3>
                                    <p class="text-indigo-600">{{ person.role }}</p>
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
            <div class="w-full mt-4 ">
                <nav class="flex items-center justify-between border-t border-gray-200 bg-white px-4 pt-3 py-1 sm:px-6"
                    aria-label="Pagination">
                    <div class="hidden sm:block">
                        <p class="text-sm text-gray-700">
                            Showing
                            {{ ' ' }}
                            <span class="font-medium">{{ startIndex+ 1 }}</span>
                            {{ ' ' }}
                            to
                            {{ ' ' }}
                            <span class="font-medium">{{ endIndex }}</span>
                            {{ ' ' }}
                            of
                            {{ ' ' }}
                            <span class="font-medium">{{ peopleCount }}</span>
                            {{ ' ' }}
                            results
                        </p>
                    </div>
                    <div class="flex flex-1 justify-between sm:justify-end">
                        <button
                            class="relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
                            @click.prevent="changePage('prev')">Previous</button>
                        <button
                            class="relative ml-3 inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
                            @click.prevent="changePage('next')">Next</button>
                    </div>
                </nav>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { computed, ref, watchEffect, inject } from "vue"
import axios from "axios"
import { useClientStore } from "../../stores/client"

const store = useClientStore()
const clients = store.useClients

const people = ref([])
const peopleCount = ref(0)
const page = ref(1)
const pageSize = ref(12)

const startIndex = computed(() => +(page.value - 1) * pageSize.value);
const endIndex = computed(() => {
    const end = +startIndex.value + +pageSize.value;
    return end > peopleCount.value ? peopleCount.value : end;
});
const totalPages = computed(() => Math.ceil(peopleCount.value / pageSize.value))
const { open, toggleQuickView } = inject("quickview")



const maxPage = computed(() => {
    return peopleCount.value % pageSize.value < people.value.length
})

const fetchPeople = async () => {
    const url = `http://127.0.0.1:8000/clients/clients/?page_size=${pageSize.value}&page=${page.value}`
    const res = await axios.get(url, store.useConfig)
    people.value = res.data.results
    peopleCount.value = res.data.count
}
watchEffect(fetchPeople)

const changePage = (direction: string) => {
    if (direction === 'next' && maxPage.value) {
        page.value++
    } else if (direction === 'prev' && page.value > 1) {
        page.value--
    }
}


</script>