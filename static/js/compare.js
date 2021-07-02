let away_name = document.getElementById("away_name").innerHTML
let home_score_list = document.getElementsByClassName("home_score")
let away_score_list = document.getElementsByClassName("away_score")
let home_date_list = document.getElementsByClassName("home_date")
let away_date_list = document.getElementsByClassName("away_date")

let home_scores = []
let away_scores = []
let dates = document.getElementsByClassName("timeline")

timeline = []

for (date of dates){
  timeline.push(date.innerHTML)
}

real_home_scores = []
real_home_dates = []

for (checkin of home_date_list){
  real_home_dates.push(checkin.innerHTML)
}

home_dates = []
for (date of real_home_dates){
  day = date.split(" ")
  home_dates.push(Date.UTC(day[0], day[1], day[2]))
}

for (checkin of home_score_list){
  real_home_scores.push(checkin.innerHTML)
}

for (i=0;i<real_home_scores.length;i++){
  home_scores.push([(home_dates[i]), parseFloat(real_home_scores[i])])
}

real_away_scores = []
real_away_dates = []

for (checkin of away_date_list){
  real_away_dates.push(checkin.innerHTML)
}

away_dates = []
for (date of real_away_dates){
  day = date.split(" ")
  away_dates.push(Date.UTC(day[0], day[1], day[2]))
}

for (checkin of away_score_list){
  real_away_scores.push(checkin.innerHTML)
}

for (i=0;i<real_away_scores.length;i++){
  away_scores.push([(away_dates[i]), parseFloat(real_away_scores[i])])
}

document.addEventListener('DOMContentLoaded', function () {
  const chart = Highcharts.chart('charter', {
      chart: {
          type: 'line'
      },
      title: {
          text: 'Daily impact score'
      },
      xAxis: {
        type: 'datetime',
        dateTimeLabelFormats: { // don't display the dummy year
            month: '%e. %b',
        },
        title: {
            text: 'Date'
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