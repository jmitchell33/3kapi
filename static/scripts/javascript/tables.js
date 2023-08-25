async function getAreaData() {
  const response = await fetch("https://129.213.48.136/api/area/");
  const areaData = await response.json();
  return areaData.results;
}

window.Smart('#table', class {
  get properties() {
      return {
          dataSource: new window.Smart.DataAdapter({
              dataSource: getAreaData(),
              dataSourceType: 'json',
              dataFields: [
                  'area: string',
                  'realm: string'
              ]
          }),
          editing: true,
          selection: true,
          keyboardNavigation: true,
          sortMode: 'one',
          columns: [
              { label: 'Area', dataField: 'area', dataType: 'string', allowEdit: false },
              { label: 'Realm', dataField: 'realm', dataType: 'string' },
          ]
      };
  }
});