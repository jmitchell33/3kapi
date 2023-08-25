import {TabulatorFull as Tabulator} from 'tabulator-tables';

async function getAreaData() {
  const response = await fetch("https://129.213.48.136/api/area/");
  const areaData = await response.json();
  return areaData.results;
}

//Build Tabulator
let table = new Tabulator("#example-table", {
  layout:"fitColumns",
  placeholder:"No Data Set",
  columns:[
      {title:"Name", field:"name", sorter:"string", width:200},
      {title:"Realm", field:"realm", sorter:"string"},
  ],
  data: getAreaData()
});