#!/bin/bash

set -e

REPO_DIR="/root/AirBnB_clone"
AUTHORS_FILE="$REPO_DIR/AUTHORS"

{
    echo "# This is the list of names of the contributors of the project"
    echo
    git -C "$REPO_DIR" log --format='%aN <%aE>' | sort -uf
} > "$AUTHORS_FILE"
