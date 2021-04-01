# Warehouse

Build the base image:
```
cd backend
make build-base
```

To start the backend app, being at the top level of cloned repository:
```
docker-compose -f docker-compose.yml up
```

To stop the backend app:
```
docker-compose -f docker-compose.yml down
```

It can be tested doing:
- Get all products with current availability

```
curl http://localhost:88/products
```
- Sell a product given its name and number of units to sell

```
curl --header "Content-Type: application/json" --request POST --data '{"product_name":"Dining Chair","units_to_sell":1}' http://localhost:88/products
```

- Get all products and see the availability decreased after previous sale

```
curl http://localhost:88/products
```

To run tests (after building on previous step):
```
cd backend
make test
```

# Infrastructure

- Uses Flask and Flask-RESTX as infrastructure base.
- In an MVP version (tagged as inmemory-mvp in this repo) an inmemory store is used based on the Flask config.
- In an following version (tagged as mongo-as-db in this repo) a MongoDB is used as store for the warehouse entities.
- The frontend app is based on ReactJS and can be considered an quick-and-dirty MVP.

## Considerations

- Although the requirements would make for a fairly straightforward app I used a DDD-like and layered approach
because in my opinion such an approach helps with concern-separation and decoupling.

- The app has 3 layers application - domain - infrastructure. The application handles business logic using
use case services which access data in the persistence to compute/act on what's the goal of the application: get
product availability and remove inventory when products are sold. The domain holds the objects that give place to
the domain which are basically two: canonical products and inventory (a catalogued product consists of certain
articles in specific numbers) and products and inventory that hold current amount of availability and stock
respectively. The infrastructure has what's necessary to handle the low level of the actions performed by the API,
that is, accessing the persisted data and providing controllers to respond to requests.

- Someone could consider that Products and Inventory are two different domains and should be separate but for
simplicity it was chosen to keep them together. As the backend app would keep increasing its complexity for example
when inventory is not only used to check product availability and removing inventory when selling probably it'd
make sense to make Inventory its own backend service which a Products service would send requests to.

- An event sourcing pattern could be used when the inventory is updated. An event defined in advance could be triggered
on an inventory update, this event could be published and other services would be subscribed to these events
and handle the inventory update accordingly on their side. 

- In the mongo-as-db version MongoDB was chosen because being a document-oriented DB fits well with the nature of data
that it's going to store: products and inventory.

- A CONTRIBUTING.md was added to describe the guidelines to follow when contributing to this repo.

## Minor Considerations

- The price was mentioned in the Assignment but it wasn't included in the data files so it was decided to set
to a fixed value of 100 for the only two products.

# Authors

Owner: Sergio Perez <sperez4mba@gmail.com>

