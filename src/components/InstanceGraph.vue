<template>
  <div class="instance-graph-container">
    <div v-for="(data, role) in historyData" :key="role" class="role-section">
      <h3>{{ role }}</h3>
<LineChart
  :chart-data="prepareChart(data.cpu, 'cpu_idle', 'CPU Usage', 'rgba(75, 192, 192, 1)')"
  chart-label="CPU Usage"
/>
<LineChart
  :chart-data="prepareChart(data.mem, 'mem_used_percent', 'Memory Usage', 'rgba(255, 99, 132, 1)')"
  chart-label="Memory Usage"
/>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import LineChart from './LineChart.vue'; // Your wrapper over vue-chartjs

export default {
  props: ['tender'],
  components: { LineChart },
  data() {
    return {
      historyData: {} // format: { role1: { cpu: [...], mem: [...] }, role2: { ... } }
    };
  },
  mounted() {
    this.fetchHistory();
  },
  methods: {
    async fetchHistory() {
      try {
        const response = await axios.get(`http://192.168.1.5:3000/api/history/${this.tender}`);
        console.log(response.data);
        this.historyData = response.data;
        console.log("Loaded history data:", this.historyData);
      } catch (error) {
        console.error("Failed to fetch history:", error);
      }
    },
prepareChart(dataArray, fieldKey, label, color = '#2196F3') {
  return {
    labels: dataArray.map(d => new Date(d.time).toLocaleTimeString()),
    datasets: [
      {
        label,
        data: dataArray.map(d => d[fieldKey]),
        fill: false,
        borderColor: color,
        tension: 0.2
      }
    ]
  };
}

  }
};
</script>

<style scoped>
.role-section {
  margin-bottom: 40px;
}

/* Charts Section */

.chart-card {
  background: #fff;
  padding: 1.2rem;
  border-radius: 12px;
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
  user-select: none;
}

.chart-card h3 {
  font-size: 1.2rem;
  margin-bottom: 0.8rem;
  font-weight: 600;
}
</style>
