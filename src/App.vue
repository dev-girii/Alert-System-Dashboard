<template>
  <div id="app">
    <Sidebar />
    <div class="layout">
      <router-view />
    </div>
  </div>
</template>

<script>
import Sidebar from './components/AppSidebar.vue';

export default {
  components: {
    Sidebar
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
