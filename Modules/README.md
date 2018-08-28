# IOTA TANGLE SIMULATION

This is a single- and multi-agent simulation of the IOTA Tangle, as described in the white-paper.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The code is run and tested with Python 3.6.3 on macOS 10.12.6.
Create a virtual environment for Python 3 with:

```
virtualenv -p python3 envname
```

### Installing packages

The used Python libraries/packages can be installed with:

```
make
```

or alternatively with:

```
pip install -r requirements.txt
```

## Running the tests

The Python unittest module is used for testing.
Run the tests with:

```
python -m unittest discover
```

## Running the simulation

Run the simulation with:

```
python core.py
```

In this file you can also change the configurations of the simulation.

## Authors

* Manuel Zander

## License

## Acknowledgments
