<template>
  <q-page class=" row">
    <q-page :style-fn="myTweak" padding class=".col-12 .col-md-6 " style="height: 460px;">
      <q-btn-group push>
        <q-btn color="red" text-color="white" label="First" icon="verified_user" />
        <q-btn color="amber" text-color="black" label="Second" />
        <q-btn color="orange" text-color="black" label="Third" />
      </q-btn-group>
    </q-page>
    <q-page :style-fn="myTweak" padding class=".col-12 .col-md-6 self-center" style="height: 460px;">
      <q-btn-group>
        <q-btn color="red" text-color="white" label="First" icon="verified_user" />
        <q-btn color="amber" text-color="black" label="Second" />
        <q-btn color="orange" text-color="black" label="Third" />
      </q-btn-group>
    </q-page>


  </q-page>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'IndexPage'
})
</script>
