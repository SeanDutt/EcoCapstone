let userScore = document.getElementsByClassName("userScore")
let userDate = document.getElementsByClassName("userDate")

let userScores = []
let userDates = []

for (checkin of userScore){
    userScores.push(parseFloat(checkin.innerHTML))
  }
  
  for (date of userDate){
    userDates.push(date.innerHTML)
  }


let contScore = document.getElementsByClassName("contScore")
let contUser = document.getElementsByClassName("contProfile")

let contScores = []
let contUsers = []

for (checkin of contScore){
    contScores.push(parseFloat(checkin.innerHTML))
  }
  
  for (date of contUser){
    contUsers.push(date.innerHTML)
  }


let zipScore = document.getElementsByClassName("zipScore")
let zipUser = document.getElementsByClassName("zipProfile")

let zipScores = []
let zipUsers = []

for (checkin of zipScore){
    zipScores.push(parseFloat(checkin.innerHTML))
  }
  
  for (date of zipUser){
    zipUsers.push(date.innerHTML)
  }


let incomeScore = document.getElementsByClassName("incomeScore")
let incomeUser = document.getElementsByClassName("incomeProfile")

let incomeScores = []
let incomeUsers = []

for (checkin of incomeScore){
    incomeScores.push(parseFloat(checkin.innerHTML))
  }
  
  for (date of incomeUser){
    incomeUsers.push(date.innerHTML)
  }



let all = document.getElementById("all")
let last7 = document.getElementById("last-7")
let last28 = document.getElementById("last-28")
let contchart = document.getElementById("cont")
let zipchart = document.getElementById("zip")
let incochart = document.getElementById("income")

all.addEventListener("click", function(){
    let chart = document.getElementById("allcheckins")
    let hide1 = document.getElementById("last7")
    let hide2 = document.getElementById("last28")
    chart.style.visibility = "visible"
    hide1.style.visibility = "hidden"
    hide2.style.visibility = "hidden"
})

last7.addEventListener("click", function(){
    let hide1 = document.getElementById("allcheckins")
    let chart = document.getElementById("last7")
    let hide2 = document.getElementById("last28")
    chart.style.visibility = "visible"
    hide1.style.visibility = "hidden"
    hide2.style.visibility = "hidden"
})

last28.addEventListener("click", function(){
    let hide1 = document.getElementById("allcheckins")
    let chart = document.getElementById("last28")
    let hide2 = document.getElementById("last7")
    chart.style.visibility = "visible"
    hide1.style.visibility = "hidden"
    hide2.style.visibility = "hidden"
})

contchart.addEventListener("click", function(){
    let hide1 = document.getElementById("zipchart")
    let chart = document.getElementById("continentchart")
    let hide2 = document.getElementById("incomechart")
    chart.style.visibility = "visible"
    hide1.style.visibility = "hidden"
    hide2.style.visibility = "hidden"
})

zipchart.addEventListener("click", function(){
    let hide1 = document.getElementById("continentchart")
    let chart = document.getElementById("zipchart")
    let hide2 = document.getElementById("incomechart")
    chart.style.visibility = "visible"
    hide1.style.visibility = "hidden"
    hide2.style.visibility = "hidden"
})

incochart.addEventListener("click", function(){
    let hide1 = document.getElementById("continentchart")
    let chart = document.getElementById("incomechart")
    let hide2 = document.getElementById("zipchart")
    chart.style.visibility = "visible"
    hide1.style.visibility = "hidden"
    hide2.style.visibility = "hidden"
})

document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('allcheckins', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Your impact scores'
        },
        xAxis: {
            categories: userDates,
        },
        yAxis: {
            title: {
                text: 'Scores'
            }
        },
        series: [{
        name: 'Daily score',
        data: userScores,
        }]
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('last7', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Your impact scores'
        },
        xAxis: {
            categories: userDates.slice(-7),
        },
        yAxis: {
            title: {
                text: 'Scores'
            }
        },
        series: [{
        name: 'Daily score',
        data: userScores.slice(-7),
        }]
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('last28', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Your impact scores'
        },
        xAxis: {
            categories: userDates.slice(-28),
        },
        yAxis: {
            title: {
                text: 'Scores'
            }
        },
        series: [{
        name: 'Daily score',
        data: userScores.slice(-28),
        }]
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('continentchart', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Your continent today'
        },
        xAxis: {
            categories: contUsers,
        },
        yAxis: {
            title: {
                text: 'Score'
            }
        },
        series: [{
            name: '',
            data: contScores,
        }]
    });
  });

  document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('zipchart', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Your zip today'
        },
        xAxis: {
            categories: zipUsers,
        },
        yAxis: {
            title: {
                text: 'Score'
            }
        },
        series: [{
            name: '',
            data: zipScores,
        }]
    });
  });

  document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart('incomechart', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Your income today'
        },
        xAxis: {
            categories: incomeUsers,
        },
        yAxis: {
            title: {
                text: 'Score'
            }
        },
        series: [{
            name: '',
            data: incomeScores,
        }]
    });
  });