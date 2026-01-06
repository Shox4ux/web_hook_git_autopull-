#!/bin/bash
set -e

echo "===== DEPLOY START $(date) =====" >> /var/log/deploy.log

cd crm_back

git pull origin main

docker compose up -d --build crm_back

echo "===== DEPLOY END $(date) =====" >> /var/log/deploy.log
