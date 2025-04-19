Arquitectura de la Solución
1. Descripción de la Arquitectura del Sistema
La solución es una aplicación web basada en Flask que implementa una API REST para la gestión de datos almacenados en una base de datos SQL. La arquitectura está diseñada para ser escalable, segura y fácil de mantener, utilizando tecnologías modernas y servicios de AWS.

1.1 Servicios y Componentes
API Backend:

Framework: Flask.
Funcionalidad: Proporciona endpoints RESTful para operaciones CRUD sobre la base de datos.
Escalabilidad: Desplegado en múltiples instancias detrás de un balanceador de carga.
Base de Datos:

Tecnología: Amazon RDS (PostgreSQL).
Funcionalidad: Almacena los datos de la aplicación.
Escalabilidad: Configuración para replicación y particionamiento si es necesario.
Balanceador de Carga:

Tecnología: AWS Elastic Load Balancer (ELB).
Funcionalidad: Distribuye el tráfico entre múltiples instancias del backend para garantizar alta disponibilidad.
Terminador SSL:

Tecnología: AWS Certificate Manager (ACM).
Funcionalidad: Gestiona la terminación de conexiones HTTPS para garantizar la seguridad de las comunicaciones.
Telemetría y Monitoreo:

Tecnología: AWS CloudWatch.
Funcionalidad: Recolección de métricas de rendimiento, monitoreo en tiempo real y gestión de logs.
2. Arquitectura Cloud
La solución se desplegará en AWS utilizando los siguientes servicios:

Compute:

Amazon Elastic Kubernetes Service (EKS): Orquestación de contenedores para gestionar múltiples instancias del backend.
Amazon Elastic Container Registry (ECR): Almacenamiento de imágenes Docker.
Networking:

Amazon VPC: Red privada virtual para aislar los recursos.
Subredes: Subredes públicas para el balanceador de carga y privadas para las instancias de la aplicación y la base de datos.
Grupos de Seguridad: Control de acceso a nivel de red.
Almacenamiento:

Amazon RDS (PostgreSQL): Base de datos relacional para almacenar los datos de la aplicación.
Seguridad:

AWS IAM: Gestión de roles y permisos.
AWS Certificate Manager (ACM): Gestión de certificados SSL/TLS.
Monitoreo y Logs:

AWS CloudWatch: Monitoreo de métricas y logs.
AWS CloudTrail: Auditoría de acciones realizadas en la infraestructura.
Despliegue y CI/CD:

AWS CodePipeline: Automatización del flujo de despliegue.
AWS CodeBuild: Construcción y pruebas automáticas.
3. Diagrama de Arquitectura
El siguiente diagrama ilustra cómo los servicios de AWS interactúan entre sí para soportar la solución:
+-------------------+       +-------------------+
|                   |       |                   |
|  Elastic Load     | <---> |  AWS Certificate  |
|  Balancer (ELB)   |       |  Manager (ACM)    |
|                   |       |                   |
+-------------------+       +-------------------+
           |                          |
           v                          v
+-------------------+       +-------------------+
|                   |       |                   |
|  EKS (Flask API)  | <---> |  CloudWatch       |
|                   |       |  (Metrics & Logs) |
+-------------------+       +-------------------+
           |
           v
+-------------------+
|                   |
|  Amazon RDS       |
|  (PostgreSQL)     |
|                   |
+-------------------+

4. Conclusión
Esta arquitectura aprovecha los servicios nativos de AWS para garantizar escalabilidad, seguridad y monitoreo. La solución es modular, lo que facilita su mantenimiento y permite adaptarse a cambios en los requisitos del negocio.

