<script setup lang="ts">
import { computed } from "vue";
import { useRouter } from "vue-router"
import { useUserStore } from "@/stores/user.js";

import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import { ChevronDownIcon } from "@heroicons/vue/20/solid";

const store = useUserStore();
const router = useRouter()
const user = computed(() => store.useUser);
const signOut = () => {
    store.signOut()
    router.push("/login")

}





const userNavigation = [
    { name: 'Your Profile', href: '#' },
    { name: 'Settings', href: '#' },
]


</script>
<template>
    <!-- Profile dropdown -->
    <Menu as="div" class="relative ml-3">
        <div>
            <MenuButton
                class="flex max-w-xs items-center rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
                <span class="sr-only">Open user menu</span>
                <img v-if="user && user.image" class="h-12 w-12 rounded-full" :src="user.image" alt="" />
            </MenuButton>
        </div>
        <transition enter-active-class="transition ease-out duration-100"
            enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
            leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
            leave-to-class="transform opacity-0 scale-95">
            <MenuItems
                class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <MenuItem v-for="item in userNavigation" :key="item.name" v-slot="{ active }">
                <router-link :to="item.href"
                    :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']">{{
                        item.name
                    }}</router-link>
                </MenuItem>
                <MenuItem>
                <button class="block px-4 py-2 text-sm text-gray-700" @click="signOut">
                    Signout
                </button>
                </MenuItem>
            </MenuItems>
        </transition>
    </Menu>
</template>