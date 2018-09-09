import calculator_pb2
import calculator_pb2_grpc
import calculator
import grpc
from concurrent import futures
import time
class ExecuteExpressionServicer(calculator_pb2_grpc.ExecuteExpressionServicer):
    def ExecExp(self, request, context):
        response = calculator_pb2.Expression()
        response.operand1 = calculator.add(request.operand1,request.operand2)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
calculator_pb2_grpc.add_ExecuteExpressionServicer_to_server(ExecuteExpressionServicer(),server)
print('server listing on port 3008')
server.add_insecure_port('[::]:3008')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)