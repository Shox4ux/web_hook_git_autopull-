#!/bin/bash
set -e

echo "===== DEPLOY START $(date) =====" >> /var/log/deploy.log

cd /opt/crm

git pull origin main

docker compose \
  up -d --build crm_back

echo "===== DEPLOY END $(date) =====" >> /var/log/deploy.log
