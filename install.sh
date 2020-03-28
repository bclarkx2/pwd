#!/usr/bin/env bash 

script="pwd.py"

source_dir="$(realpath $(dirname $0))"
source_script="$source_dir/$script"

install_dir="${1:-$HOME/.local/bin}"
install_script="$install_dir/$script"

# Ensure source exists
if [ -f "$source_script" ]; then

	# Ensure target exists
	mkdir -p "$install_dir"
	
	# Create symlink
	ln -s "$source_script" "$install_script"

	# Report
	echo "Created symlink: $install_script"
else
	echo "Ensure $script exists in this directory" 1>&2
fi

