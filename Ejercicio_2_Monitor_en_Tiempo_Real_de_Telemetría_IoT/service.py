from concurrent import futures
import grpc
import telemetria_pb2
import telemetria_pb2_grpc
import time
import random
from datetime import datetime


class MonitorCadenaFrioServicer(
    telemetria_pb2_grpc.MonitorCadenaFrioServicer
):

    def TransmitirTelemetria(self, request, context):

        print("\n[Servidor] Nueva suscripción recibida")
        print(f"Camión solicitado: {request.id_camion}")
        print(f"Intervalo: {request.intervalo_segundos} segundos")

        # VALIDAR SI EL CAMIÓN EXISTE

        camiones_existentes = ["CAM-001", "CAM-002"]

        if request.id_camion not in camiones_existentes:

            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("El camión solicitado no existe")

            print("[Servidor] Error: camión no encontrado")

            return

        # VALIDAR EL INTERVALO

        if request.intervalo_segundos <= 0:

            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("El intervalo debe ser mayor a cero")

            return

        print(f"[Servidor] Iniciando transmisión para {request.id_camion}")

        # SIMULACIÓN DE TEMPERATURAS

        temperaturas = [4.5, 3.8, 1.5, 5.2, 8.7, 6.0, 4.2, 1.2, 7.5, 5.0]

        contador = 0

        try:

            while context.is_active():

                temperatura = temperaturas[contador % len(temperaturas)]

                # GENERAR UBICACIÓN SIMULADA

                latitud = -0.1807 + random.uniform(-0.01, 0.01)
                longitud = -78.4678 + random.uniform(-0.01, 0.01)

                # DETECTAR ALERTA CRÍTICA

                alerta = temperatura < 2.0 or temperatura > 8.0

                # GENERAR FECHA Y HORA

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # CREAR MENSAJE DE TELEMETRÍA

                lectura = telemetria_pb2.LecturaSensor(
                    id_camion=request.id_camion,
                    temperatura_celsius=temperatura,
                    latitud=latitud,
                    longitud=longitud,
                    timestamp=timestamp,
                    alerta_critica=alerta
                )

                print(
                    f"[Servidor] Camión: {request.id_camion} | "
                    f"Temperatura: {temperatura}°C | "
                    f"Alerta: {alerta}"
                )

                # ENVIAR LECTURA AL CLIENTE

                yield lectura

                contador += 1

                # ESPERAR EL INTERVALO SOLICITADO

                time.sleep(request.intervalo_segundos)

        except GeneratorExit:
            print("[Servidor] El cliente cerró la suscripción")

        finally:
            print(f"[Servidor] Finalizando transmisión de {request.id_camion}")


def serve():

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    telemetria_pb2_grpc.add_MonitorCadenaFrioServicer_to_server(
        MonitorCadenaFrioServicer(),
        server
    )

    puerto = "50053"

    server.add_insecure_port(f"[::]:{puerto}")

    server.start()

    print(f"Servidor gRPC de telemetría escuchando en el puerto {puerto}...")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
