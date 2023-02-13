<template>
    <div v-if="showLoading" class="loading-container">
        <div class="loader ease-linear rounded-full border-4 border-t-4 border-gray-200 h-12 w-12 mb-4"></div>
        <h2 class="text-center text-white text-xl font-semibold">Loading...</h2>
        <p class="w-1/3 text-center text-white">{{ progress }}%</p>
    </div>
</template>

<script setup>
import { watch, ref } from 'vue';
import { useProgressStore } from "@/stores/progress.js";


const progressStore = useProgressStore();
const showLoading = ref(false);

watch(() => progressStore.useProgress, (newValue) => {
    console.log('GLOBAL LOADING LOADED');
    if (newValue > 0) {
        showLoading.value = true;
    } else {
        showLoading.value = false;
    }
});



</script>

<style>
.loader {
    border-top-color: #3498db;
    -webkit-animation: spinner 1.5s linear infinite;
    animation: spinner 1.5s linear infinite;
}

@-webkit-keyframes spinner {
    0% {
        -webkit-transform: rotate(0deg);
    }

    100% {
        -webkit-transform: rotate(360deg);
    }
}

@keyframes spinner {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
</style>
<!-- 
<template>
  <div v-if="loading">
    <div class="loader ease-linear rounded-full border-4 border-t-4 border-gray-200 h-12 w-12 mb-4"></div>
    <h2 class="text-center text-white text-xl font-semibold">Loading...</h2>
    <p class="w-1/3 text-center text-white">{{ progress }}%</p>
  </div>
</template>

<script>
import { inject } from "vue";

export default {
  setup() {
    const progress = inject("progress");

    return {
      progress: computed(() => progress.useProgress)
    };
  }
};
</script> -->