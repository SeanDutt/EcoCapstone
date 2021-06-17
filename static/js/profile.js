let checkinList = document.getElementsByClassName("score")
let dateList = document.getElementsByClassName("date")

let dates = []
let scores = []
for (checkin of checkinList){
  scores.push(parseFloat(checkin.innerHTML))
}

for (date of dateList){
  dates.push(date.innerHTML)
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
          categories: dates,
      },
      yAxis: {
          title: {
              text: 'Scores'
          }
      },
      series: [{
          name: 'Daily score',
          data: scores,
      }]
  });
});
