## About

`pwd` is a Python tool to create a perfect bash prompt!

### Features:

Supported version control systems: `git`

- VCS: Repo and branch name

![repo-branch-name-example](https://raw.githubusercontent.com/bclarkx2/pwd/media/doc/img/repo_branch_name.png)

- VCS: Remote display

![remote-example](https://raw.githubusercontent.com/bclarkx2/pwd/media/doc/img/remote.png)

- VCS: Dirty flag

![dirty-flag-example](https://raw.githubusercontent.com/bclarkx2/pwd/media/doc/img/dirty_flag.png)

- VCS: Divergence tracking

![divergence-example](https://raw.githubusercontent.com/bclarkx2/pwd/media/doc/img/divergence.png)

- VCS: Submodule support

![submodule-example](https://raw.githubusercontent.com/bclarkx2/pwd/media/doc/img/submodule.png)

- VCS: Detached HEAD warning

![detached-head-example](https://raw.githubusercontent.com/bclarkx2/pwd/media/doc/img/detached_head.png)


- User+hostname if on an external system

![identity-example](https://raw.githubusercontent.com/bclarkx2/pwd/media/doc/img/identity.png)


- Python virtual environment (limited)

![venv-example](https://raw.githubusercontent.com/bclarkx2/pwd/media/doc/img/venv.png)
![missing-venv-example](https://raw.githubusercontent.com/bclarkx2/pwd/media/doc/img/missing_venv.png)


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

## Licensing
This project is released under the MIT license. See [LICENSE.md](LICENSE.md) for details.
