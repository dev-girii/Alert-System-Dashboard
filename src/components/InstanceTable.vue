<template>
    <div class="instanceTable">
        <!-- <h2>Nodes: </h2> -->
            <!-- <h2 class="host-title">🖥️ Instance: {{ host.name }}</h2> -->
    <div class="resource-table">
      <table>
        <thead>
          <tr>
            <th>ROLE</th>
            <th>IP</th>
            <th>CPU</th>
            <th>MEM</th>
            <th>DISK</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="host in tenderHosts" :key="host.role">
            <td>{{ host.role }} </td>
            <td>{{ host.ip }}</td>
            <td>{{ parseFloat(host.cpu_idle).toFixed(1) }}%</td>
            <td>{{ parseFloat(host.mem_used_percent).toFixed(1) }}%</td>
            <td v-if="host.disks && host.disks.length">
               <span class="disk_path">
    <span
      v-for="(disk, index) in host.disks"
      :key="index"
      style="margin-right: 10px;"
    >
      {{ disk.path || disk.device }}
      <span class="metric-value status-green">
        {{
          disk.used_percent != null
            ? parseFloat(disk.used_percent).toFixed(1)
            : 'N/A'
        }}%
      </span>
      <br/>
    </span>
  </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    </div>
</template>
<script>
export default{
  props: {
    tender: {
      type: String,
      default: null
    },
    data: {
      type: Array,
      default: () => []
  }
  },
  computed: {
    tenderHosts() {
      if (this.data.length > 0) {
        return this.data;
      }

      // Fallback: when no data prop is passed, filter from store
      return this.$store.state.hosts.hosts.filter(
        (h) =>
          h.instance?.trim().toLowerCase() ===
          this.tender?.trim().toLowerCase()
      );
    }
  },
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

.resource-table{
  padding-top: 0.6rem;
}
/* Table Styling */
.resource-table table {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 0;
  margin-bottom: 2rem;
  background: #fff;
  border: 1px solid;
  /* border-radius: 12px; */
  overflow: hidden;
  /* box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); */
  font-variant-numeric: tabular-nums;
}

.resource-table thead tr {
  background: #f0f2fa;
  color: #0d3b66;
}

.resource-table th {
  font-weight: 700;
  padding: 1rem 1.5rem;
  text-align: center;
  font-size: 1rem;
  border: 1px solid;
  /* border-bottom: 2px solid #90caf9; */
  user-select: none;
}

.resource-table tbody tr {
  transition: background-color 0.25s ease;
  cursor: default;
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
  border: 1px solid;
  user-select: text;
}

.resource-table tbody tr:last-child td {
  border-bottom: none;
}
</style>