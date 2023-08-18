GNUPG_PASS_DIR=Path/To/Pass
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "${CURRENT_DIR}"

client_run() {
	export DISCORD_API_TOKEN="$( pass $GNUPG_PASS_DIR )"
	echo "Running Discord Client ..."
	poetry run python roleplay_discord/__init__.py
}

client_run
