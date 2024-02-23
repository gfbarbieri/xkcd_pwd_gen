# XKCD Password Generator

This project implements a secure password generator inspired by the popular [XKCD Password Generator](https://preshing.com/20110811/xkcd-password-generator/). It combines common words with a few digits to create passwords that are easy to remember but hard to guess. This approach balances memorability and security, making it suitable for generating strong passphrases.

For credit, the original program was written and sent to me by Jeff Barbieri. However, I am responsible for any issues with the code in this repository.

## Features

- Generates passphrases with a mix of common words and random digits.
- Calculates the entropy of generated passphrases to estimate their security level.
- Customizable word count and digit count in the passphrase.

## Installation

To install `xkcd_pwd_gen`, clone this repository and run the setup script:

```bash
git clone https://github.com/gfbarbieri/xkcd_pwd_gen.git
cd xkcd_pwd_gen
python setup.py install
```

## Usage
To generate a passphrase, simply run the main.py script from the command line:

```bash
python src/xkcdpassgen/main.py
```

### Customizing Passphrase Generation
By default, the script generates a passphrase with 4 common words and 2 digits. You can customize the script to change the number of words and digits as per your security needs.

## Development
To set up a development environment, it's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install -e .
```

## Running Tests
This project uses pytest for testing. To run tests, navigate to the project root and execute:

```bash
pytest tests/
```

## Contributing
Contributions to xkcd_pwd_gen are welcome! Please refer to the CONTRIBUTING.md file for guidelines on how to contribute to this project.

## License
This project is licensed under the MIT License - see the [LICENSE](/LICENSE.txt) file for details.