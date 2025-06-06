<template>
  <div class="metric-box">
    <h4>{{ title }}</h4>
    <p>{{ value }}</p>
  </div>
</template>

<script>
export default {
  props: ['title', 'value']
};
</script>

<style scoped>
.metric-box {
  padding: 1rem;
  background: #ecf0f1;
  border-radius: 8px;
  margin: 0.5rem;
}
</style>
