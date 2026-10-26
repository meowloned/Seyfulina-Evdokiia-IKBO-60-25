#!/bin/sh

cd "$(dirname "$0")/.." || exit 1

./run.sh --vfs "./scripts" --log "./log.csv" \
    --script "./scripts/startup.txt"
