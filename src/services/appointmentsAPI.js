import API from "./baseAPI";
// import config from "./CONFIG";
// console.log("CONFIG", config());
export default {
  loadAppointments() {
    return API().post("/clients/appointments/");
  },
  getLoggedInUser() {
    return API().get("/user/me/");
  },
};
