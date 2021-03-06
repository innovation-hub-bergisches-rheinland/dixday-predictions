# Dixday 

* Output: Integerwert, der "Zustand des Lagers" beschreibt, ausgewertet auf Basis der Temperaturdaten
* Input:

```json
{
    "temperature": 25.0,
    "timestamp": 175546546132,
    ...
}
```

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Usage

Examples for deployment in Docker or Kubernetes can be found in the examples
directory:

- [Docker Compose](examples/docker-compose)
- [Kubernetes](examples/k8s)

## Contributing

The source code of dixday-predictions can be found on
Github:
<https://github.com/innovation-hub-bergisches-rheinland/dixday-predictions/>

We'd love to have you contribute! Please refer to our
[contribution guidelines](CONTRIBUTING.md) for details.

## License

[Apache 2.0 License](LICENSE)

## Local Development

Install [pyenv](https://github.com/pyenv/pyenv) with the
[pyenv installer](https://github.com/pyenv/pyenv-installer), configure your
shell (log out and log back in for changes to take effect):

```shell
# Install pyenv
curl https://pyenv.run | bash
# Configure shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init --path)"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```

Install and activate Python version specified in `.python-version` with pyenv:

```shell
# Install and activate Python version
pyenv install
# Check Python version
pyenv version
```

Install [Poetry](https://python-poetry.org/):

```shell
curl -sSL \
    https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py |
    python
```

Windows Powershell:
```
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

Create project environment, install dependencies and activate the environment in
your shell:

```shell
# Configure Poetry to create environments in project directories (OPTIONAL)
poetry config virtualenvs.in-project true
# Create project environment
poetry env use $(which python)
# Install dependencies
poetry install
# Activate project environment
poetry shell
```

You can build a Docker image locally with:

```shell
./build.sh
```
