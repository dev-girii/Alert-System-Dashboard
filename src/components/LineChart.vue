<template>
  <canvas ref="canvas"></canvas>
</template>

<script>
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default {
  props: ['labels', 'data', 'label', 'color'],
  mounted() {
    new Chart(this.$refs.canvas, {
      type: 'line',
      data: {
        labels: this.labels,
        datasets: [{
          label: this.label,
          data: this.data,
          fill: true,
          backgroundColor: this.color,
          borderColor: this.color.replace('0.5', '1'),
          tension: 0.4
        }]
      },
      options: {
        responsive: true,
        plugins: { legend: { display: true } }
      }
    });
  }
}
</script>
