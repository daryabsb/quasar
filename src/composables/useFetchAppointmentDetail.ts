import axios from "axios";
import { useClientStore } from "../stores/client";
import { Appointment } from "./interfaces";

const store = useClientStore(); // store has all the config, clients and appointments stuff
const config = store.useConfig; // config contains all headers and autjorizations for axios

const endpoints = {
  appointments: "http://127.0.0.1:8000/appointment/appointments/",
  prescriptions: "http://127.0.0.1:8000/appointment/prescriptions/",
  treatments: "http://127.0.0.1:8000/appointment/treatments/",
  medications: "http://127.0.0.1:8000/appointment/medications/",
};

export default async function fetchData(clientId: number) {
  const appointments = (
    await axios.get(endpoints.appointments + `?client=${clientId}`, config)
  ).data.results;
  const pastAppointments = await appointments.filter(
    (appointment: Appointment) => new Date(appointment.date) < new Date()
  );
  const nextAppointment = await appointments.find(
    (appointment: Appointment) => new Date(appointment.date) > new Date()
  );

  return {
    pastAppointments,
    nextAppointment,
  };
}
