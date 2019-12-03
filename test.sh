#!/usr/bin/env bash

# Run computepac package unit tests
#
# Use the following three lines to run this bash script locally in a terminal:
#
#     cd your_path/computepac
#     chmod +x test.sh
#     ./test.sh
#

echo -e "           Unit tests for compute-pac initialized           "
pytest
echo -e "                   Unit tests completed                     "
