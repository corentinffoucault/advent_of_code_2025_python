# Advent of Code 2025 (Python 3)

Python project for Advent of Code 2025, using Poetry for management.  
The project is organized with an internal library `lib`, exercises in `days`, and an executable `main`.

---

## Project Structure

```
advent_of_code_2025_python/
├── resources  
│   └── dayX.txt
├── src/              
│   └──advent_of_code_2025_python    
│       ├── main.py
│       ├── days/
│       │   ├── ADay.py
│       │   └── dayX/
│       │       └── DayX.py
│       └── lib/
│           └── path_utils.py
├── tests  
│   └──advent_of_code_2025_python     
│       └── days/
│           └── dayX/
│               └── test_dayX.py
└── README.md
```

---

## Prerequisites

- **Python** ≥ 3.14.1
- **Poetry** ≥ 2.2.1

---


## Clone the project
```bash
git clone https://github.com/corentinffoucault/advent_of_code_2025_python.git
cd advent_of_code_2025_python
poetry install
```

## Run

```bash
poetry run python -m advent_of_code_2025_python.main
```

## Test
```bash
poetry run pytest -v tests/
```

---

## Technical Details

- The `lib` directory contains reusable utilities (`path_utils`)
- The `resources` directory contains all input files for each day
- The `days` directory contains all exercises, organized in subdirectories by day
- The `main` executable asks which day to run and uses these libraries to solve Advent of Code 2025 challenges

---