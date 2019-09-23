#!/bin/bash

# Save current directory
CUR_DIR="$(pwd)"

# Switch to template directory
cd "$(dirname "$0")" || exit

# List and copy all project files to given destination
git ls-tree -r HEAD --name-only | tr '\n' '\0' | xargs -0 cp --parents --target-directory "$CUR_DIR"
