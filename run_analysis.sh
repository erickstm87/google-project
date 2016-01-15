#!/bin/bash

for i in {1..10}
do
    python income.py >> big40rent.csv
done

grep -c "True" big40rent.csv
grep -c "False" big40rent.csv 
