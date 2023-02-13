import { defineStore } from "pinia";

export const useProgressStore = defineStore("progress", {
  state: () => ({
    progress: 0,
    totalRequests: 0,
    completedRequests: 0,
  }),
  getters: {
    useProgress(state) {
      return state.progress;
    },
  },
  actions: {
    incrementProgress() {
      this.completedRequests += 1;
      this.progress = (this.completedRequests / this.totalRequests) * 100;
    },
    setTotalRequests(total) {
      this.totalRequests = total;
    },
    resetProgress() {
      this.progress = 0;
      this.totalRequests = 0;
      this.completedRequests = 0;
    },
  },
});
