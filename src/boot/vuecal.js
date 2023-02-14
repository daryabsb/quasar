import { boot } from "quasar/wrappers";
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";

export default boot(({ app }) => {
  app.component("vue-cal", VueCal);
});
