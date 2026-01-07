```
erDiagram
    address ||--o{ customer : has
    customer ||--o{ order : orders
    order ||--o{ transaction : belongs
    processing_status ||--o{ order : has

    product ||--o{ transaction : belongs

    customer {
        serial id PK
        varchar firstname
        varchar lastname
        int age
        int address_id FK
    }

    address {
        serial id PK
        varchar city
        int city_code
        varchar street
        int house_number
    }

    product {
        serial id PK
        varchar name
        varchar category
        float single_price
    }

    order {
        serial id PK
        int customer_id FK
        timestamp order_date
        int status_id FK
    }

    processing_status {
        serial id PK
        varchar status_name
        varchar responsible
    }

    transaction {
        serial id PK, FK
        int product_id PK, FK
        int amount
    }
```
