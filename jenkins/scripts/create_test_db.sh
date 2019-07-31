#!/bin/bash
function start {
    apt-get install -y postgresql-9.2
	adduser postgres sudo
	echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
	sudo -u postgres -H sh -c "psql -c 'CREATE DATABASE test;'"
}
start $@
