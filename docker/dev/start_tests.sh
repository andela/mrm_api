#!/bin/bash
cd /app/
export $(cat .env.tests | xargs)
eval $@
