FROM odoo:17

# Instalar dependencias adicionales si es necesario
RUN apt-get update && apt-get install -y python3-dev python3-pip

# Copiar archivos del proyecto a la imagen
WORKDIR /workspace
COPY . /workspace

# Exponer el puerto por defecto de Odoo
EXPOSE 8069
