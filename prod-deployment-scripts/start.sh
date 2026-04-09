#!/bin/bash

/opt/mcp/linux-app-deployer/venv/bin/python api.py &
PID1=$!

/opt/mcp/linux-app-deployer/venv/bin/python server.py &
PID2=$!

wait -n   # waits until ANY process exits
exit $?   # propagate failure