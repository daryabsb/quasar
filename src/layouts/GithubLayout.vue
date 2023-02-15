<template>
  <Provider>

    <q-layout class="bg-grey-1">

      <q-header elevated class="text-white" style="background: #24292e" height-hint="61.59">
        <q-toolbar class="q-py-sm q-px-md">
          <router-link to="/">
            <q-btn round dense flat :ripple="false" :icon="fasUserDoctor" size="19px" color="white" class="q-mr-sm"
              no-caps />
          </router-link>



          <q-select ref="search" dark dense standout use-input hide-selected class="GL__toolbar-select" color="black"
            :stack-label="false" label="Search or jump to..." v-model="text" :options="filteredOptions" @filter="filter"
            style="width: 350px">

            <template v-slot:append>
              <img src="https://cdn.quasar.dev/img/layout-gallery/img-github-search-key-slash.svg">
            </template>

            <template v-slot:no-option>
              <q-item>
                <q-item-section>
                  <div class="text-center">
                    <q-spinner-pie color="grey-5" size="24px" />
                  </div>
                </q-item-section>
              </q-item>
            </template>

            <template v-slot:option="scope">
              <q-item v-bind="scope.itemProps" class="GL__select-GL__menu-link">
                <q-item-section side>
                  <q-icon name="collections_bookmark" />
                </q-item-section>
                <q-item-section>
                  <q-item-label v-html="scope.opt.label" />
                </q-item-section>
                <q-item-section side :class="{ 'default-type': !scope.opt.type }">
                  <q-btn outline dense no-caps text-color="blue-grey-5" size="12px" class="bg-grey-1 q-px-sm">
                    {{ scope.opt.type || 'Jump to' }}
                    <q-icon name="subdirectory_arrow_left" size="14px" />
                  </q-btn>
                </q-item-section>
              </q-item>
            </template>
          </q-select>
          <q-space></q-space>
          <div v-if="$q.screen.gt.sm"
            class="GL__toolbar-link q-ml-xs q-gutter-md text-body2 text-weight-bold row items-center no-wrap uppercase space-x-8">
            <a href="#/clients" class="text-white">
              Clients
            </a>
            <a href="#/appointments" class="text-white">
              Appointments
            </a>
            <a href="#/visits" class="text-white">
              Visits
            </a>
            <a href="#/users" class="text-white">
              Users
            </a>
            <a href="#/playground" class="text-white">
              Playground
            </a>

          </div>

          <q-space />

          <div class="q-pl-sm q-gutter-sm row items-center no-wrap">
            <q-btn v-if="$q.screen.gt.xs" dense flat round size="md" icon="notifications" />
            <q-btn v-if="$q.screen.gt.xs" dense flat size="md">
              <div class="row items-center no-wrap">
                <q-icon name="add" size="28px" />
                <q-icon name="arrow_drop_down" size="16px" style="margin-left: -2px" />
              </div>
              <q-menu auto-close>
                <q-list dense style="min-width: 100px">
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>New repository</q-item-section>
                  </q-item>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>Import repository</q-item-section>
                  </q-item>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>New gist</q-item-section>
                  </q-item>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>New organization</q-item-section>
                  </q-item>
                  <q-separator />
                  <q-item-label header>This repository</q-item-label>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>New issue</q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </q-btn>

            <q-btn dense flat no-wrap>
              <q-avatar v-if="user && user.image" rounded size="40px">
                <img :src="user.image">
              </q-avatar>
              <q-icon name="arrow_drop_down" size="16px" />

              <q-menu auto-close>
                <q-list dense>
                  <q-item class="GL__menu-link-signed-in">
                    <q-item-section>
                      <div>Signed in as <strong>{{ user.name }}</strong></div>
                    </q-item-section>
                  </q-item>
                  <q-separator />
                  <q-item clickable class="GL__menu-link-status">
                    <q-item-section>
                      <div>
                        <q-icon name="tag_faces" color="blue-9" size="18px" />
                        Set your status
                      </div>
                    </q-item-section>
                  </q-item>
                  <q-separator />
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>Your profile</q-item-section>
                  </q-item>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>Your repositories</q-item-section>
                  </q-item>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>Your projects</q-item-section>
                  </q-item>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>Your stars</q-item-section>
                  </q-item>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>Your gists</q-item-section>
                  </q-item>
                  <q-separator />
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>Help</q-item-section>
                  </q-item>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>Settings</q-item-section>
                  </q-item>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section @click="signOut">Sign out</q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </q-btn>
          </div>
        </q-toolbar>
      </q-header>

      <q-drawer v-model="drawer" :mini="miniState" overlay @mouseover="miniState = false" @mouseout="miniState = true"
        :width="200" :breakpoint="500" show-if-above bordered content-class=" bg-zinc-300">
        <q-scroll-area class="fit">
          <q-list padding>
            <q-item clickable v-ripple>
              <q-item-section avatar>
                <q-icon name="inbox" size="md"></q-icon>
              </q-item-section>

              <q-item-section>
                <h1 class="text-lg">
                  Inbox
                </h1>
              </q-item-section>
            </q-item>

            <q-item active clickable v-ripple>
              <q-item-section avatar>
                <q-icon name="star" size="md"></q-icon>
              </q-item-section>

              <q-item-section>
                Star
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple>
              <q-item-section avatar>
                <q-icon name="send"></q-icon>
              </q-item-section>

              <q-item-section>
                Send
              </q-item-section>
            </q-item>

            <q-separator></q-separator>

            <q-item clickable v-ripple>
              <q-item-section avatar>
                <q-icon name="drafts"></q-icon>
              </q-item-section>

              <q-item-section>
                Drafts
              </q-item-section>
            </q-item>
          </q-list>
        </q-scroll-area>
      </q-drawer>

      <q-page-container>
        <router-view />
      </q-page-container>
    </q-layout>
  </Provider>
</template>

<script setup>
import { ref, computed } from 'vue'
import { fasUserDoctor } from '@quasar/extras/fontawesome-v6'
import { useRouter } from "vue-router"
import { useUserStore } from "../stores/user"
import Provider from "../providers/index.vue"

// USER RELATED
const store = useUserStore();
const router = useRouter()
const user = computed(() => store.useUser);
const signOut = () => {
  store.signOut()
  router.push("/login")

}

const stringOptions = [
  'quasarframework/quasar',
  'quasarframework/quasar-awesome'
]

const drawer = ref(true)
const miniState = ref(true)

const text = ref('')
const options = ref(null)
const filteredOptions = ref([])
const search = ref(null) // $refs.search
function filter(val, update) {
  if (options.value === null) {
    // load data
    setTimeout(() => {
      options.value = stringOptions
      search.value.filter('')
    }, 2000)
    update()
    return
  }
  if (val === '') {
    update(() => {
      filteredOptions.value = options.value.map(op => ({ label: op }))
    })
    return
  }
  update(() => {
    filteredOptions.value = [
      {
        label: val,
        type: 'In this repository'
      },
      {
        label: val,
        type: 'All GitHub'
      },
      ...options.value
        .filter(op => op.toLowerCase().includes(val.toLowerCase()))
        .map(op => ({ label: op }))
    ]
  })
}

</script>

<style lang="sass">

.aside 
  transform: translate3d(0px, 0px, 0px)

.GL
  &__select-GL__menu-link
    .default-type
      visibility: hidden
    &:hover
      background: #0366d6
      color: white
      .q-item__section--side
        color: white
      .default-type
        visibility: visible
  &__toolbar-link
    a
      color: white
      text-decoration: none
      &:hover
        opacity: 0.7
  &__menu-link:hover
    background: #0366d6
    color: white
  &__menu-link-signed-in,
  &__menu-link-status
    &:hover
      & > div
        background: white !important
  &__menu-link-status
    color: $blue-grey-6
    &:hover
      color: $light-blue-9
  &__toolbar-select.q-field--focused
    width: 450px !important
    .q-field__append
      display: none
</style>
