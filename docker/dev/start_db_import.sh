#!/bin/bash
function import {
    apt-get update && apt-get install sudo
    filename=$(basename $1)
    sudo -u postgres psql -d converge < $filename
}

import $@
