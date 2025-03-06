# data-engineering-test-feiHuang
This repository creates a data pipeline that processes a dataset, applies transformations, and loads it into a mock data warehouse

## Dataset Info:
    - Warehouse and Retail Sales dataset: https://catalog.data.gov/dataset/warehouse-and-retail-sales
    - A CSV file derived from the link would be placed in the "data" directory for pipeline processing.

## Design Desisions
- **Pandas** is use for data manipulation
- **Validation** basic checks for missing or invalid values in critical columns
- **Testing** Pythons "unittest" framework to ensure data calidation and transformation working correct
