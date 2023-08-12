CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
GNUPG_PASS_DIR=Discord/FreeRPruDEV
cd "${CURRENT_DIR}"

client_run() {
	export DISCORD_API_TOKEN="$( pass $GNUPG_PASS_DIR )"
	echo "Running Discord Client ..."
	poetry run python roleplay_discord/main.py
}

client_run
