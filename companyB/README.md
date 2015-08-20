# Readme

A standard Django application for factual client test
 
Find stragegy:

-  find geo of the location -> 
-  search (default distance 5000 meters and limit is 5)


Recommend stragegy:

-  merge all likes, dislikes and requirements ->
-  remove common items in likes and dislikes from likes set ->
-  find geo of the location -> 
-  starts from most liked ones ->
-  filter from restaurants-au (default distance 5000 meters and limit is 5)

not sure if the `seating_outdoor` parameter is needed

# Requirements

## Install

```shell
sudo pip install django
sudo pip install factual-api
export FACTUAL_KEY=xxxxxx
export FACTUAL_SECRET=xxxxxx
```

## Tests

```shell
python manage.py test api
```
