# Game Databaseschema (ERD)

```mermaid
erDiagram
    USERS {
        string email
        string alias
        string password_hash
        int credits
        int level
        int xp
        datetime created_at
    }
    CLUBS {
        string name
        int score
        datetime created_at
    }
    CLUB_MEMBERS {
        int user_id
        int club_id
        datetime joined_at
    }
    SESSIONS {
        int id
        int user_id
        int mission_id
        string status
        int progress
        datetime started_at
        datetime ended_at
    }
    MISSIONS {
        int id
        string title
        string description
        int difficulty
    }
    AI_HISTORY {
        int id
        int user_id
        string prompt
        string response
        datetime timestamp
    }
    CREDIT_TRANSACTIONS {
        int id
        int user_id
        int amount
        string type
        string description
        datetime timestamp
    }
    USERS ||--o{ SESSIONS : has
    USERS ||--o{ AI_HISTORY : interacts
    USERS ||--o{ CREDIT_TRANSACTIONS : earns/spends
    USERS ||--o{ CLUB_MEMBERS : joins
    CLUBS ||--o{ CLUB_MEMBERS : has
    SESSIONS ||--|{ MISSIONS : includes
```
