<template>
  <div class="stats-panel">
    <MetricBox title="CPU Usage" :value="cpu" />
    <MetricBox title="Memory Usage" :value="memory" />
    <MetricBox title="Disk Usage" :value="disk" />
  </div>
</template>

<script>
import MetricBox from './MetricBox.vue';

export default {
  components: { MetricBox },
  props: ['cpu', 'memory', 'disk']
};
</script>

<style scoped>
.stats-panel {
  display: flex;
  gap: 1rem;
  padding: 1rem;
}
</style>
