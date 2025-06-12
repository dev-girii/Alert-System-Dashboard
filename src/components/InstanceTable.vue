<template>
    <div class="instanceTable">
        <h2>Hosts Table</h2>
            <!-- <h2 class="host-title">🖥️ Instance: {{ host.name }}</h2> -->
    <div class="resource-table">
      <table>
        <thead>
          <tr>
            <th>Role</th>
            <th>CPU (%)</th>
            <th>Mem(GB)</th>
            <th>Disk (GB)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="host in tenderHosts" :key="host.role">
            <td>{{ host.role }}</td>
            <td>{{ host.cpu_idle }}</td>
            <td>{{ host.mem_used_percent }}</td>
            <td>{{ host.disk_used_percent }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    </div>
</template>
<script>
export default{
    props: ['tender'],
    computed: {
  tenderHosts() {
    return this.$store.state.hosts.hosts.filter(h => h.instance === this.tender);
  }
},
mounted() {
  console.log('All hosts:', this.$store.state.hosts.hosts);
  console.log('Tender name:', this.tender);
  console.log('Filtered hosts for tender:', this.tenderHosts);
}
}
</script>
<style scoped>

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
</style>