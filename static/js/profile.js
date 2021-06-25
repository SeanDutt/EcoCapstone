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


document.addEventListener('DOMContentLoaded', function () {
  const chart = Highcharts.chart('chart0', {
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
    const chart = Highcharts.chart('chart1', {
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
    const chart = Highcharts.chart('chart2', {
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
    const chart = Highcharts.chart('chart3', {
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