<template>
  <Provider>

    <q-layout view="hHh lpR fFf">
      <q-header elevated>
        <q-toolbar>
          <q-btn flat round dense icon="menu" class="q-mr-sm" @click="toggleLeftDrawer" />
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>

          <q-toolbar-title>Quasar Framework</q-toolbar-title>

          <q-btn flat round dense icon="whatshot" />
        </q-toolbar>

        <q-tabs v-model="model">
          <q-tab v-for="tab in options" :key="tab.value">{{ tab.label }}</q-tab>
        </q-tabs>
      </q-header>

      <!-- <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />
      <q-tabs v-model="model" flat stretch>
      <q-tab v-for="tab in options" :key="tab.value">{{ tab.label }}</q-tab>
    </q-tabs> -->
      <q-drawer v-model="leftDrawerOpen" show-if-above :mini="!leftDrawerOpen || miniState" @click.capture="drawerClick"
        :breakpoint="500" bordered class="bg-grey-3">
        <template v-slot:mini>
          <q-scroll-area class="fit mini-slot cursor-pointer">
            <div>
              <div class="column items-start">
                <q-icon name="inbox" color="blue" class="mini-icon" />
                <q-icon name="star" color="orange" class="mini-icon" />
                <q-icon name="send" color="purple" class="mini-icon" />
                <q-icon name="drafts" color="teal" class="mini-icon" />
              </div>
            </div>
          </q-scroll-area>
        </template>

        <q-scroll-area class="fit">
          <q-list padding>
            <q-item clickable v-ripple>
              <q-item-section>
                Inbox
              </q-item-section>
            </q-item>

            <q-item active clickable v-ripple>
              <q-item-section>
                Star
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple>
              <q-item-section>
                Send
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple>
              <q-item-section>
                Drafts
              </q-item-section>
            </q-item>
          </q-list>
        </q-scroll-area>

        <!--
        in this case, we use a button (can be anything)
        so that user can switch back
        to mini-mode
      -->
        <div class="q-mini-drawer-hide absolute" style="top: 15px; right: -17px">
          <q-btn dense round unelevated color="accent" icon="chevron_left" @click="miniState = true" />
        </div>
      </q-drawer>
      <q-page-container>
        <router-view />
      </q-page-container>
      <q-footer bordered class="bg-grey-8 flex text-white q-px-lg">
        <q-toolbar>
          <q-toolbar-title>
            <div class="flex space-x-5">
              <q-avatar>
                <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
              </q-avatar>
              <div>Title</div>
            </div>

          </q-toolbar-title>
        </q-toolbar>
      </q-footer>
    </q-layout>
  </Provider>
</template>

<script>
import { defineComponent, ref } from 'vue'
// import EssentialLink from 'components/EssentialLink.vue'
import Provider from "../providers/index.vue"
const linksList = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Discord Chat Channel',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Forum',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev'
  },
  {
    title: 'Twitter',
    caption: '@quasarframework',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev'
  },
  {
    title: 'Facebook',
    caption: '@QuasarFramework',
    icon: 'public',
    link: 'https://facebook.quasar.dev'
  },
  {
    title: 'Quasar Awesome',
    caption: 'Community Quasar projects',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev'
  }
]

export default defineComponent({
  name: 'MainLayout',

  components: {
    Provider,
    // EssentialLink
  },

  setup() {
    const leftDrawerOpen = ref(false)
    const miniState = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      drawer: ref(false),
      miniState,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      drawerClick(e) {
        // if in "mini" state and user
        // click on drawer, we switch it to "normal" mode
        if (miniState.value) {
          miniState.value = false

          // notice we have registered an event with capture flag;
          // we need to stop further propagation as this click is
          // intended for switching drawer to "normal" mode only
          e.stopPropagation()
        }
      },
      model: ref('one'),

      options: [
        { label: 'One', value: 'one' },
        { label: 'Two', value: 'two' },
        { label: 'Three', value: 'three' }
      ]
    }
  }
})
</script>
<style lang="sass" scoped>
.mini-slot
  transition: background-color .28s
  &:hover
    background-color: rgba(0, 0, 0, .04)

.mini-icon
  font-size: 1.718em
  padding: 2px 16px

  & + &
    margin-top: 18px
</style>
