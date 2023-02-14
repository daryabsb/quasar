<script setup>
import { inject } from "vue"


</script>

<template>
    <div class="h-screen w-screen flex justify-center items-center">

        <div
            class=" flex flex-col justify-center items-start bg-white p-8 shadow-lg shadow-slate-200 rounded-lg w-full md:w-2/3 lg:w-1/3">
            <!-- PROGRESS 01 -->
            <div v-if="progress1" class="flex items-center justify-between">
                <span class="text-slate-400 text-sm ">Progress 1</span>
                <span
                    class="px-2 py-1 bg-teal-50 rounded-lg text-xs text-teal-400 font-medium min-w-[46px] text-center">0%</span>
            </div>

            <div class="w-full bg-slate-100 h-1 mb-6 mt-2">
                <div class="bg-teal-400 h-1 rounded" :style="{ width: `${loading}%` }"></div>
            </div>
            <!-- PROGRESS 02 -->
            <div v-if="progress2" class="w-full">
                <div class="flex items-center justify-between">
                    <span class="text-slate-400 text-sm ">Progress 2</span>
                    <span
                        class="px-2 py-1 bg-teal-50 rounded-lg text-xs text-teal-400 font-medium min-w-[46px] text-center">25%</span>
                </div>

                <div class="w-full bg-slate-100 h-1 mb-6 mt-2">
                    <div class="bg-teal-400 h-1 rounded" style="width: 25%"></div>
                </div>

            </div>
            <!-- PROGRESS 03 -->
            <div v-if="progress3" class="w-full">
                <div class="flex items-center justify-between">
                    <span class="text-slate-400 text-sm ">Progress 3</span>
                    <span
                        class="px-2 py-1 bg-teal-50 rounded-lg text-xs text-teal-400 font-medium min-w-[46px] text-center">50%</span>
                </div>

                <div class="w-full bg-slate-100 h-1 mb-6 mt-2">
                    <div class="bg-teal-400 h-1 rounded" style="width: 50%"></div>
                </div>
            </div>
            <!-- PROGRESS 04 -->
            <div v-if="progress4" class="w-full">
                <div class="flex items-center justify-between">
                    <span class="text-slate-400 text-sm ">Progress 4</span>
                    <span
                        class="px-2 py-1 bg-teal-50 rounded-lg text-xs text-teal-400 font-medium min-w-[46px] text-center">75%</span>
                </div>

                <div class="w-full bg-slate-100 h-1 mb-6 mt-2">
                    <div class="bg-teal-400 h-1 rounded" style="width: 75%"></div>
                </div>
            </div>
            <!-- PROGRESS 05 -->
            <div v-if="progress5" class="w-full">
                <div class="flex items-center justify-between">
                    <span class="text-slate-400 text-sm ">Progress 5</span>
                    <span
                        class="px-2 py-1 bg-teal-50 rounded-lg text-xs text-teal-400 font-medium min-w-[46px] text-center">100%</span>
                </div>

                <div class="w-full bg-slate-100 h-1 mt-2">
                    <div class="bg-teal-400 h-1 rounded" style="width: 100%"></div>
                </div>
            </div>
        </div>
    </div>
</template>