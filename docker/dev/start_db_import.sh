#!/bin/bash
function import {
    filename=$(basename $1)
    sudo -u postgres psql -d converge < $filename
}

import $@
