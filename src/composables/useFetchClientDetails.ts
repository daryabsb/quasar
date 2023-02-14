import { ref } from "vue";
import axios from "axios";
import { useClientStore } from "../stores/client.js";
import { useProgressStore } from "../stores/progress.js";
import fetchClientAppointmentsData from "../composables/useFetchAppointmentDetail";
import { Client, Attachment, Examination, Appointment } from "./interfaces";

const store = useClientStore(); // store has all the config, clients and appointments stuff
const progress = useProgressStore();
const config = store.useConfig; // config contains all headers and autjorizations for axios

const endpoints = {
  client: "http://127.0.0.1:8000/clients/clients/",
  attachments: "http://127.0.0.1:8000/clients/attachments/",
  examination: "http://127.0.0.1:8000/clients/examinations/",
  status: "http://127.0.0.1:8000/clients/status/",
};

const asyncExec1 = async (promise: Promise<any>) => {
  try {
    const result = await promise;
    return [null, result];
  } catch (error) {
    return [error, null];
  }
};
const asyncExec = async (promise: Promise<any>) => {
  try {
    progress.setTotalRequests(progress.totalRequests + 1);
    const result = await promise;
    progress.incrementProgress();
    return [null, result];
  } catch (error) {
    progress.incrementProgress();
    return [error, null];
  }
};

export default async function fetchData(clientId: number) {
  let client = {};
  let status = {};
  let attachments = [];
  let examination = [];
  let details = [];

  const clientPromise = axios.get(endpoints.client + clientId, config);
  const attachmentsPromise = axios.get(
    endpoints.attachments + "?client=" + clientId,
    config
  );
  const statusPromise = axios.get(endpoints.status + clientId, config);

  const examinationPromise = axios.get(
    endpoints.examination + clientId,
    config
  );
  const detailsPromise = fetchClientAppointmentsData(clientId);

  const [clientError, clientResult] = await asyncExec(clientPromise);
  if (clientError) console.log(`Error fetching client data: ${clientError}`);
  else client = clientResult.data;

  const [statusError, statusResult] = await asyncExec(statusPromise);
  if (statusError) console.log(`Error fetching client data: ${statusError}`);
  else status = statusResult.data;

  const [attachmentsError, attachmentsResult] = await asyncExec(
    attachmentsPromise
  );
  if (attachmentsError)
    console.log(`Error fetching attachments data: ${attachmentsError}`);
  else attachments = attachmentsResult.data.results;

  const [examinationError, examinationResult] = await asyncExec(
    examinationPromise
  );
  if (examinationError)
    console.log(`Error fetching examination data: ${examinationError}`);
  else examination = examinationResult.data;

  const [detailsError, detailsResult] = await asyncExec(detailsPromise);
  if (detailsError) console.log(`Error fetching details data: ${detailsError}`);
  else details = detailsResult;

  return {
    client,
    status,
    attachments,
    examination,
    details,
  };
}
