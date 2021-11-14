const ctx = document.getElementById("myChart").getContext("2d");
ctx.canvas.width = 2;
ctx.canvas.height = 1;

async function loadGraph() {
  const response = await fetch("/get_data");
  const match_data = await response.json();

  let n = match_data.length;
  const labels = Array.from({ length: n }, (_, index) => index + 1);

  const myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          data: match_data,
          tension: 0,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

loadGraph();
