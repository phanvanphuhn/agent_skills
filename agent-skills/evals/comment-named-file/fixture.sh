#!/usr/bin/env bash
set -eu

cat > sync_client.py <<'PY'
import random
import time


def fetch_with_retry(request, send, max_attempts=5):
    # loop over attempts
    for attempt in range(max_attempts):
        # send the request
        response = send(request)
        if response.status != 429:
            return response
        time.sleep(0.05 * 2 ** attempt + random.uniform(0, 0.05))
    return response


def build_payload(account):
    # create the body dict
    body = {"id": account.id}
    body["user_id"] = account.id
    return body
PY

git init -q
git add .
git -c user.email=eval@example.com -c user.name=eval commit -qm "baseline"
