# fix-errors-example

Setup:

- Add an api key to docker.env
- Run `docker compose up`
- In another shell, in the same dir, run `docker compose exec toolbox bash`
- `curl movies-api-py:8000/movies` (not passing a `q` query param will cause an error)
