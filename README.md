# cloud_play

## Index
- [Description](#description)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [How to execute the project](#how-to-execute-the-project)
- [How to execute the Unit tests](#how-to-execute-the-unit-tests)

### Description
Improving the familiarity with GCP and implementing code following the industry standard.\
In this project there will have 3 main function:
- [`table_exists()`](cloud_play/table_exists.py) that checks if a table exists;
- [`file_finder()`](cloud_play/file_finder.py) that checks if a file exists in the storage and at what path;
- [`dag_exists()`](cloud_play/dag_exists.py) that checks if a DAG is present in the Composer configuration.

### Architecture
The architecture is quite simple: the python function will call needed api.
![alt text](resource/architecture_image.png)
(TODO)Look how beautiful the storage function is
![alt text](resource/file_finder_image.png)
(TODO)
![alt text](resource/table_finder_image.png)
(TODO)
![alt text](resource/class_image.png)

### Requirements (TODO)
a machine that runs staff and poetry (fingers could be needed)\
Run `poetry install`

### How to execute the project

To execute the code:
```bash
poetry run script

```

### How to execute the Unit tests
To execute the test:

```bash
poetry run pytest
```