#!/bin/bash
function start {
	apt-get update
	apt-get install sudo
	adduser postgres sudo
	echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
	sudo -u postgres -H sh -c "psql -c 'CREATE DATABASE test;'"
}
start $@
