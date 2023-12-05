#!/bin/bash

GNUPG_PASS_DIR_DISCORD="Discord/token"
GUNPG_PASS_DIR_DB="Mariadb/passwd"
DB_USER="crazydevnew"
DB_PASSWD="$( pass $GUNPG_PASS_DIR_DB )"
DB_DATABASE="roleplay"
DB_ADDES="localhost"

export DB_DSN="mariadb+pymysql://$DB_USER:$DB_PASSWD@$DB_ADDES/$DB_DATABASE?charset=utf8mb4"
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "${CURRENT_DIR}"

client_run() {
	export DISCORD_API_TOKEN="$( pass $GNUPG_PASS_DIR_DISCORD )"
	echo "Running Discord Client ..."
	poetry run python roleplay_discord/main.py
}

client_run
