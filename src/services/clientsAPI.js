import API from "./baseAPI";
// import config from "./CONFIG";

export default {
  loadClients(config) {
    return API().post("/clients/all/", config);
  },
  // getLoggedInUser() {
  //   return API().get("/user/me/");
  // },
};
