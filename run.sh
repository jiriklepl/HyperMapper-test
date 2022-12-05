#!/bin/sh

HERE=$(pwd)

if DIR="/tmp/$(uuid)"; then
    mkdir -p "$DIR"
    echo "$DIR"

    {
        cd "$DIR" && {
            ln -s "$HERE/kernels" kernels
            ln -s "$HERE/parameters.json" .
            ln -s "$HERE/parameters2.json" .
            "$HERE/autotuner.py"
        }
    }
fi
