let obj;
let container = document.getElementById("container")

function AddCounter(id){
  let li = document.createElement("li");
  let label = document.createElement("label")
  let addBtn = document.createElement("h2")
  let subBtn = document.createElement("h2")
  let qtyBox = document.createElement("input")

  label.innerHTML = obj[id]["item"] + "<br>" + obj[id]["co2PerUnit"] + " kgs of CO2/serving";;
  qtyBox.name = obj[id]["item"]
  qtyBox.value = 0
  qtyBox.id = "qtyBox"+id
  subBtn.innerText = "-"
  subBtn.id = "sub"+id
  addBtn.innerText = "+"
  addBtn.id = "add"+id

  addBtn.addEventListener("click", ()=>{
    qtyBox.value = parseInt(qtyBox.value) + 1
  })
  subBtn.addEventListener("click", ()=>{
    if(qtyBox.value > 0){
      qtyBox.value = parseInt(qtyBox.value) - 1
      }
  })

  li.append(label, subBtn, qtyBox, addBtn);
  return li
}

fetch('http://127.0.0.1:8000/api/impacts/')
  .then(response => response.json())
  .then(data => obj = data)
  .then(() => {
    for(i=0;i<obj.length;i++){
      container.prepend(AddCounter(i));
  }})