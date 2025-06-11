<template>
      <DashboardHeader />
      <SearchAndFilter />
  <div class="dashboard">
    <div class="hosts">
      <HostCard v-for="host in hosts" :key="host.id" :host="host" />
    </div>
    <StatsPanel :cpu="metrics.cpu" :memory="metrics.memory" :disk="metrics.disk" />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import HostCard from '../components/HostCard.vue';
import StatsPanel from '../components/StatsPanel.vue';
import SearchAndFilter from '../components/SearchAndFilter.vue';
import DashboardHeader from '../components/DashboardHeader.vue';
export default {
  components: { HostCard, StatsPanel, DashboardHeader,
    SearchAndFilter},
  computed: {
    ...mapState('hosts', ['hosts', 'metrics'])
  },
    created() {
    this.$store.dispatch('hosts/initSocket'); // Ensure socket connection starts
  }
};
</script>

<style scoped>
.dashboard {
  flex: 1;
  padding: 1rem;
}
.hosts {
    display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); /* Smaller min size for 4 per row */
  gap: 30px; /* Increased spacing */
}
</style>
