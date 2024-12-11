Proyecto: Configuración de Raspberry Pi para Red Wi-Fi, Base de Datos y Servidor TCP

Este repositorio contiene todo el código y los archivos necesarios para configurar completamente una Raspberry Pi como punto de acceso Wi-Fi, servidor de base de datos PostgreSQL y servidor TCP, todo gestionado mediante contenedores Docker para garantizar la portabilidad y la replicación en otros entornos.

Descripción del Proyecto

El objetivo del proyecto es implementar una infraestructura que permita:

Configurar la Raspberry Pi como un punto de acceso Wi-Fi funcional.

Gestionar una base de datos PostgreSQL para almacenar información sobre dispositivos conectados y datos capturados.

Crear un servidor TCP que procese conexiones entrantes y datos de clientes.

Garantizar la portabilidad del sistema mediante el uso de Docker.

Requerimientos Iniciales

El proyecto fue desarrollado utilizando las siguientes tecnologías y herramientas:

Raspberry Pi OS.

PostgreSQL 15.

Docker y Docker Compose.

Lenguaje de programación: Python 3.11.

Librerías y herramientas adicionales: psycopg2-binary.

Además, se configuraron servicios clave en la Raspberry Pi, como hostapd y dnsmasq, para habilitar el acceso Wi-Fi.

Estructura del Proyecto

Archivos Principales

Archivos de configuración:

hostapd.conf: Configuración del servicio hostapd para habilitar el punto de acceso Wi-Fi.

dnsmasq.conf: Configuración del servicio dnsmasq para el manejo de DHCP y DNS.

postgresql.conf: Configuración personalizada de PostgreSQL.

pg_hba.conf: Configuración de acceso para PostgreSQL.

Códigos Python:

conectar_postgresql.py: Script para conectarse a la base de datos PostgreSQL.

insertar_datos.py: Script para insertar datos desde un archivo JSON en la base de datos.

crear_tablas.py: Script para crear las tablas necesarias en PostgreSQL.

main.py: Script principal para el servidor TCP.

Archivos Docker:

Dockerfile (para PostgreSQL y Python).

docker-compose.yml: Orquestación de los servicios.

Estructura de Directorios

.
|-- partes2/
|   |-- python_app/
|   |   |-- main.py
|   |   |-- requirements.txt
|   |-- postgresql/
|   |   |-- Dockerfile
|   |   |-- postgresql.conf
|   |   |-- pg_hba.conf
|   |-- docker-compose.yml
|-- configuraciones_previas/
|   |-- hostapd.conf
|   |-- dnsmasq.conf

Proceso de Desarrollo

Fase 1: Configuración del Punto de Acceso Wi-Fi

Se configuraron los servicios hostapd y dnsmasq para habilitar el modo de punto de acceso en la Raspberry Pi:

Edición del archivo /etc/hostapd/hostapd.conf con los parámetros necesarios.

Edición del archivo /etc/dnsmasq.conf para gestionar direcciones IP mediante DHCP.

Configuración de reenvío de IPs en /etc/sysctl.conf.

Fase 2: Configuración de PostgreSQL

Instalación de PostgreSQL 15.

Configuración de acceso remoto en los archivos postgresql.conf y pg_hba.conf.

Creación de la base de datos proyecto_wifi_db.

Creación de tablas para dispositivos y paquetes mediante crear_tablas.py.

Fase 3: Servidor TCP

Creación de un servidor TCP utilizando Python (main.py).

El servidor escucha conexiones entrantes y responde a los clientes.

Fase 4: Dockerización

Se crearon contenedores Docker para facilitar el despliegue y la replicación del proyecto:

Contenedor para PostgreSQL con configuraciones personalizadas.

Contenedor para la aplicación Python que gestiona el servidor TCP y la conexión a la base de datos.

Lecciones Aprendidas

Durante el desarrollo, tuvimos que reiniciar parte del proyecto debido a problemas con la configuración inicial de los servicios.

La integración de servicios mediante Docker simplificó el manejo de dependencias.

Se confirmó la importancia de la documentación y el control de versiones para el seguimiento del progreso.

Cómo Ejecutar el Proyecto

Requisitos

Docker y Docker Compose instalados en el sistema.

Instrucciones

Clonar el repositorio:

git clone https://github.com/Benjamin-Sanhueza/Redes2024.git
cd Redes2024

Construir y ejecutar los contenedores:

docker-compose up --build

Acceder a la aplicación:

El servidor TCP estará disponible en el puerto 8000.

PostgreSQL estará disponible en el puerto 5432.

Créditos

Proyecto desarrollado por Benjamin Sanhueza como parte del curso Redes 2024. Todas las configuraciones y scripts en este repositorio han sido implementados y probados para garantizar su funcionalidad.
