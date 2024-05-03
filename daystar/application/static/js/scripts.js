// sidebar toggle

var sidebarOpen = false;
var sidebar = document.getElementById("sidebar");

function openSidebar() {
    if(sidebarOpen) {
        sidebar.classList.add("sidebar-responsive");
        sidebarOpen = true;
    }
}

function closeSidebar() {
    if(sidebarOpen) {
        sidebar.classList.remove("sidebar-responsive");
        sidebarOpen = false;
    }
}






// ......................apex barchart
var barChatOptions = {
    series: [{
    data: [400, 430, 448, 470],
    name:"inventory"
  }],
    chart: {
    type: 'bar',
    background:"transparent",
    height: 350,
    toolbar: {
      show: false,
    },
  },
  colors: [
    "#2962ff",
    "#d50000",
    "#2e7d32",
    "#ff6d00",
    "#583cb3",

  ],
  plotOptions: {
    bar: {
      borderRadius: 4,
      borderRadiusApplication: 'end',
      horizontal: true,
    }
  },
  dataLabels: {
    enabled: false
  },
  xaxis: {
    categories: ['Dolls', 'milk', 'daipers ', 'fruits', 'sugar'
    ],
    title: {
        style: {
            color: "#f5f7ff",

        },
    },
    axisBorder: {
        show: true,
        color: "#55596e",
    }
  }
  };

  var chart = new ApexCharts(document.querySelector("#bar-chart"), options);
  chart.render();






