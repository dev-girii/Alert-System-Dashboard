import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/DashboardMain.vue'
import StatisticsPage from '../views/StatisticsPage.vue'
import NotificationsPage from '../views/NotificationsPage.vue'

const routes = [
  { path: '/', name: 'Dashboard', component: Dashboard },
  { path: '/statistics', name: 'StatisticsPage', component: StatisticsPage },
  { path: '/notifications', name: 'NotificationsPage', component: NotificationsPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
