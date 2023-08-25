async function getAreaData() {
  const response = await fetch("https://129.213.48.136/api/area/");
  const areaData = await response.json();
  return areaData.results;
  console.log(areaData.results);
}

function getOrderData() {
  const orderData = [], productNames = ['Wireless Microphone System', 'One for the Blackbird, One for the Crow', 'Ultrean 6 Quart Air Fryer', 'NETGEAR WiFi Range Extender', 'YTD Men\'s Short Sleeve Polo Shirt', 'Sling Bag', 'Kantek Tablet Stand', 'Cuisinart C55CNS-8CFP', 'Panasonic Noise Cancelling Over The Ear Headphones', 'Magid GF18T Pesticide Glove', 'Ink+Ivy Alpine Cotton Duvet Cover', '12 Little Zoo Animals Toy Figure'], productPrices = [47.59, 7.48, 64.59, 29.99, 28.99, 25.49, 17.03, 10.14, 136.88, 7.73, 71.33, 6.99], countryCodes = ['US', 'AE', 'BK', 'CD', 'ld', 'sd', 'sdf', 'wre', 'mkd', 'mksd', 'klps', 'mklsdf'];
  for (let i = 0; i < 30000; i++) {
      const productIndex = Math.floor(Math.random() * productNames.length);
      const order = {
          id:  i,
          productName: productNames[productIndex],
          price: productPrices[productIndex],
          quantity: Math.floor(Math.random() * 8) + 1,
          date: new Date((new Date()).getTime() - Math.floor(Math.random() * 9 + 1) * 86400000),
          country: countryCodes[Math.floor(Math.random() * countryCodes.length)][1].toLowerCase(),
          margin: Math.floor(Math.random() * 4) + 1,
          status: ['Received', 'Confirmed', 'Processing', 'Shipped', 'In transit', 'Delivered'][Math.floor(Math.random() * 6)]
      };
      order.total = parseFloat((order.price * order.quantity).toFixed(2));
      order.profit = parseFloat((((Math.floor(Math.random() * 30) + 9) / 100) * order.total).toFixed(2));
      orderData.push(order);
  }
  return orderData;
}


Smart('#table', class {
  get properties() {
      return {
          dataSource: new window.Smart.DataAdapter({
              dataSource: getAreaData(),
              dataFields: [
                  'id: number',
                  'area: string',
                  'realm: string',
                  'dungeon: bool'
              ]
          }),
          editing: true,
          selection: true,
          keyboardNavigation: true,
          sortMode: 'one',
          columns: [
              { label: 'id', dataField: 'id', dataType: 'number', allowEdit: false },
              { label: 'Area Name', dataField: 'area', dataType: 'string' },
              { label: 'Realm', dataField: 'realm', dataType: 'string', templateElement: '<span>${{value}}</span>' },
              { label: 'Dungeon', dataField: 'dungeon', dataType: 'bool' },
          ]
      };
  }
});

window.onload = function() {
  const table = document.getElementById('table');
}