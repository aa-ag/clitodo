# CLI To-Do app

Creating a To-do app using Python & [Typer](Because the class shows a version of this project with several dependencies, a virtual env was created: `conda activate clitodo`) to be used via CLI following class from [RealPython](https://realpython.com/python-typer-cli/).

In class, the project is broken down into 12 sections, and it's more of an article than a follow along class;  here, you will only find the relevant scripts to make the app run.

Because the class shows a version of this project with several dependencies, a virtual env was created: `conda activate clitodo`

### dependencies

- `conda install -c conda-forge typer`
- `conda install -c conda-forge colorama`
- `conda install -c conda-forge shellingham`
- `conda install -c conda-forge pytest`

### file structure

```
clitodo
├── README.md
├── requirenmets.txt
├── tests
│   ├── __init__.py
│   └── test_todo.py
└── todoapp
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    ├── config.py
    ├── database.py
    └── todo.py
```