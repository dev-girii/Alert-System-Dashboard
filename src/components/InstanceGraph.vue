<template>
  <h2>Usage:</h2>
  <div class="instance-graph-container">
    <div v-for="(data, role) in historyData" :key="role" class="role-section">
      <h3 style="text-align: center;">{{ role }}</h3>
      <div class="chartCollection">
        <!-- <LineChart
          :chart-data="prepareChart(data.cpu, 'cpu_idle', 'CPU Usage', 'rgba(75, 192, 192, 1)')"
          chart-label="CPU Usage"
        />
        <LineChart
          :chart-data="prepareChart(data.mem, 'mem_used_percent', 'Memory Usage', 'rgba(255, 99, 132, 1)')"
          chart-label="Memory Usage"
        /> -->
        <LineChart
  :chart-data="prepareCombinedChart(data)"
  chart-label="CPU & Memory Usage"
/>

      </div>

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
    this.interval = setInterval(() => {
      this.fetchHistory();
    }, 10000);
  },
  beforeUnmount() {
    clearInterval(this.interval);
  },
  methods: {
    async fetchHistory() {
      try {
        const response = await axios.get(`http://localhost:3000/api/history/${this.tender}`);
        console.log(response.data);
        this.historyData = response.data;
        console.log("Loaded history data:", this.historyData);
      } catch (error) {
        console.error("Failed to fetch history:", error);
      }
    },
prepareCombinedChart(data) {
  // Align labels based on CPU data timestamps
  const labels = data.cpu.map(d => new Date(d.time).toLocaleTimeString());

  return {
    labels,
    datasets: [
      {
        label: 'CPU Idle (%)',
        data: data.cpu.map(d => d.cpu_idle),
        borderColor: 'rgba(75, 192, 192, 1)',
        fill: false,
        tension: 0.2
      },
      {
        label: 'Memory Used (%)',
        data: data.mem.map(d => d.mem_used_percent),
        borderColor: 'rgba(255, 99, 132, 1)',
        fill: false,
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
.instance-graph-container{
  padding-top: 0.6rem;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.2rem;
  width: 100%;
}
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
