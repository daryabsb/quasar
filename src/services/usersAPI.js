import API from "./API";

export default {
  logInUser({ email, password }) {
    return API().post("/user/token/", { email, password });
  },
  getLoggedInUser() {
    return API().get("/user/me/");
  },
};
