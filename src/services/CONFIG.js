import { useUserStore } from "@/stores/user";
import { useClientStore } from "@/stores/client";

const Authorization = useUserStore().useToken;
const store = useClientStore();
console.log("CHECK TOKEN", Authorization);

const config = (msg = "") => {
  const conf = {
    headers: {
      Authorization,
    },
    onDownloadProgress: (progressEvent) => {
      if (msg == "clients") {
        store.loadingClients = Math.round(
          (progressEvent.loaded * 100) / progressEvent.total
        );
      }
      console.log(
        progressEvent,
        // `+++ ${(progressEvent.bytes / progressEvent.bytes) * 100}`,
        `${msg} +++ ${progressEvent.progress * 100}`
      );
    },
  };

  return conf;
};

export default config;
