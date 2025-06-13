<template>
  <div class="host-details-container">
    <div class="tender-title">
      <h2>{{ tender }}</h2>
    </div>
    <div style="padding: 1rem;">
      <InstanceTable :tender="tender" />
      <div class="charts-container">
        <InstanceGraph :tender="tender" />
      </div>
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
.tender-title{
    text-align: center;
    padding: 1rem;
    border-bottom: 1px solid;
}
.host-details-container {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f8f9fa;
  min-height: 100vh;
  color: #2c3e50;
}

</style>