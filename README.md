# Saqtan REST API
## Installation
```
pip install invoke
inv install
```

## Run uvicorn server
```
    uvicorn main:app --reload
```
Follow link: http://127.0.0.1:8000/docs#/


# CONTRIBUTING
To contribute to the code, suppose you are working on Issue Ticket #34, you’ll need to create a new local branch named “feature/34”

git checkout -b "feature/34"

Now once you have made all changes,
```
inv format (To format all the files according to Python standards)
```
```
inv check (To check formatting once again)
```
```
git add .
```
```
git commit -m "#34 <commit message>"
```
Example: ```git commit -m "#34 Add support for feature X"```
```
git push --set-upstream origin feature/34
```
Now, your changes would have been pushed online to the new branch “feature/34”.

After this, you need to go to your branch online and create a Pull Request to merge the branch “feature/34” with “master”.

Once the Pull Request is approved after code review, you can merge the Pull Request. :-)

## For devs.
Create new app
```
    inv create --app app_name
```

Create new model
```
    inv createModel model_name
```

Create new schema
```
    inv createSchema schema_name
```

Pack all models
```
    inv packmodels
```

Pack all schemas
```
    inv packschemas
```

# Project structure
```
.
├── apps.txt  <- List of created apps(need for inv format)
├── core  <- Configuration of app
│   ├── config.py
│   ├── __init__.py
│   └── logging.py
├── Database  <- All database entities
│   ├── database.py
│   ├── __init__.py
│   ├── models  <- Models
│   │   ├── cache  <- Packed models
│   │   │   ├── __init__.py
│   │   │   └── pack_models.py
│   │   ├── City_code.py
│   │   ├── Crime_count.py
│   │   └── __init__.py
│   └── schemas  <- Schemas
│       ├── cache  <- Packed schemas
│       │   ├── __init__.py
│       │   └── pack_schemas.py
│       ├── City_code.py
│       └── __init__.py
├── Dependencies  <- Dependecies scripts
│   ├── get_db.py
│   └── __init__.py
├── main.py
├── README.md
├── resources
│   ├── __init__.py
│   └── strings.py
├── setup.cfg
├── tasks.py
└── utils  <- Utils for allocate business logic
    ├── City_code_utils.py
    └── __init__.py
```