#!/usr/bin/env bash
# coding: utf-8

# Test tsv2tr

echo "Testing examples/1.tsv. Output to examples/1.tr"
FILE=examples/1.tsv
echo "python tsv2tr.py -i 1 ${FILE}"
python tsv2tr.py -i 1 ${FILE}

echo "Testing examples/2.tsv. Output to examples/2.tr"
FILE=examples/2.tsv
echo "python tsv2tr.py ${FILE}"
python tsv2tr.py ${FILE}
