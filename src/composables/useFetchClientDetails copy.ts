import { ref } from "vue";
import axios from "axios";
import { useClientStore } from "@/stores/client";
import fetchClientAppointmentsData from "@/composables/useFetchAppointmentDetail";
import { Client, Attachment, Examination, Appointment } from "./interfaces";

const store = useClientStore(); // store has all the config, clients and appointments stuff
const config = store.useConfig; // config contains all headers and autjorizations for axios

const endpoints = {
  client: "http://127.0.0.1:8000/clients/clients/",
  attachments: "http://127.0.0.1:8000/clients/attachments/",
  examination: "http://127.0.0.1:8000/clients/examinations/",
};

const asyncExec = async (promise: Promise<any>) => {
  try {
    const result = await promise;
    return [null, result];
  } catch (error) {
    return [error, null];
  }
};

export default async function fetchData(clientId: number) {
  // let client = {};
  // let error = null;
  // let attachments = [];
  // let examination = [];
  // let details = [];
  const [error1, client] = await asyncExec(
    axios.get(endpoints.client + clientId, config)
  );
  if (error1) console.log(`Error fetching client data: ${error1}`);

  const [error2, attachments] = await asyncExec(
    axios.get(endpoints.attachments + "?client=" + clientId, config)
  );
  if (error2) console.log(`Error fetching attachments data: ${error2}`);

  const [error3, examination] = await asyncExec(
    axios.get(endpoints.examination + clientId + "/", config)
  );
  if (error3) console.log(`Error fetching examination data: ${error3}`);

  const [error4, details] = await asyncExec(
    fetchClientAppointmentsData(clientId)
  );
  if (error4) console.log(`Error fetching details data: ${error4}`);

  return {
    client,
    attachments,
    examination,
    details,
  };
}
