#!/bin/sh

DIR=$(dirname $0)

python3 -m gomoengine ../moves.txt > play.txt
mv play.txt ..
