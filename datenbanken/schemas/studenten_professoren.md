```
erDiagram 
    Professor ||--o{ Vorlesung: liest
    Student ||--o{ Matching: hoert
    Vorlesung ||--o{ Matching: wird_gehoert

    Student {
        int Matr_ID PK
        varchar Vorname
        varchar Nachname
    }

    Vorlesung {
        int Vorlesung_ID PK
        int Prof_ID FK
        varchar Name 
    }

    Professor {
        int Prof_ID PK
        varchar Vorname
        varchar Nachname
    }

    Matching {
        int Vorlesung_ID PK, FK
        int Matr_ID PK, FK
    }
```
