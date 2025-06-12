<template>
  <Line :data="chartData" :options="chartOptions" />
</template>

<script>
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js';

import { Line } from 'vue-chartjs';

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
);

export default {
  name: 'LineChart',
  components: { Line },
  props: {
    chartData: Object,
    chartLabel: String,
    color: {
      type: String,
      default: '#2196F3'
    }
  },
  computed: {
    chartOptions() {
      return {
        responsive: true,
        plugins: {
          legend: { position: 'top' },
          title: {
            display: true,
            text: this.chartLabel
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 100
          }
        }
      };
    }
  }
};
</script>
