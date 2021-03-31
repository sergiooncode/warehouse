# Warehouse

To start app, being at the top level of cloned repository:
```
docker-compose -f docker-compose.yml up
```

To run tests (after building on previous step):
```
cd backend
make unit-tests
```

# Infrastructure

- Uses Flask and Flask-RESTX as infrastructure base
- In an MVP version (tagged as mvp in github) an inmemory store is used based on the Flask config
