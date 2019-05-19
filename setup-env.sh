#!/bin/sh
mkdir -p $HOME/.pythonvenv
python3 -m venv $HOME/.pythonvenv/azurebloboperations
source $HOME/.pythonvenv/azurebloboperations/bin/activate
export PATH="$HOME/.pythonvenv/azurebloboperations/bin:$PATH"
export PYTHONDONTWRITEBYTECODE=1