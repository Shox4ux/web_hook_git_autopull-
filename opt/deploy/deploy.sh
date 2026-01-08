#!/bin/bash
set -e

echo "===== DEPLOY START ====="
date

cd /root/crm_back || {
  echo "❌ crm_back directory NOT FOUND"
  exit 1
}

echo "📦 Pulling latest code"
git pull

echo "🐳 Rebuilding containers"
docker compose up -d --build

echo "✅ DEPLOY FINISHED"
