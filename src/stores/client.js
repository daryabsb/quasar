import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";
import { useUserStore } from "../stores/user";

import clientsAPI from "../services/clientsAPI";
import appointmentsAPI from "../services/appointmentsAPI";
import axios from "axios";

export const useClientStore = defineStore("client", {
  state: () => ({
    clients: useStorage("clients", []),
    appointments: useStorage("appointments", []),
    loadingClients: 0,
  }),

  getters: {
    useClients(state) {
      return state.clients;
    },
    useAppointments(state) {
      return state.appointments;
    },
    useIsLoadingClient(state) {
      return state.loadingClients;
    },
    useConfig(state) {
      const Authorization = useUserStore().useToken;
      return {
        headers: {
          Authorization,
        },
        onDownloadProgress: (progressEvent) => {
          state.loadingClients = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );

          console.log(
            progressEvent,
            // `+++ ${(progressEvent.bytes / progressEvent.bytes) * 100}`,
            `msg +++ ${progressEvent.progress * 100}`
          );
        },
      };
    },
  },

  actions: {
    async fetchClients() {
      // localStorage.setItem("auth");
      console.log("REACHED");
      try {
        const res = await axios.get(
          "http://127.0.0.1:8000/clients/all/",
          this.useConfig
        );
        this.clients = await res.data;
        console.log(this.clients);
      } catch (error) {
        console.log(error);
      }

      console.log("FINITO");
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
  },
});
