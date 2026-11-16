<div align="center">

# Universidad Politécnica Salesiana

# Carrera de Computación

# Asignatura de Sistemas Distribuidos

</div>

**Nombre del estudiante:** Burgos Andrés

**Fecha:** 18 de noviembre de 2026

**Tema:** Ejercicios de gRPC.

**Objetivos**
- Construir un servicio gRPC unario que valide una solicitud de pago y devuelva una respuesta síncrona indicando si la transacción fue aprobada o rechazada, aplicando códigos de estado gRPC en caso de solicitudes inválidas o denegadas.
- Implementar un patrón gRPC de Server Streaming donde el cliente envía una única petición de suscripción y el servidor responde con un flujo continuo (cadena de respuestas con `yield`) con las lecturas emitidas por los sensores.

**Desarrollo de la actividad**

<div align="center">

**Desarrollo del Ejercicio 1 (Nivel Básico - Unario): Microservicio de Validación de Pagos y Detección de Fraude en E-Commerce**

</div>

<div align="center">

**Parte de la ejecución del Servidor**

</div>

**Paso 1:** En este primer paso, ubicado en la terminal dentro del directorio del proyecto de sistemas distribuidos, se procede a inicializar un entorno virtual de Python mediante el comando "python3 -m venv venv". La creación de este entorno aislado es una buena práctica fundamental en el desarrollo de microservicios, ya que permite encapsular todas las dependencias, bibliotecas y versiones específicas del proyecto (como el ecosistema gRPC) sin alterar ni contaminar la instalación global del sistema operativo.

<img width="690" height="26" alt="image" src="https://github.com/user-attachments/assets/ad70b9ca-ed02-48b1-944d-7ee809814a33" />

**Paso 2:** Se activa el entorno virtual utilizando el comando "source venv/bin/activate", lo cual redirige el intérprete de Python y las rutas de comandos hacia el espacio aislado. Con el entorno activo, se procede a instalar los paquetes indispensables para la comunicación de alto rendimiento mediante el comando "pip install grpcio grpcio-tools". Esto descarga e integra la biblioteca de tiempo de ejecución de gRPC (grpcio) junto con las herramientas de compilación de protocolos (grpcio-tools), las cuales son indispensables para procesar la serialización binaria y habilitar la infraestructura de red sobre HTTP/2 que exige el microservicio de pagos.

<img width="1063" height="363" alt="image" src="https://github.com/user-attachments/assets/35070f62-305c-45dc-8b9c-50215b35e84a" />

**Paso 3:** En este paso final del servidor, se compila el archivo de interfaz de contratos "comercio_digital.proto" utilizando las herramientas de gRPC para generar automáticamente los módulos de Python (_pb2.py y _pb2_grpc.py) que estructuran los mensajes y los stubs de comunicación. Inmediatamente después, se ejecuta el script del servidor con "python servidor_ejercicio_1.py", logrando que el microservicio inicie su ciclo de escucha activa en el puerto 50051.

<img width="1063" height="141" alt="image" src="https://github.com/user-attachments/assets/e08589c3-61c2-4a85-8da3-3411b69cdc7f" />

<div align="center">

**Parte de la ejecución del Cliente**

</div>

**Paso 1:** Se asegura la disponibilidad del entorno virtual aislado creado previamente para el proyecto. Al ejecutar la verificación y activación del entorno junto con la comprobación de los paquetes mediante pip, el sistema confirma que las dependencias como grpcio y grpcio-tools se encuentran debidamente instaladas y satisfechas en su versión requerida. Esto garantiza que el entorno de ejecución del cliente posea las mismas capacidades de serialización y transporte de red que el servidor.

<img width="1069" height="141" alt="image" src="https://github.com/user-attachments/assets/9d9ba16e-4412-4701-9ca7-07611ee5267f" />

**Paso 2:** Se ejecuta el compilador de Protobuf a través de la interfaz de herramientas de gRPC (python -m grpc_tools.protoc) sobre el archivo maestro comercio_digital.proto. Esta acción genera e integra los stubs de comunicación del lado del cliente, los cuales actúan como la capa de abstracción de red que permite invocar de forma remota los métodos del servidor como si fueran funciones locales. Mediante esta serialización binaria ultrarrápida, el cliente queda totalmente preparado para estructurar los mensajes de solicitud de pago y manejar las conexiones síncronas bajo el protocolo HTTP/2.

<img width="1069" height="37" alt="image" src="https://github.com/user-attachments/assets/ca595562-d46f-468f-96f9-dc132d94ad4a" />

**Paso 3:** Se muestra la ejecución exitosa del script cliente mediante el comando "python cliente_ejercicio_1.py", el cual interactúa directamente con el servidor gRPC en el puerto 50051. En la salida de la consola se visualizan de forma clara los tres casos de prueba obligatorios solicitados en la rúbrica: primero, un pago válido que retorna un código de autorización exitoso; segundo, un argumento inválido por monto negativo que captura la excepción gRPC con el código "StatusCode.INVALID_ARGUMENT"; y tercero, una tarjeta de lista negra que dispara la regla de fraude capturando el código "StatusCode.PERMISSION_DENIED".

<img width="1069" height="241" alt="image" src="https://github.com/user-attachments/assets/819ad0cf-bd59-411a-a9de-5cd78edbfb11" />

<div align="center">

**Desarrollo del Ejercicio 2 (Nivel Intermedio - Server Streaming): Monitor en Tiempo Real de Telemetría IoT y Cadena de Frío Logística**

</div>

<div align="center">

**Parte de la ejecución del Servidor**

</div>

**Paso 1:**

**Paso 2:**

**Paso 3:**

<div align="center">

**Parte de la ejecución del Cliente**

</div>

**Paso 1:**

**Paso 2:**

**Paso 3:**

**Conclusiones**

- 
- 
