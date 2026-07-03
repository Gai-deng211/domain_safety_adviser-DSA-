quick progress update; - these concepts are locked in so far;
1. postgresql - contention strings, queries, rbac, optimization(explain-analyze)
2. sqlalchemy - models - bases, create_engine, psycopg2,
3. webscrapping - playwright, web dev tools
4. pydantic - validation
5. alembic migrations (high level understanding):
- You define the models/tables
- alembic init alembic -> alembic/ + .ini file
- configure the env.py by importing your models and db_url
- alembic revision --autogenerate -m "message"
- alembic migrations
- alembic upgrade head --> get the changes into the database

6. ci.yml/docker -> getting comportable but more practice needed. But the idea is building quickly
7. DSA -> revisited the linked lists : singly, doubly, circular, insert/delete/update/reverse/traversal -> still shaky on reverse!
8. fastapi router API
9. whois-lookup (done)
10. pytest

Remaining 
---
1. html response/templates
2. redis
3. hashing
4. sessions/tokens

---
please geneate a .md of this progress update and also tell me what I should do next

