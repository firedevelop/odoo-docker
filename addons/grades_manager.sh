#!/bin/bash

# Nombre del módulo
MODULE_NAME="grades_manager"

# Nombre de la base de datos
DB_NAME="odoo"

# Comando para actualizar el módulo
docker-compose exec odoo odoo -u $MODULE_NAME -d $DB_NAME --stop-after-init

# Mensaje de confirmación
echo "Módulo $MODULE_NAME actualizado correctamente en la base de datos $DB_NAME."

