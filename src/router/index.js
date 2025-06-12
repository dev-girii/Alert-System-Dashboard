import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/DashboardMain.vue'
import StatisticsPage from '../views/StatisticsPage.vue'
import NotificationsPage from '../views/NotificationsPage.vue'
import ViewDetails from '@/views/ViewDetails.vue'
import ViewInventory from '@/views/ViewInventory.vue'
const routes = [
  { path: '/', name: 'Dashboard', component: Dashboard },
  { path: '/statistics', name: 'StatisticsPage', component: StatisticsPage },
  { path: '/notifications', name: 'NotificationsPage', component: NotificationsPage },
  {path: '/inventory-details', name: 'ViewInventory', component: ViewInventory},
  {path: '/view-details-:tender',name: 'ViewDetails',component: ViewDetails, props: true}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
