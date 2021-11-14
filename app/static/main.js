const ctx = document.getElementById("myChart").getContext("2d");
ctx.canvas.width = 2;
ctx.canvas.height = 1;

// async function chartData() {
//   let data = await fetch("/get_data");

//   const chart = new Chart(ctx, {});
// }

const data = {
  labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
  datasets: [
    {
      // data: [1, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 3, 4, 3],
      data: [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 5, 6, 7],//
      tension: 0,
    },
  ],
};

const myChart = new Chart(ctx, {
  type: "line",
  data: data,
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});
