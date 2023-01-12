#!/bin/bash

# activate anly521 virtual environment
source activate anly521

echo "Running zipf.py"
python scripts/zipf.py --path ./data/TheLongPatrol.txt
