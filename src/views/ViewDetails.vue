<template>
  <div class="host-details-container">
    <h2 class="host-title">🖥️ Instance: {{ host.name }}</h2>
    <div class="resource-table">
      <table>
        <thead>
          <tr>
            <th>Node Type</th>
            <th>CPU (%)</th>
            <th>RAM (GB)</th>
            <th>Memory (GB)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="node in host.nodes" :key="node.type">
            <td>{{ node.type }}</td>
            <td>{{ node.cpu }}</td>
            <td>{{ node.ram }}</td>
            <td>{{ node.memory }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="charts-container">
      <div class="chart-card">
        <h3>Web Server - CPU Usage</h3>
        <LineChart :labels="labels" :data="cpuData" label="CPU (%)" color="#3b82f6" />
      </div>

      <div class="chart-card">
        <h3>Web Server - RAM Usage</h3>
        <LineChart :labels="labels" :data="ramData" label="RAM (GB)" color="#22c55e" />
      </div>
    </div>
  </div>
</template>

<script>
import LineChart from '../components/LineChart.vue';

export default {
  name: 'HostDetails',
  components: { LineChart },
  props: ['hostId'],
  data() {
    return {
      labels: ['T-5', 'T-4', 'T-3', 'T-2', 'T-1', 'Now'],
      host: {
        id: '1',
        name: 'Instance-A',
        nodes: [
          { type: 'Web Server', cpu: 45, ram: 8, memory: 120 },
          { type: 'Database', cpu: 70, ram: 16, memory: 240 },
          { type: 'Cache', cpu: 25, ram: 4, memory: 80 }
        ]
      },
      cpuData: [30, 35, 40, 45, 50, 48],
      ramData: [6, 6.5, 7, 7.5, 8, 8]
    };
  }
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

/* Title */
.host-title {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  user-select: none;
}

/* Table Styling */
.resource-table table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin-bottom: 2rem;
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  font-variant-numeric: tabular-nums;
}

.resource-table thead tr {
  background: linear-gradient(90deg, #e0f2ff, #bbdefb);
  color: #0d3b66;
}

.resource-table th {
  font-weight: 700;
  padding: 1rem 1.5rem;
  text-align: center;
  font-size: 1rem;
  border-bottom: 2px solid #90caf9;
  user-select: none;
}

.resource-table tbody tr {
  transition: background-color 0.25s ease;
  cursor: default;
}

.resource-table tbody tr:nth-child(odd) {
  background-color: rgba(187, 222, 251, 0.15);
}

.resource-table tbody tr:hover {
  background-color: rgba(59, 130, 246, 0.15);
}

.resource-table td {
  padding: 1rem 1.5rem;
  text-align: center;
  font-weight: 500;
  font-size: 0.95rem;
  color: #34495e;
  border-bottom: 1px solid #e3f2fd;
  user-select: text;
}

.resource-table tbody tr:last-child td {
  border-bottom: none;
}

/* Charts Section */
.charts-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
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
