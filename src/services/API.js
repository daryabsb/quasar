import axios from "axios";
import { useUserStore } from "../stores/user";

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export default (url = "http://127.0.0.1:8000/api") => {
  return axios.create({
    baseURL: url,
  });
};
