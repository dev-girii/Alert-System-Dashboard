// import { createApp } from 'vue'
// import App from './App.vue'
// import store from './store'  // import your Vuex store

// const app = createApp(App)
// app.use(store)              // IMPORTANT: use the store
// app.mount('#app')

import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app')
// createApp(App).use(router).mount('#app')
