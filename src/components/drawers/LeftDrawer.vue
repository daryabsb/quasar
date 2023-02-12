<template>
    <q-drawer v-model="drawer" show-if-above :mini="!drawer || miniState" @click.capture="drawerClick" :width="200"
        :breakpoint="500" bordered class="bg-grey-3">
        <template v-slot:mini>
            <q-scroll-area class="fit mini-slot cursor-pointer">
                <div class="q-py-lg">
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
</template>

<script setup lang="ts">
// import EssentialLink from 'components/EssentialLink.vue'

// const {
//     drawer = false,
//     miniState = false,
// } = defineProps<{
//     drawer: boolean;
//     miniState: boolean;
// }>();

// const props = withDefaults(
//     defineProps<{ drawer: boolean, miniState: boolean }>(),
//     { drawer: false, miniState: false }
// )
</script>