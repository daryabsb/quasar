<template>
  <div class="relative isolate overflow-hidden ">
    <div class="absolute border top-64 left-32 h-64 w-64    backdrop-blur-sm shadow-sm">
      <div class="w-full h-full flex justify-center items-center cursor-move" draggable="true">
        <h1 class="text-white drop-shadow-sm text-4xl">Blures</h1>

      </div>
    </div>
    <img src="https://images.unsplash.com/photo-1521737604893-d14cc237f11d" alt=""
      class="absolute inset-0 -z-10 h-full w-full object-cover" />

    <div class="px-6 lg:px-8">


      <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
        <div class="hidden sm:mb-8 sm:flex sm:justify-center">
          <div
            class="relative rounded-full py-1 px-3 text-sm leading-6 text-gray-400 ring-1 ring-white/10 hover:ring-white/20">
            Announcing our next round of funding. <a href="#" class="font-semibold text-white"><span
                class="absolute inset-0" aria-hidden="true" />Read more <span aria-hidden="true">&rarr;</span></a>
          </div>
        </div>
        <div class="text-center">
          <h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl">Data to enrich your online
            business</h1>
          <p class="mt-6 text-lg leading-8 text-gray-300">Anim aute id magna aliqua ad ad non deserunt sunt.
            Qui irure qui lorem cupidatat commodo. Elit sunt amet fugiat veniam occaecat fugiat aliqua.</p>
          <div class="mt-10 flex items-center justify-center gap-x-6">
            <a href="#"
              class="rounded-md bg-indigo-500 px-3.5 py-1.5 text-base font-semibold leading-7 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-400">Get
              started</a>
            <a href="#" class="text-base font-semibold leading-7 text-white">Learn more <span
                aria-hidden="true">→</span></a>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel } from '@headlessui/vue'
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'

const navigation = [
  { name: 'Product', href: '#' },
  { name: 'Features', href: '#' },
  { name: 'Marketplace', href: '#' },
  { name: 'Company', href: '#' },
]

const mobileMenuOpen = ref(false)
</script>
