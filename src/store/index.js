import { createStore } from 'vuex';
import hosts from './modules/hosts';
import "/src/assets/index.css";
export default createStore({
  modules: {
    hosts
  }
});
