<template>
  <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
</template>

<script>
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale } from "chart.js";
import { Bar } from "vue-chartjs";

ChartJS.register(BarElement, CategoryScale, LinearScale);

export default {
  name: "WeeklySessionsChart",
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: ["Friday", "Saturday", "Sunday", "Monday", "Tuesday"],

        datasets: [{ data: [60, 15, 0, 90, 60], backgroundColor: "#9879F2" }],
      },
      chartOptions: {
        responsive: true,
      },
    };
  },
};
</script>
