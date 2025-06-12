<template>
  <div class="host-details-container">
    <InstanceTable :tender="tender" />
    <div class="charts-container">
      <InstanceGraph :tender="tender" />
    </div>
  </div>
</template>

<script>
import InstanceGraph from '@/components/InstanceGraph.vue';
// import LineChart from '../components/LineChart.vue';
import InstanceTable from '@/components/InstanceTable.vue';

export default {
  props: ['tender'],
  components: {InstanceGraph, InstanceTable},
};
</script>

<style scoped>
/* Container */
.host-details-container {
  padding: 2rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f8f9fa;
  min-height: 100vh;
  color: #2c3e50;
}

.charts-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
}
</style>