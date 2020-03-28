#!/usr/bin/env bash 

script="pwd.py"

install_dir="${1:-$HOME/.local/bin}"
install_script="$install_dir/$script"

if [ -L "$install_script" ]; then
	rm "$install_script"
	echo "Removed symlink: $install_script"
fi

