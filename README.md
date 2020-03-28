## About

`pwd` is a Python tool to create a perfect bash prompt!

### Features:
- Color
- User+hostname if on an external system
- Version control integration
 - Repo name
 - Submodule support
 - Dirty/clean flag
 - Supports: git
- Python virtual environment (limited)

### Examples:

![An example](https://raw.githubusercontent.com/bclarkx2/pwd/master/doc/example1.png)

![Another example](https://raw.githubusercontent.com/bclarkx2/pwd/master/doc/example2.png)


## Installation

Clone the git repo:

`git clone git@github.com:bclarkx2/pwd`


Install using `make`:

`make install`


Add the following line to your `.bashrc` (or other shell configuration files):

`export PROMPT_COMMAND='PS1="$(pwd.py)"`


## Configuration

### Username/hostname
If the current username and hostname are both equal to the respective values in the `MY_USERNAME` and `MY_HOSTNAME` environment variables, the `user@hostname` part of the prompt will be suppressed.
