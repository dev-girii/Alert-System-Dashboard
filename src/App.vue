<template>
  <div id="app">
    <Sidebar />
    <div class="layout">
      <DashboardHeader />
      <SearchAndFilter />
      <Dashboard />
    </div>
  </div>
</template>

<script>
import DashboardHeader from './components/DashboardHeader.vue';
import Sidebar from './components/AppSidebar.vue';
import Dashboard from './views/DashboardMain.vue';
import SearchAndFilter from './components/SearchAndFilter.vue';
export default {
  components: {
    DashboardHeader,
    Sidebar,
    Dashboard,
    SearchAndFilter
  }
};
</script>

<style scoped>
.layout {
  width: calc(100% - 60px);
  height: 100vh;
  background-color: white;
  position: relative;
  left: 60px;
}

@media (max-width: 600px) {
.layout{
  width: 100%;
  left: 0;
}
}
</style>
