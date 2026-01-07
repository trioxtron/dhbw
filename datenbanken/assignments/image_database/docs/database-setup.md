```
erDiagram
    images {
        int id PK
        varchar filename
        bytea image_data 
        varchar description
    }

    tags {
        int id PK
        varchar name
    }

    image_tags {
        int image_id PK,FK
        int tag_id PK,FK
    }

    images ||--o{ image_tags : ""
    tags ||--o{ image_tags : ""
```
