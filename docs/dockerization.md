### overview

- this project use docker compose to declare services, the goal is to run the application in production mode by simply
  running `docker compose up`
- to run the application in dev mode, we should specify the docker compose dev file
  `docker compose -f docker-compose.dev.yml up --build`

### services:

this project contains the following services:

- user-ui: the React front end application
- api: the fastapi backend api
- grafana: the observability center
- prometheus: collect the api metrics

### tips:

- adding the following to the docker compose file fix the permission problem that prevent the stopping of a container, this issue occur on ubuntu

```yml
    security_opt:
      - apparmor:unconfined
```

- use docker watcher in docker compose dev file to auto-reload file changes, this replaces the old method of using volumes.
- docker watcher not enabled at startup, it needs to be enabled manually