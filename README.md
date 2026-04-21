# Calculator App

A simple Python calculator application for demonstrating QA analysis workflows.

## Features

- Basic arithmetic: add, subtract, multiply, divide
- Command-line interface
- Unit tests with pytest

## Project Structure

```
calculator-app/
├── src/calculator/
│   ├── __init__.py
│   ├── operations.py    # Core arithmetic functions
│   └── cli.py           # Command-line entry point
├── tests/
│   └── test_operations.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
cd src
python -m calculator.cli add 2 3      # 5.0
python -m calculator.cli div 10 2     # 5.0
```

## Running Tests

```bash
pytest
```

## Tech Stack

- Python 3.9+
- pytest for testing
