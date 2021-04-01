/* eslint-disable no-undef */
const PRODUCTS_API_URL = 'http://localhost:88/products';

function getProducts(cb) {
    return fetch(PRODUCTS_API_URL, {
      accept: "application/json"
    })
      .then(checkStatus)
      .then(parseJSON)
      .then(cb);
  }

function sellProduct(values, cb) {
  return fetch(PRODUCTS_API_URL, {
      method: "POST",
      body: JSON.stringify( { product_name: values.productName,
        units_to_sell: parseInt(values.units)} ),
      headers: {
        'Content-Type': 'application/json'
      },
  })
    .then((res) => res.json())
    .then((data) => data)
    .catch((err) => {throw err})
    .then(cb);
}
  
function checkStatus(response) {
  if (response.status >= 200 && response.status < 300) {
    return response;
  }
  const error = new Error(`HTTP Error ${response.statusText}`);
  error.status = response.statusText;
  error.response = response;
  //console.log(error); // eslint-disable-line no-console
  throw error;
}

function parseJSON(response) {
  return response.json();
}

const Client = { getProducts, sellProduct };
export default Client;
  