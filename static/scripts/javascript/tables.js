//trigger AJAX load on selected button clicks;
document.getElementById("area-trigger").addEventListener("click", function(){
  let table = new Tabulator("#data-table", {
    layout:"fitColumns",
    placeholder:"No Data Set",
    columns:[
        {title:"Name", field:"name", sorter:"string", width:200},
        {title:"Realm", field:"realm", sorter:"string"},
    ],
  });

  fetch('https://129.213.48.136/api/area/')
    .then(response => response.json())
    .then(data => {
      const areaData = data.results;
      table.setData(areaData);
    })
    .catch(error => console.error(error));  
});

document.getElementById("monster-trigger").addEventListener("click", function(){
  let table = new Tabulator("#data-table", {
    layout:"fitColumns",
    placeholder:"No Data Set",
    columns:[
        {title:"Name", field:"short", sorter:"string"},
        {title:"Class", field:"size", sorter:"number"},
        {title:"Area", field:"parent_area_name", sorter:"string"},
        {title:"Scaler", field:"scaler", sorter:"number"},
        {title:"Description", field:"description"},
        {title:"Notes", field:"notes", sorter:"string"},
    ],
  });

  fetch('https://129.213.48.136/api/monster/')
    .then(response => response.json())
    .then(data => {
      const areaData = data.results;
      table.setData(areaData);
    })
    .catch(error => console.error(error));  
});

document.getElementById("item-trigger").addEventListener("click", function(){
  let table = new Tabulator("#data-table", {
    layout:"fitColumns",
    placeholder:"No Data Set",
    columns: [        
      {title:"Name", field:"short", sorter:"string"},
      {title:"Area", field:"parent_area_name", sorter:"string"},
      {title:"Mob", field:"parent_monster_name", sorter:"string"},
      {title:"Type", field:"slot", sorter:"string"},
      {title:"Weight", field:"weight", sorter:"string"},
      {title:"Unbreakable", field:"unbreakable", sorter:"bool"},
      {title:"Cursed", field:"cursed", sorter:"bool"},
      {title:"Description", field:"description", sorter:"string"},
      {title: "HP Regen", field: "hp_regen", sorter: "number"},
      {title: "SP Regen", field: "sp_regen", sorter: "number"},
      {title: "HP Drain", field: "hp_drain", sorter: "number"},
      {title: "SP Drain", field: "sp_drain", sorter: "number"},
      {title: "Ftouch?", field: "ftouchable", sorter: "bool"},
      {title: "Transmute", field: "transmutable", sorter: "bool"},
      {title: "Dupe Item", field: "duplicable", sorter: "bool"},
      {title: "BOP", field: "bind_on_pickup", sorter: "bool"},
      {title: "BOE", field: "bind_on_equip", sorter: "bool"},
      {title: "stats_str", field: "stats_str", sorter: "number"},
      {title: "stats_con", field: "stats_con", sorter: "number"},
      {title: "stats_int", field: "stats_int", sorter: "number"},
      {title: "stats_wis", field: "stats_wis", sorter: "number"},
      {title: "stats_dex", field: "stats_dex", sorter: "number"},
      {title: "stats_cha", field: "stats_cha", sorter: "number"},
      {title: "SMD", field: "smd", sorter: "bool"},
      {title: "edged", field: "edged", sorter: "number"},
      {title: "blunt", field: "blunt", sorter: "number"},
      {title: "fire", field: "fire", sorter: "number"},
      {title: "ice", field: "ice", sorter: "number"},
      {title: "acid", field: "acid", sorter: "number"},
      {title: "electricity", field: "electricity", sorter: "number"},
      {title: "mind", field: "mind", sorter: "number"},
      {title: "energy", field: "energy", sorter: "number"},
      {title: "poison", field: "poison", sorter: "number"},
      {title: "radiation", field: "radiation", sorter: "number"},
      {title: "Specials", field: "specials", sorter: "string"},
    ],
  });

  fetch('https://129.213.48.136/api/item/')
    .then(response => response.json())
    .then(data => {
      const areaData = data.results;
      table.setData(areaData);
    })
    .catch(error => console.error(error));  
});


