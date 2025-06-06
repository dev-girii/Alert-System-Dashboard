import { createApp } from 'vue'
import App from './App.vue'
import store from './store'  // import your Vuex store

const app = createApp(App)
app.use(store)              // IMPORTANT: use the store
app.mount('#app')