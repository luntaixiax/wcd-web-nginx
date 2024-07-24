#!/bin/bash
uvicorn app:app --host 0.0.0.0 --port ${PORT} --root-path /api/ --forwarded-allow-ips "*"