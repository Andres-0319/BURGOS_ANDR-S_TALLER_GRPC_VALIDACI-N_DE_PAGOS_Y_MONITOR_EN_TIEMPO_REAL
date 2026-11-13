import grpc
import comercio_digital_pb2
import comercio_digital_pb2_grpc

def run_test_case(stub, peticion, descripcion):
    print(f"\n[CASO DE PRUEBA] {descripcion}")
    print(
        f"Enviando -> Tarjeta: {peticion.numero_tarjeta}, Monto:"
        f" ${peticion.monto}, País: {peticion.pais_origen}"
    )
    
    try:
        respuesta = stub.VerificarTransaccion(peticion)
        if respuesta.aprobado:
            print(
                f" [Cliente] Resultado: APROBADO | Código de Autorización:"
                f" {respuesta.codigo_autorizacion}"
            )
        else:
            print(f" [Cliente] Resultado: RECHAZADO | Motivo: {respuesta.motivo_rechazo}")
    except grpc.RpcError as e:
        print(f" [Error gRPC] Código: {e.code()} | Detalle: {e.details()}")

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = comercio_digital_pb2_grpc.ValidadorPagosStub(channel)
        pago_exitoso = comercio_digital_pb2.SolicitudPago(
            id_transaccion="TXN-001",
            numero_tarjeta="4532123456789012",
            monto=150.0,
            codigo_moneda="USD",
            pais_origen="US",
        )
        run_test_case(stub, pago_exitoso, "1. Pago exitoso válido")
        
        pago_invalido = comercio_digital_pb2.SolicitudPago(
            id_transaccion="TXN-002",
            numero_tarjeta="4532123456789012",
            monto=-50.0,
            codigo_moneda="USD",
            pais_origen="US",
        )
        run_test_case(stub, pago_invalido, "2. Argumento inválido (Monto negativo)")
        
        pago_denegado = comercio_digital_pb2.SolicitudPago(
            id_transaccion="TXN-003",
            numero_tarjeta="4000123456789012",
            monto=200.0,
            codigo_moneda="USD",
            pais_origen="US",
        )
        run_test_case(stub, pago_denegado, "3. Tarjeta denegada (Lista negra)")
            
if __name__ == "__main__":
    run()