#!/bin/bash

echo "===== DEPLOY START ====="
date

CRM_DIR="/root/crm_back"

if [ ! -d "$CRM_DIR" ]; then
  echo "❌ crm_back directory NOT FOUND at $CRM_DIR"
  exit 1
fi

cd "$CRM_DIR" || exit 1

echo "📦 Pulling latest code"
git pull

echo "🐳 Rebuilding containers"
docker compose down
docker compose up -d --build

echo "✅ DEPLOY FINISHED"
