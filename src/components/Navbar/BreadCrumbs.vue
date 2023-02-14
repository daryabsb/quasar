<template>
    <header class="bg-white shadow">


        <div class="mx-auto max-w-7xl px-4 sm:px-6">
            <div class="border-t border-gray-200 py-3">
                <nav class="flex" aria-label="Breadcrumb">

                    <div v-if="$q.screen.gt.sm">
                        <!-- <div> -->
                        <ol role="list" class="flex items-center space-x-4">

                            <li>
                                <div>
                                    <router-link to="/" class="text-gray-400 hover:text-gray-500">
                                        <HomeIcon class="h-5 w-5 flex-shrink-0" aria-hidden="true" />
                                        <span class="sr-only">Home</span>
                                    </router-link>
                                </div>
                            </li>
                            <li v-for="item in breadcrumbs" :key="item.name">
                                <div class="flex items-center">
                                    <svg class="h-5 w-5 flex-shrink-0 text-gray-300" xmlns="http://www.w3.org/2000/svg"
                                        fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                                        <path d="M5.555 17.776l8-16 .894.448-8 16-.894-.448z" />
                                    </svg>
                                    <router-link :to="item.route"
                                        class="ml-4 text-sm font-medium text-gray-500 hover:text-gray-700">{{
    item.name
                                        }}</router-link>
                                </div>
                            </li>

                        </ol>
                    </div>
                    <div v-else class="flex ">
                        <a href="/"
                            class="group inline-flex space-x-3 text-sm font-medium text-gray-500 hover:text-gray-700">
                            <ArrowLongLeftIcon class="h-5 w-5 flex-shrink-0 text-gray-400 group-hover:text-gray-600"
                                aria-hidden="true" />
                            <span>Back to Applicants</span>
                        </a>
                    </div>
                </nav>
            </div>
        </div>
    </header>
</template>

<script setup>
import { ref } from "vue"

import {
    ArrowLongLeftIcon,
    CheckIcon,
    HandThumbUpIcon,
    HomeIcon,
    MagnifyingGlassIcon,
    PaperClipIcon,
    QuestionMarkCircleIcon,
    UserIcon,
} from '@heroicons/vue/20/solid'

defineProps({
    breadcrumbs: { type: Array, required: true }
})


</script>