import './App.css';
import { Component } from 'react';
import Client from './apiClient';

class App extends Component {
  state = {
    products: [],
    error: "",
    units: "",
    productName: ""
  };

  componentDidMount() {
    Client.getProducts(products => {
      this.setState({products: products})
    });
  };

  onSellButtonClick = (event) => {
    event.preventDefault();
    const { units, productName } = this.state;
    const values = {
      units: units,
      productName: productName
    };
    Client.sellProduct(values, err => {
      this.setState({error: err})
    });
    Client.getProducts(products => {
      this.setState({products: products})
    });
  };

  handleUnitsChange = (event) => {
    this.setState({ units: event.target.value })
  };

  handleProductNameChange = (event) => {
    this.setState({ productName: event.target.value })
  };

  render() {
    const { products } = this.state;
    const { error } = this.state;
    const productRows = products.map((product, idx) => (
      <tr key={idx}>
        <td>{Object.keys(product)[0]}</td>
        <td>{product[Object.keys(product)[0]].availability_in_units}</td>
        <td>{product[Object.keys(product)[0]].price}</td>
      </tr>
    ));

    return (
      <div className="App">
        <h1>Warehouse App</h1>
        <h4>Product Availability</h4>
        <table className="Products">
          <thead>
            <tr>
              <th>Product Name</th>
              <th>Availability in Units</th>
              <th>Price</th>
            </tr>
          </thead>
          <tbody>
            {productRows}
          </tbody>
        </table>
        <h4>Sell Product</h4>
        <div>
          <form>
            <div>
              <p>Number of units</p>
              <input type="text" className="UnitsTextBox" onChange={this.handleUnitsChange} />
              <p>Product name</p>
              <input type="text" className="ProductTextBox" onChange={this.handleProductNameChange} />
            </div>
            <div className="ButtonBox">
              <button onClick={this.onSellButtonClick}>
                Sell
              </button>
            </div>
            <div className="ErrorBox">
              <p className="ErrorStartLine">Order Status:</p>
              <p className="ErrorText">{error.message}</p>
            </div>
          </form>
        </div>
      </div>
    )
  }
}

export default App;
