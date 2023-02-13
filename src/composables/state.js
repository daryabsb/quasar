import { ref } from "vue";

export function useState(initialState) {
  const state = ref(initialState);
  const setState = (newState) => {
    state.value = newState;
  };

  return [state, setState];
}
export const usePlainText = () => useState("plainText");

// import { ref, readonly } from "vue";
// import { useStorage } from "@vueuse/core";
// export function useState(initialState) {
//   const state = ref(initialState);
//   const setState = (newState) => {
//     state.value = newState;
//   };

//   return [readonly(state), setState];
// }
// export const usePlainText = () => useState("plainText", () => "");
