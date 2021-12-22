#!/usr/bin/env bash

set -e


trap - ERR

function func1 () {
    echo 222; test 1 = 2
}

echo start ...
echo 111; func1
echo end ...
