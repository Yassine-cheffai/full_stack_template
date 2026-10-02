### stack
- this application use the following tools:
    - `fastapi` to expose a http server
    - `sqlalchemy` as an ORM to interact easly with the database
    - `alembic` to manage the evolution/migration of the database
    - `prometheus` to collect logs
    - `grafana` observabily dashboard

### alembic usefull commands:
```bash
# Generate a migration by comparing models to the DB
alembic revision --autogenerate -m "create users table"

# Review the generated file in alembic/versions/ before applying!

# Apply it
alembic upgrade head

alembic current            # show current revision
alembic history            # list migrations
alembic downgrade -1       # roll back one step
alembic upgrade head       # apply everything

```
- when starting the development without alembic, we may use the following:
```python
from db.schema import Base, engine
# Delete this
Base.metadata.create_all(bind=engine)
```
- delete it once you start using alembic, because alembic will own the schema and make the updates on the DB



### notes
#### unit testing:
- pytest use pytest.ini to load confs, example what is the root path