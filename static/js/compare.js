let home_score_list = document.getElementsByClassName("home_score")
let home_date_list = document.getElementsByClassName("home_date")

let away_name = document.getElementById("away_name").innerHTML
let away_score_list = document.getElementsByClassName("away_score")
let away_date_list = document.getElementsByClassName("away_date")

let home_dates = []
let home_scores = []
let away_dates = []
let away_scores = []
let dates = []
if(home_dates.length > away_dates.length){
  dates = home_dates
} else {
  dates = away_dates
}

for (score of home_score_list){
  home_scores.push(parseFloat(score.innerHTML))
}

for (date of home_date_list){
  home_dates.push(date.innerHTML)
}

for (score of away_score_list){
  away_scores.push(parseFloat(score.innerHTML))
}

for (date of away_date_list){
  away_dates.push(date.innerHTML)
}

document.addEventListener('DOMContentLoaded', function () {
  const chart = Highcharts.chart('chart', {
      chart: {
          type: 'line'
      },
      title: {
          text: 'Daily impact score'
      },
      xAxis: {
          categories: dates
      },
      yAxis: {
          title: {
              text: 'Scores'
          }
      },
      series: [{
          name: 'Your score',
          data: home_scores
      }, {
          name: away_name +'\'s score',
          data: away_scores
      }]
  });
});