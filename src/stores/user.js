import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";
import usersAPI from "../services/usersAPI";
import axios from "axios";

export const useUserStore = defineStore("user", {
  state: () => ({
    user: useStorage("user", {}),
    token: useStorage("token", ""),
    signedIn: useStorage("signedIn", false),
    appointments: useStorage("appointments", []),
  }),

  getters: {
    useUser(state) {
      return state.user;
    },
    isAuthenticated(state) {
      return state.signedIn;
    },
    useToken(state) {
      return `Token ${state.token}`;
    },
    useAppointments(state) {
      return state.appointments;
    },
    useAuthHeader() {
      return {
        headers: {
          Authorization: `Token ${this.token}`,
        },
        onDownloadProgress: (progressEvent, msg) =>
          console.log(
            progressEvent,
            // `+++ ${(progressEvent.bytes / progressEvent.bytes) * 100}`,
            `${msg} +++ ${progressEvent.progress * 100}`
          ),
      };
    },
  },

  actions: {
    async fetchUser() {
      // localStorage.setItem("auth");
      const res = await axios.get(
        "http://127.0.0.1:8000/api/user/me/",
        this.useAuthHeader
      );

      const user = await res.data;
      this.user = user;
      this.signedIn = true;
      this.fetchAppointments();
    },
    async fetchAppointments() {
      const res = await axios.get(
        "http://127.0.0.1:8000/clients/appointments/",
        this.useAuthHeader
      );

      const appointments = await res.data;
      this.appointments = appointments.results;
      console.log("APPOINTMENTS", appointments.results);
      // this.signedIn = true;
    },
    async signUp(email, password) {
      const res = await axios.post("http://127.0.0.1:8000/api/user/create/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: { email, password },
      });
      const user = await res.json();
      this.user = user;
    },
    async signIn(email, password) {
      console.log("from login page", email, password);
      try {
        const res = await axios.post(
          "http://127.0.0.1:8000/api/user/token/",
          {
            email,
            password,
          },
          {
            onDownloadProgress: (progressEvent) =>
              console.log(
                progressEvent,
                // `+++ ${(progressEvent.bytes / progressEvent.bytes) * 100}`,
                `USER LOGIN => +++ ${progressEvent.progress * 100}`
              ),
          }
        );
        this.token = await res.data.token;
        localStorage.setItem("auth_token", res.data.token);
        await this.fetchUser();
      } catch (error) {
        console.log(error);
      }
    },
    signOut() {
      this.user = {};
      this.token = "";
      this.signedIn = false;
    },

    //   pingServer(url = "") {
    //     const ping = require("web-pingjs");

    //     ping(url)
    //       .then(function (delta) {
    //         console.log("Ping time was " + String(delta) + " ms");
    //       })
    //       .catch(function (err) {
    //         console.error("Could not ping remote URL", err);
    //       });
    //   },
  },
});
