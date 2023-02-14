<script setup>
import { ref, computed, onMounted, nextTick } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "../stores/user";
import { useQuasar } from 'quasar'

const $q = useQuasar()

const store = useUserStore();
const router = useRouter();
const email = ref("");
const password = ref("");

const signIn = async () => {
  try {
    await store.signIn(email.value, password.value);
  } catch (error) {
    console.log(error);
  }

  // router.push('/')
  email.value = "";
  password.value = "";
  router.push({ name: "preloader" });
};


// QUASAR

const title = ref('Authorization');
// const email= ref('');
const username = ref('');
// const password = ref('');
const repassword = ref('');
const register = ref(false);
const passwordFieldType = ref('password');
const btnLabel = ref('Login');
const visibility = ref(false);
const visibilityIcon = ref('visibility');



// function required(val) {

// };
const required = computed({
  get() {
    return true
  },
  set(val) {
    return (val && val.length > 0 || 'Field must be filled')
  },
})
function diffPassword(val) {
  const val2 = passwordField.value
  return (val && (val === val2) || "Password doesn't match!")
};
function short(val) {
  return (val && val.length > 3 || 'Value is too short')
};
function isEmail(val) {
  const emailPattern = /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/
  return (emailPattern.test(val) || 'Enter correct email')
};
const emailField = ref(null);
const passwordField = ref(null);
const repasswordField = ref(null);
const usernameField = ref(null);
function submit() {
  if (register.value) {
    emailField.value.validate()
    usernameField.value.validate()
    passwordField.value.validate()
    repasswordField.value.validate()
  } else {
    emailField.value.validate()
    passwordField.value.validate()
  }

  if (!register.value)
    if (!emailField.value.hasError && (!passwordField.value.hasError)) {
      $q.notify({
        icon: 'done',
        color: 'positive',
        message: 'Authorization'
      })
    }
};
function switchTypeForm() {
  register.value = !register.value
  title.value = register.value ? 'New user' : 'Authorization'
  btnLabel.value = register.value ? 'Registration' : 'Login'
};
function switchVisibility() {
  visibility.value = !visibility.value
  passwordFieldType.value = visibility.value ? 'text' : 'password'
  visibilityIcon.value = visibility.value ? 'visibility_off' : 'visibility'
}


</script>
<template>
  <!--
    This example requires updating your template:

    ```
    <html class="h-full bg-gray-50">
    <body class="h-full">
    ```
  -->
  <div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
    <q-layout view="lHh Lpr fff">
      <q-page-container>

        <q-page class="window-height window-width row justify-center items-center"
          style="background: linear-gradient(#8274C5, #5A4A9F);">
          <div class="column q-pa-lg">
            <div class="row">
              <q-card square class="shadow-24" style="width:400px;height:540px;">
                <q-card-section class="bg-deep-purple-7">
                  <h4 class="text-h5 text-white q-my-md">{{ title }}</h4>

                </q-card-section>
                <q-card-section>
                  <q-fab color="primary" @click="switchTypeForm" icon="add" class="absolute"
                    style="top: 0; right: 12px; transform: translateY(-50%);">
                    <q-tooltip>

                      New User Registration
                    </q-tooltip>
                  </q-fab>
                  <q-form class="q-px-sm q-pt-xl">
                    <q-input ref="emailField" square clearable v-model="email" type="email" lazy-rules
                      :rules="[required, isEmail, short]" label="Email">
                      <template v-slot:prepend>
                        <q-icon name="email" />
                      </template>
                    </q-input>
                    <q-input ref="usernameField" v-if="register" square clearable v-model="username" lazy-rules
                      :rules="[required, short]" type="username" label="User">
                      <template v-slot:prepend>
                        <q-icon name="person" />
                      </template>
                    </q-input>
                    <q-input ref="passwordField" square clearable v-model="password" :type="passwordFieldType"
                      lazy-rules :rules="[required, short]" label="
Password">

                      <template v-slot:prepend>
                        <q-icon name="lock" />
                      </template>
                      <template v-slot:append>
                        <q-icon :name="visibilityIcon" @click="switchVisibility" class="cursor-pointer" />
                      </template>
                    </q-input>
                    <q-input ref="repasswordField" v-if="register" square clearable v-model="repassword"
                      :type="passwordFieldType" lazy-rules :rules="[required, short, diffPassword]"
                      label="Repeat password">
                      <template v-slot:prepend>
                        <q-icon name="lock" />
                      </template>
                      <template v-slot:append>
                        <q-icon :name="visibilityIcon" @click="switchVisibility" class="cursor-pointer" />
                      </template>
                    </q-input>
                  </q-form>
                </q-card-section>

                <q-card-actions class="q-px-lg">
                  <q-btn unelevated size="lg" color="secondary" @click="submit" class="full-width text-white"
                    :label="btnLabel" />
                </q-card-actions>
                <q-card-section v-if="!register" class="text-center q-pa-sm">
                  <p class="text-grey-6">Forgot your password?</p>
                </q-card-section>
              </q-card>
            </div>
          </div>

        </q-page>
      </q-page-container>
    </q-layout>
  </div>
</template>
