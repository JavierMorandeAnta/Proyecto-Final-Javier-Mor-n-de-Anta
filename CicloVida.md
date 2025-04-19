### **Descripción del Ciclo de Vida del Software**

---

#### **1. Modelo de Desarrollo**

1. **Desarrollo Local**:
   - Los desarrolladores trabajarán en sus máquinas locales utilizando un entorno virtual configurado con `venv` o `pipenv`.
   - La base de datos local será PostgreSQL, replicando la configuración de producción.
   - El archivo 

manage.sh

 se usará para inicializar la base de datos localmente.

2. **Tipos de Pruebas Obligatorias**:
   - **Pruebas Unitarias**: Validarán la lógica de negocio y las funciones individuales.
   - **Pruebas de Integración**: Verificarán la interacción entre los componentes (API y base de datos).
   - **Pruebas de Carga**: Simularán múltiples usuarios para garantizar que la aplicación pueda manejar tráfico concurrente.
   - **Pruebas de Seguridad**: Validarán que no existan vulnerabilidades comunes como inyecciones SQL o XSS.

3. **Diferentes Tipos de Entornos**:
   - **Desarrollo**: Entorno local con configuraciones de desarrollo (`FLASK_ENV=development`).
   - **Pruebas**: Entorno aislado en AWS para ejecutar pruebas automatizadas.
   - **Producción**: Entorno en AWS con configuraciones optimizadas para rendimiento y seguridad.

4. **Modelo de Ramas**:
   - **Modelo GitHub Flow**:
     - La rama principal será `main`.
     - Cada nueva funcionalidad o corrección se desarrollará en ramas específicas (`feature/nombre`, `bugfix/nombre`).
     - Las ramas se fusionarán a `main` mediante Pull Requests (PR) con revisiones obligatorias.
   - **Decisiones de Despliegue**:
     - Solo los cambios aprobados en `main` se desplegarán en producción.
     - Los cambios en ramas de características se desplegarán en entornos de pruebas para validación.

---

#### **2. Modelo de Operaciones**

1. **Estrategia de Despliegue**:
   - **Despliegue Rolling**:
     - Se actualizarán las instancias de EKS de manera gradual para evitar interrupciones.
     - Se utilizará un balanceador de carga (AWS ELB) para enrutar el tráfico solo a las instancias saludables.
   - **Rollback Automático**:
     - Si una nueva versión falla las pruebas de salud, AWS EKS revertirá automáticamente a la versión anterior.

2. **Gestión de Trazas y Logs**:
   - **Logs**:
     - Los logs de la aplicación se enviarán a **AWS CloudWatch Logs** para centralizar su gestión.
   - **Trazas**:
     - Se utilizará **AWS X-Ray** para rastrear solicitudes y diagnosticar problemas de rendimiento.
   - **Alertas**:
     - Se configurarán alarmas en **AWS CloudWatch** para notificar sobre errores críticos o métricas anómalas.

3. **Monitoreo y Mantenimiento**:
   - **Métricas**:
     - Se monitorearán métricas clave como uso de CPU, memoria y latencia de la API.
   - **Actualizaciones**:
     - Las actualizaciones de dependencias y parches de seguridad se realizarán de manera periódica.
   - **Backups**:
     - Se configurarán backups automáticos en Amazon RDS para garantizar la recuperación ante fallos.

---

Este ciclo de vida asegura un desarrollo colaborativo eficiente, pruebas exhaustivas y un despliegue confiable en producción, minimizando riesgos y garantizando un servicio continuo para los usuarios.
