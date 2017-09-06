# Env

It's simple docker container which runs a web service to return JSON of enviromental variables.

## Run
```
docker run -p 5000:5000 -e A=5 radeklos/env
```


```
http localhost:5000
```

```
{
  "env": {
    "A": "5"
  }
}
```
