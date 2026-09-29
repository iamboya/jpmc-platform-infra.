#!/bin/bash
echo "🚀 Initiating automated production workspace deployment..."

# 1. Create a secure logging folder structure cleanly
mkdir -p build/logs

# 2. Explicitly write out the config file configuration block
echo "PORT=9000" > build/app.conf

# 3. Secure file system permissions immediately
chmod 600 build/app.conf

echo "✅ Environment configuration successfully deployed and hardened!"
