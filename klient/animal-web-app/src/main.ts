import { createPinia } from "pinia";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "/src/main.scss";
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { mdi } from "vuetify/iconsets/mdi";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { updateToken } from "@/services/apiClient";
import "@mdi/font/css/materialdesignicons.css";
library.add(fas);

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    sets: {
      mdi,
    },
  },
});

const app = createApp(App);

app.component("font-awesome-icon", FontAwesomeIcon);
updateToken();
app.use(createPinia()).use(router).use(vuetify).mount("#app");
