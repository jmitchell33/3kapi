async function getAreaData() {
  const response = await fetch("https://129.213.48.136/api/area/");
  const areaData = await response.json();
  console.log(areaData);
}


Smart('#table', class {
  get properties() {
    return {
        dataSource: new Smart.DataAdapter(
      {
        dataSource: getAreaData(),
        dataFields:
        [
          'id: number',
          'name: string',
          'realm: number',
          'dungeon: boolean'
        ]
      }),
      columns: [
        'name',
        'realm',
        'dungeon'
      ]
    }
  }
});

window.onload = function() {
  const table = document.getElementById('table');
  
  table.sortBy('name', 'asc');
}