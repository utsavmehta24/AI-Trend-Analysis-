AOS.init({ duration: 1000 });

fetch("data/ai_trends_cleaned.csv")
  .then(response => response.text())
  .then(csv => {
    const rows = csv.trim().split("\n").slice(1);

    const labels = [];
    const values = [];

    rows.forEach(row => {
      const [date, interest] = row.split(",");
      labels.push(date);
      values.push(Number(interest));
    });

    const ctx = document.getElementById("trendChart").getContext("2d");

    new Chart(ctx, {
      type: "line",
      data: {
        labels: labels,
        datasets: [{
          label: "AI Search Interest",
          data: values,
          borderColor: "#38bdf8",
          borderWidth: 2,
          tension: 0.4,
          fill: false
        }]
      },
      options: {
        responsive: true,
        animation: {
          duration: 2000
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 100
          }
        }
      }
    });
  });
