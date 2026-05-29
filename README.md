#### commands for development

```sh
# run docker compose for development
docker compose -f docker-compose.dev.yml up --build 
```
```sh
# stop containers
docker compose -f docker-compose.dev.yml down
```
```sh
# list containers
docker ps
```
```sh
# attach to a container
docker attach "container_id"
```
```sh
# open bash for api service
docker compose exec -it api bash
```
```sh
# open bash for ui service
docker compose exec -it ui sh
```