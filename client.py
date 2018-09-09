import grpc
import calculator_pb2
import calculator_pb2_grpc

chnl = grpc.insecure_channel('localhost:3008')
stub = calculator_pb2_grpc.ExecuteExpressionStub(chnl)
x = input("Enter operand 1 for addition ")
y = input("Enter operand 2 for addition ")
expression = calculator_pb2.Expression(operand1=float(x), operand2=float(y), operator='+')
response = stub.ExecExp(expression)

print('The result is ')
print(response.operand1)