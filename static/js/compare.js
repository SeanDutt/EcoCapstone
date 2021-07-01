let away_name = document.getElementById("away_name").innerHTML
let home_score_list = document.getElementsByClassName("home_score")
let away_score_list = document.getElementsByClassName("away_score")

let home_scores = []
let away_scores = []
let dates = document.getElementsByClassName("timeline")

timeline = []

for (date of dates){
  timeline.push(date.innerHTML)
}

for (score of home_score_list){
  home_scores.push(parseFloat(score.innerHTML))
}

for (score of away_score_list){
  away_scores.push(parseFloat(score.innerHTML))
}

console.log(dates)

document.addEventListener('DOMContentLoaded', function () {
  const chart = Highcharts.chart('chart', {
      chart: {
          type: 'line'
      },
      title: {
          text: 'Daily impact score'
      },
      xAxis: {
          categories: timeline
      },
      yAxis: {
          title: {
              text: 'Scores'
          },
          min: 0
      },
      tooltip: {
        headerFormat: '<b>{series.name}</b><br>',
        pointFormat: '{point.x:%e. %b}: {point.y:.2f} m'
      },
      plotOptions: {
        series: {
          marker: {
            enabled: true
          }
        }
      },
      series: [{
          name: 'Your score',
          data: away_scores
      }, {
          name: away_name +'\'s score',
          data: home_scores
      }]
  });
});