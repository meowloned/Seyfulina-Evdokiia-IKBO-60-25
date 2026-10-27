#!/bin/sh

cd "$(dirname "$0")/.." || exit 1

./run.sh --vfs vfs_examples/demo
