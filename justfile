# Run a notebook with decrypted env vars
edit notebook:
    sops exec-env .env 'uv run marimo edit --watch --port 8888 {{notebook}}'

# Run a notebook in read-only mode
run notebook:
    sops exec-env .env 'uv run marimo run --watch --port 8888 {{notebook}}'

# Kill any process on port 8888
cleanup:
    -fuser -k 8888/tcp

# Run a Python command/script with decrypted env vars
py *args:
    sops exec-env .env 'uv run python {{args}}'

# Decrypt .env to stdout
show-env:
    sops decrypt .env

# Update all git submodules
update-subs:
    git submodule update --remote --merge
