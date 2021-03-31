# Warehouse

To start the backend app, being at the top level of cloned repository:
```
docker-compose -f docker-compose.yml up
```

It can be tested doing:
- Get all products

```
curl http://localhost:88/products
```
- Sell a given product

```
curl --header "Content-Type: application/json" --request POST --data '{"product_name":"Dining Chair","units_to_sell":1}' http://localhost:88/products
```

To run tests (after building on previous step):
```
cd backend
make unit-tests
```

# Infrastructure

- Uses Flask and Flask-RESTX as infrastructure base
- In an MVP version (tagged as inmemory-mvp in github) an inmemory store is used based on the Flask config
