# Como ejecutar el Backend
- Instalar [Docker y Docker Compose](https://docs.docker.com/get-started/get-docker/) (Incluidos al instalar Docker Desktop, o por separado)
- Clonar el repositorio y navegar hasta el directorio raiz.
- Crear un archivo `.env` en el directorio `/api/`. Usar el archivo `/api/.env.EXAMPLE` como referencia.
- Ejecutar: 
```bash 
docker compose up
```
- Se puede acceder a la documentación de la API, por defecto en: http://localhost:8080/docs y al panel de administración de RabbitMQ, por defecto en: http://localhost:15672/ (por defecto, usuario: guest, contraseña: guest)

