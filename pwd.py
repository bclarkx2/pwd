#!/usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import os
import hashlib
import sys

from socket import gethostname
from os import path

import subprocess


###############################################################################
# Constants                                                                   #
###############################################################################

# user specific info
MY_USERNAME = os.getenv("MY_USERNAME")
MY_HOSTNAME = os.getenv("MY_HOSTNAME")

# prompt text constants
CURSOR = '$ '
ELLIPSIS = ".."

# colors
RS = r"\[\033[0m\]"     # reset
HC = r"\[\033[1m\]"     # hicolor
UL = r"\[\033[4m\]"     # underline
INV = r"\[\033[7m\]"    # inverse background and foreground
FBLK = r"\[\033[30m\]"  # foreground black
FRED = r"\[\033[31m\]"  # foreground red
FGRN = r"\[\033[32m\]"  # foreground green
FYEL = r"\[\033[33m\]"  # foreground yellow
FBLE = r"\[\033[34m\]"  # foreground blue
FMAG = r"\[\033[35m\]"  # foreground magenta
FCYN = r"\[\033[36m\]"  # foreground cyan
FWHT = r"\[\033[37m\]"  # foreground white
BBLK = r"\[\033[40m\]"  # background black
BRED = r"\[\033[41m\]"  # background red
BGRN = r"\[\033[42m\]"  # background green
BYEL = r"\[\033[43m\]"  # background yellow
BBLE = r"\[\033[44m\]"  # background blue
BMAG = r"\[\033[45m\]"  # background magenta
BCYN = r"\[\033[46m\]"  # background cyan
BWHT = r"\[\033[47m\]"  # background white

vcs_subdirs = [".svn", ".git"]


###############################################################################
# Helper functions                                                            #
###############################################################################

# Retrieval functions

def repo_information(pwd):
    pwd_list = pwd.split("/")

    repos = []
    last_repo = []
    last_vcs_subdir = ""

    for i in range(2, len(pwd_list)+1):
        current_dir = pwd_list[:i]

        # Bail out if pwd is IN the VCS data dir
        if current_dir[-1] in vcs_subdirs:
            return [], [], ""

        vcs_subdir = get_vcs_subdir(current_dir)
        if vcs_subdir:
            last_repo = current_dir
            repos.append(current_dir[-1])
            last_vcs_subdir = vcs_subdir

    repo_str = "->".join(repos)
    repo_path = "/".join(last_repo)

    return repo_str, repo_path, last_vcs_subdir


def get_vcs_subdir(current_dir):
    for vcs_subdir in vcs_subdirs:
        candidate = "/".join([*current_dir, vcs_subdir])
        if path.exists(candidate):
            return vcs_subdir
    return ""


def branch_info(repo_path, vcs_subdir):
    vcs_obj = path.join(repo_path, vcs_subdir)

    if vcs_subdir == ".git":
        return git_branch_info(repo_path, vcs_subdir)
    else:
        return "SVN", ""


def git_branch_info(repo_path, vcs_subdir):
    cmd_output = subprocess.run(
        ["git", "status", "--branch", "--porcelain"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if cmd_output.returncode != 0:
        err = cmd_output.stderr.decode(encoding="utf-8").strip()
        return "NO STATUS", "", f"[{err}]"

    lines = cmd_output.stdout.decode(encoding="utf-8").splitlines()

    status = lines[0][3:]

    if " " in status:
        branches, divergence = status.split(" ", 1)
    else:
        branches, divergence = status, ""

    if "..." in branches:
        local, remote = branches.split("...", 1)
        remote = remote[:remote.find("/")]
    else:
        local, remote = branches, ""

    changes = lines[1:]
    dirty = len(changes) > 0

    if dirty:
        local += "*"

    stash_output = subprocess.check_output(["git", "stash", "list"])
    stash_lines = stash_output.decode(encoding="utf-8").splitlines()
    stashes = len(stash_lines)

    return local, remote, divergence, stashes


def virtual_env(pwd):

    # might be in an activated venv
    if sys.prefix != sys.base_prefix:
        venv_name = os.path.basename(sys.prefix)
        return format_name("|{}|", venv_name, FGRN)

    # might be in a directory that contains a venv
    else:

        pwd = os.path.expanduser(pwd)
        _, subdirs, _ = next(os.walk(pwd))

        for subdir in subdirs:
            f = os.path.join(subdir, "bin", "activate")
            if os.path.isfile(f):
                return format_name("!!{}!!", "ENV", FRED)

        return ""


# Format functions

def format_identity(username, hostname):
    if username != MY_USERNAME or hostname != MY_HOSTNAME:
        return f"{username}@{hostname}:"
    else:
        return ""


def format_pwd(pwd):
    homedir = os.path.expanduser('~')
    return pwd.replace(homedir, '~', 1)


def format_name(fmt, name, color):
    if name:
        return f"{color}{fmt.format(name)}{RS}"
    else:
        return ""

def format_stashes(stashes):
    if stashes:
        return "".join("." * stashes)
    else:
        return ""

###############################################################################
# Main                                                                        #
###############################################################################

def main():

    # Extract data
    try:
        pwd = os.getcwd()
    except OSError:
        pwd = "DNE"

    hostname = gethostname()
    username = os.getenv('USER')
    repo, repo_path, vcs_subdir = repo_information(pwd)
    if repo:
        branch, remote, div, stashes = branch_info(repo_path, vcs_subdir)
    else:
        branch, remote, div, stashes = "", "", "", ""
    virtualenv = virtual_env(pwd)

    # Format pieces for display
    identity = format_identity(username, hostname)
    pwd = format_pwd(pwd)
    repo = format_name("[{}]", repo, FCYN)
    branch = format_name("({})", branch, FMAG)
    remote = format_name("↑{{{}}}", remote, FBLE)
    stash = format_stashes(stashes)

    # Combine into display
    prompt = ''.join([
        os.linesep,
        identity,
        repo,
        FGRN,
		pwd,
		RS,
		remote,
        branch,
        div,
		virtualenv,
        stash,
		os.linesep,
		FYEL,
		CURSOR,
		RS
    ])
    print(prompt)


if __name__ == '__main__':
    main()
