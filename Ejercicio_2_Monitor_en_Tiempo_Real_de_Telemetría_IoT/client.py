import grpc
import telemetria_pb2
import telemetria_pb2_grpc


def run():

    with grpc.insecure_channel("localhost:50053") as channel:

        stub = telemetria_pb2_grpc.MonitorCadenaFrioStub(channel)

        print("==========================================")
        print(" MONITOR DE CADENA DE FRÍO - CLIENTE IoT")
        print("==========================================")

        # CREAR SOLICITUD DE SUSCRIPCIÓN

        peticion = telemetria_pb2.SuscripcionCamion(
            id_camion="CAM-001",
            intervalo_segundos=2
        )

        print(f"\nSuscribiéndose al camión: {peticion.id_camion}")
        print(f"Intervalo de lectura: {peticion.intervalo_segundos} segundos")

        try:

            # CONSUMIR EL STREAM DEL SERVIDOR

            for respuesta in stub.TransmitirTelemetria(peticion):

                print("\n------------------------------------------")
                print(" NUEVA LECTURA DE TELEMETRÍA")
                print("------------------------------------------")

                print(f"Camión: {respuesta.id_camion}")
                print(f"Temperatura: {respuesta.temperatura_celsius} °C")
                print(f"Latitud: {respuesta.latitud:.6f}")
                print(f"Longitud: {respuesta.longitud:.6f}")
                print(f"Fecha y hora: {respuesta.timestamp}")

                # COMPROBAR ALERTA CRÍTICA

                if respuesta.alerta_critica:

                    print("\033[91m")
                    print(" ¡¡¡ ALERTA CRÍTICA !!!")
                    print(" TEMPERATURA FUERA DEL RANGO PERMITIDO")
                    print(" ¡REVISAR CADENA DE FRÍO!")
                    print("\033[0m")

                else:

                    print("\033[92m")
                    print(" Estado: TEMPERATURA NORMAL")
                    print("\033[0m")

        except grpc.RpcError as e:

            print("\n[Cliente] ERROR EN LA SUSCRIPCIÓN")
            print(f"Código gRPC: {e.code()}")
            print(f"Detalle: {e.details()}")

        except KeyboardInterrupt:

            print("\n[Cliente] Monitoreo detenido por el usuario")


if __name__ == "__main__":
    run()
