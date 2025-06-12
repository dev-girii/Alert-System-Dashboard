<template>
  <div class="inventory-container">
    <h2>Inventory Overview</h2>

<div v-if="Object.keys(groupedInstances).length">
  <div
    v-for="(roles, instance) in groupedInstances"
    :key="instance"
    class="instance-section"
  >
    <h3>{{ instance }}</h3>
    <InstanceTable :tender="instance" :data="roles"/>
  </div>
</div>
<div v-else>
  <p>Loading instance data...</p>
</div>

  </div>
</template>

<script>
import InstanceTable from '@/components/InstanceTable.vue';

export default {
  name: 'ViewInventory',
  components: { InstanceTable },
  computed: {
    groupedInstances() {
      const allHosts = this.$store.state.hosts.hosts;
      console.log(allHosts);
      const grouped = {};
      allHosts.forEach((host) => {
        if (!grouped[host.instance]) {
          grouped[host.instance] = [];
        }
        grouped[host.instance].push(host);
      });
      console.log(grouped);
      return grouped;
    }
  }
};
</script>

<style scoped>
.inventory-container {
  padding: 2rem;
}

.instance-section {
  margin-bottom: 3rem;
  background: #f9f9f9;
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.instance-section h3 {
  font-size: 1.4rem;
  margin-bottom: 1rem;
  font-weight: 600;
  color: #333;
}
</style>