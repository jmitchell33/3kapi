
async function getAreaData() {
  const response = await fetch("https://129.213.48.136/api/area/");
  const areaData = await response.json();
  return areaData.results;
}

const apiAreaData = getAreaData();

console.log('data is', apiAreaData);


//Build Tabulator
let table = new Tabulator("#example-table", {
  layout:"fitColumns",
  placeholder:"No Data Set",
  columns:[
      {title:"Name", field:"name", sorter:"string", width:200},
      {title:"Realm", field:"realm", sorter:"string"},
  ],
});


//trigger AJAX load on "Load Data via AJAX" button click
document.getElementById("area-trigger").addEventListener("click", function(){
  table.setData("https://129.213.48.136/api/area/");
});