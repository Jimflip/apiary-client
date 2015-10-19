Apiary Unofficial CLI Client for Python
=======================================

This is a clone of the Ruby Apiary Client and is only a * PARTIAL * implementation.
Currently it only allows using the preview command to output to file.
This is sufficient to allow a Apiary rendering of the markdown to HTML.
Note that this makes API calls to Apiary and the final HTML is very dependent on the Apiary service being responsive.

[Apiary](https://apiary.io) CLI client, `apiary`.


## Description

The Apiary CLI Client gem is a command line tool for developing and previewing
[API Blueprint](http://apiblueprint.org) documents locally. It can also be
used for pushing updated documents to and fetching existing documents from
[Apiary](http://apiary.io).


Please see the `apiary help` command and the [full documentation](http://client.apiary.io) for an in-depth look in how to use this tool.

For instructions on making your  own changes, see [Hacking Apiary CLI Client](#hacking-apiary-cli-client), below.

## Installation

### Install as a Python pip

``` sh
pip install apiary
```

### Setup Apiary credentials

*Required only for publish and fetch commands.*


1. Make sure you are a registered user of [Apiary](http://apiary.io).
2. Retrieve API key (token) on [this page](https://login.apiary.io/tokens).
3. Export it as an environment variable:

```sh
export APIARY_API_KEY=<your_token>
```
## Command-line Usage

```
$ apiary help
Commands:
  apiary fetch --api-name=API_NAME    # Fetch apiary.apib from API_NAME.apiary.io
  apiary help [COMMAND]               # Describe available commands or one specific command
  apiary preview                      # Show API documentation in default browser
  apiary publish --api-name=API_NAME  # Publish apiary.apib on docs.API_NAME.apiary.io
  apiary version                      # Show version

```

### Details

#### fetch

```
$ apiary help fetch
Usage:
  apiary fetch --api-name=API_NAME

Options:
  --api-name=API_NAME  
  [--api-host=HOST]    # Specify apiary host
  [--output=FILE]      # Write apiary.apib into specified file

Fetch apiary.apib from API_NAME.apiary.io
```

#### preview

```
$ apiary help preview
Usage:
  apiary preview

Options:
  [--browser=chrome|safari|firefox]  # Show API documentation in specified browser
                                     # Possible values: chrome, safari, firefox
  [--output=FILE]                    # Write generated HTML into specified file
  [--path=PATH]                      # Specify path to blueprint file
                                     # Default: apiary.apib
  [--api-host=HOST]                  # Specify apiary host
  [--server], [--no-server]          # Start standalone web server on port 8080
  [--port=PORT]                      # Set port for --server option

Show API documentation in default browser
```

#### publish

```
$ apiary help publish
Usage:
  apiary publish --api-name=API_NAME

Options:
  [--message=COMMIT_MESSAGE]  # Publish with custom commit message
  [--path=PATH]               # Specify path to blueprint file
                              # Default: apiary.apib
  [--api-host=HOST]           # Specify apiary host
  --api-name=API_NAME         

Publish apiary.apib on docs.API_NAME.apiary.io
```

#### version

```
$ apiary help version
Usage:
  apiary version

Options:
  [--{:aliases=>"-v"}={:ALIASES=>"-V"}]  

Show version
```

## Hacking Apiary CLI Client

### Build

1.  If needed, install bundler:

    ```sh
    $ gem install bundler
    ```

2.  Clone the repo:

    ```sh
    $ git clone git@github.com:Jimflip/apiary-client.git
    $ cd apiary-client
    ```

3.  Install dependencies:

    ```sh
    $ pip install -r requirements.txt
    ```

### Test

Inside the `apiary-client` repository directory run:

```sh
$ make test
$ make behave
```

## License

Released under MIT license.
