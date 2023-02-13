<script setup>
import { inject, defineAsyncComponent } from "vue"
const QuickView = defineAsyncComponent(() => import("../components/client/QuickView.vue"))
const { open } = inject("quickview");

</script>
<template>
    <div>
        <QuickView v-if="open" />
    </div>
</template>