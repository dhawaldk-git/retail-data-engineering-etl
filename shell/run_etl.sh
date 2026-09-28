#!/bin/bash

echo "ETL Started"

echo "===== VALIDATION ====="
python ../scripts/etl.py || exit 1
# python ../scripts/validate.py || exit 1

# echo "Validation Exit Code: $?"
# # python ../scripts/extract.py || exit 1

# echo "Before Transform"
# python ../scripts/transform.py || exit 1
# echo "Transform Exit Code: $?"

# python ../scripts/load.py || exit 1

echo "ETL Completed Successfully"
