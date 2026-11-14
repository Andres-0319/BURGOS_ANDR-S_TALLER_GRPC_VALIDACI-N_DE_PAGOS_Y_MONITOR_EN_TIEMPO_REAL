from concurrent import futures
import time
import grpc
import comercio_digital_pb2
import comercio_digital_pb2_grpc

class ComercioDigitalServicer (comercio_digital_pb2_grpc.ValidadorPagosServicer):
    def VerificarTransaccion (self, request, context):
        print (f" [Servidor] Petición recibida para transacción: {request.id_transaccion}") 
        if request.monto <= 0 or len(request.numero_tarjeta) != 16:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Monto o número de tarjeta inválido")
            return comercio_digital_pb2.ResultadoPago()
        
        if request.numero_tarjeta.startswith("4000"):
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Tarjeta bloquada por fraude")
            return comercio_digital_pb2.ResultadoPago()

        if request.monto > 10000:
            if request.pais_origen not in ["US", "MX"]:
                return comercio_digital_pb2.ResultadoPago(
                    aprobado=False, 
                    codigo_autorizacion="", 
                    motivo_rechazo=("Rechazado por política de fraude: Monto > $10000 requiere país" " US o MX"
                ),
            )
        
        return comercio_digital_pb2.ResultadoPago(
            aprobado=True,
            codigo_autorizacion="AUTH-OK-" + str(int(time.time())),
            motivo_rechazo="",)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    comercio_digital_pb2_grpc.add_ValidadorPagosServicer_to_server(
        ComercioDigitalServicer(), server
    )
    puerto = "50051"
    server.add_insecure_port(f"[::]:{puerto}")
    server.start()
    print(f" Servidor gRPC escuchando en el puerto {puerto}...")
    server.wait_for_termination()

if __name__== "__main__":
    serve()