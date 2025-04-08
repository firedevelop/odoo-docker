 <a id="0"></a>
# Table of content
- [1. General](#1)
- [2. Docker commands](#2)
- [3. Full Backup Script for Odoo Docker Environment](#3)
- [4. Restore Script for Odoo Docker Backup](#4)

 <a id="1.1"></a>
# 1. General [🡅](#0)

## File __init__.py
import libraries, classes

## Application
allow your app appears on filter application on file **__manifest__.py**

```'application': True,```

## Module auto update
![2025_04_07_09-56-56.png](images/2025_04_07_09-56-56.png)
(Section 4.14)

## models folder
logic algorithm of your module

## Create Scaffold or Module Structure Demo
```
docker exec -it odoo-docker-web-1 python3 odoo-bin scaffold mi_modulo /mnt/extra-addons
```
## Module create database table
![2025_04_07_20-17-09.png](images/2025_04_07_20-17-09.png)

## Permission on WSL2 ubuntu:
```
ls -ld /home/admin1/odoo-docker/addons/mi_modulo_personal/models
sudo chown -R admin1:admin1 /home/admin1/odoo-docker/addons/mi_modulo_personal/models
sudo chmod -R 755 /home/admin1/odoo-docker/addons/mi_modulo_personal/models
```
if you miss this permission you cannot save or create files from windows 11 PyCharm to Docker or WSL2 Ubuntu.

## find folder 
find / -name "odoo-bin" 2>/dev/null

<a id="2"></a>
# 2. Docker commands [🡅](#0)
## Start Docker
Tips: if doesn't work the command, start the container manually from windows Docker Desktop and will work.

```docker exec -it odoo-docker-web-1 bash```

## Docker Restart
```
docker-compose down
docker-compose up -d
```

## Docker check running
docker ps

## Docker version 

## Delete and Clean Docker volumes
docker volume prune

# Models
Nomrmal = models.Model
Abstract = se usan para ser heredados
Transitorios = no se guarda en base de datos, se utilizan para Wizard.

# PgAdmin from windows 11 connect to WSL2 Ubuntu Docker
from WSL get the ip:
```ip addr | grep inet```

output:
```
    inet 172.17.108.98/20 brd 172.17.111.255 scope global eth0
```
here the ip 172.17.108.98

<a id="3"></a>
# 🛡️ 3. Full Backup Script for Odoo Docker Environment [🡅](#0)

This script creates a complete backup of your Odoo setup, including:

- 📦 The PostgreSQL database volume (`odoo-docker_odoo-db-data`)
- 🧩 Odoo data files volume (`odoo-docker_odoo-web-data`)
- 🧠 Custom addons directory (`./addons`)

---

### 📄 `backup_odoo.sh`

Save this script in the root directory of your Docker project:

```bash
#!/bin/bash

# Backup filename with date and time
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_DIR="./backups"
mkdir -p $BACKUP_DIR

echo "🔄 Backing up Docker volumes..."

# Backup PostgreSQL database volume
docker run --rm \
  -v odoo-docker_odoo-db-data:/volume \
  -v $(pwd)/$BACKUP_DIR:/backup \
  alpine tar czf /backup/db-data_$DATE.tar.gz -C /volume .

# Backup Odoo web data volume (attachments, filestore, etc.)
docker run --rm \
  -v odoo-docker_odoo-web-data:/volume \
  -v $(pwd)/$BACKUP_DIR:/backup \
  alpine tar czf /backup/web-data_$DATE.tar.gz -C /volume .

echo "📁 Backing up custom addons..."

# Backup custom addons directory
tar czf "$BACKUP_DIR/addons_$DATE.tar.gz" ./addons

echo "✅ Full backup saved in: $BACKUP_DIR"

<a id="4"></a>
## 🔁 Restore Script for Odoo Docker Backup

This script restores your full Odoo environment from backups, including:

- 📦 The PostgreSQL database volume (`odoo-docker_odoo-db-data`)
- 🧩 Odoo data volume (`odoo-docker_odoo-web-data`)
- 🧠 Your custom addons (`./addons`)

---

### 🛠️ Script: `restore_odoo.sh`

Save this script alongside the backup script in `~/odoo-docker/`:

```bash
#!/bin/bash

# Ask for the backup base name (without .tar.gz)
echo "🔍 Enter the base name of the backup (e.g., db-data_2025-04-07_20-45-00):"
read BACKUP_NAME

BACKUP_DIR="./backups"

# Check if backup files exist
if [ ! -f "$BACKUP_DIR/db-data_$BACKUP_NAME.tar.gz" ]; then
  echo "❌ $BACKUP_DIR/db-data_$BACKUP_NAME.tar.gz not found"
  exit 1
fi

if [ ! -f "$BACKUP_DIR/web-data_$BACKUP_NAME.tar.gz" ]; then
  echo "❌ $BACKUP_DIR/web-data_$BACKUP_NAME.tar.gz not found"
  exit 1
fi

if [ ! -f "$BACKUP_DIR/addons_$BACKUP_NAME.tar.gz" ]; then
  echo "❌ $BACKUP_DIR/addons_$BACKUP_NAME.tar.gz not found"
  exit 1
fi

echo "🛑 Stopping current containers..."
docker-compose down

echo "🧹 Removing existing volumes..."
docker volume rm odoo-docker_odoo-db-data
docker volume rm odoo-docker_odoo-web-data

echo "♻️ Restoring database volume..."
docker volume create odoo-docker_odoo-db-data
docker run --rm \
  -v odoo-docker_odoo-db-data:/volume \
  -v $(pwd)/$BACKUP_DIR:/backup \
  alpine sh -c "cd /volume && tar xzf /backup/db-data_$BACKUP_NAME.tar.gz"

echo "♻️ Restoring Odoo data volume..."
docker volume create odoo-docker_odoo-web-data
docker run --rm \
  -v odoo-docker_odoo-web-data:/volume \
  -v $(pwd)/$BACKUP_DIR:/backup \
  alpine sh -c "cd /volume && tar xzf /backup/web-data_$BACKUP_NAME.tar.gz"

echo "♻️ Restoring custom addons..."
rm -rf ./addons/*
tar xzf "$BACKUP_DIR/addons_$BACKUP_NAME.tar.gz" -C .

echo "🚀 Starting containers..."
docker-compose up -d

echo "✅ Restore completed successfully."
```
<a id="4"></a>
## 🔁 4.Restore Script for Odoo Docker Backup [🡅](#0)

This script restores your full Odoo environment from backups, including:

- 📦 The PostgreSQL database volume (`odoo-docker_odoo-db-data`)
- 🧩 Odoo data volume (`odoo-docker_odoo-web-data`)
- 🧠 Your custom addons (`./addons`)

---

### 🛠️ Script: `restore_odoo.sh`

Save this script alongside the backup script in `~/odoo-docker/`:

```bash
#!/bin/bash

# Ask for the backup base name (without .tar.gz)
echo "🔍 Enter the base name of the backup (e.g., db-data_2025-04-07_20-45-00):"
read BACKUP_NAME

BACKUP_DIR="./backups"

# Check if backup files exist
if [ ! -f "$BACKUP_DIR/db-data_$BACKUP_NAME.tar.gz" ]; then
  echo "❌ $BACKUP_DIR/db-data_$BACKUP_NAME.tar.gz not found"
  exit 1
fi

if [ ! -f "$BACKUP_DIR/web-data_$BACKUP_NAME.tar.gz" ]; then
  echo "❌ $BACKUP_DIR/web-data_$BACKUP_NAME.tar.gz not found"
  exit 1
fi

if [ ! -f "$BACKUP_DIR/addons_$BACKUP_NAME.tar.gz" ]; then
  echo "❌ $BACKUP_DIR/addons_$BACKUP_NAME.tar.gz not found"
  exit 1
fi

echo "🛑 Stopping current containers..."
docker-compose down

echo "🧹 Removing existing volumes..."
docker volume rm odoo-docker_odoo-db-data
docker volume rm odoo-docker_odoo-web-data

echo "♻️ Restoring database volume..."
docker volume create odoo-docker_odoo-db-data
docker run --rm \
  -v odoo-docker_odoo-db-data:/volume \
  -v $(pwd)/$BACKUP_DIR:/backup \
  alpine sh -c "cd /volume && tar xzf /backup/db-data_$BACKUP_NAME.tar.gz"

echo "♻️ Restoring Odoo data volume..."
docker volume create odoo-docker_odoo-web-data
docker run --rm \
  -v odoo-docker_odoo-web-data:/volume \
  -v $(pwd)/$BACKUP_DIR:/backup \
  alpine sh -c "cd /volume && tar xzf /backup/web-data_$BACKUP_NAME.tar.gz"

echo "♻️ Restoring custom addons..."
rm -rf ./addons/*
tar xzf "$BACKUP_DIR/addons_$BACKUP_NAME.tar.gz" -C .

echo "🚀 Starting containers..."
docker-compose up -d

echo "✅ Restore completed successfully."
```

