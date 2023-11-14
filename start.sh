#!/bin/bash

GNUPG_PASS_DIR=Discord/token
DB_USER=""
DB_PASSWD=""
DB_DATABASE=""
DB_ADDES=""


export DB_DSN="mariadb+pymysql://$DB_USER:$DB_PASSWD@$DB_ADDES/$DB_DATABASE?charset=utf8mb4"
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "${CURRENT_DIR}"

client_run() {
	export DISCORD_API_TOKEN="$( pass $GNUPG_PASS_DIR )"
	echo "Running Discord Client ..."
	poetry run python roleplay_discord/main.py
}

client_run
