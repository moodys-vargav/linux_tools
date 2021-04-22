#!/usr/bin/env bash

multiply() {
    local result=$(( $1 * $2 ))
    return $result
}

sum() {
    local result=$(( $1 + $2 ))
    return $result
}

multiply 4 5
echo "4 * 5 = $?"

sum 4 5
echo "4 + 5 = $?"
