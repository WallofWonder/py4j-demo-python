from py4j.clientserver import ClientServer, JavaParameters, PythonParameters
from py4j.java_collections import ListConverter


class OperatorTest(object):

    def __init__(self):
        self.client_server = None

    def set_server(self, client_server):
        self.client_server = client_server

    def test(self, data):
        self.client_server.jvm.System.out.println("Python处理中。。")
        data.append(5)
        python_list = [i for i in data]
        # https://www.py4j.org/advanced_topics.html#converting-python-collections-to-java-collections
        python_list = ListConverter().convert(python_list, self.client_server._gateway_client)

        return python_list

    def add(self, a, b):
        # gateway.jvm.System.out.println("完成加法计算！")
        return a + b

    class Java:
        implements = ["com.example.py4jdemo.utils.operators.OperatorTest",
                      "com.example.py4jdemo.utils.operators.Addition"]


if __name__ == '__main__':
    op_test = OperatorTest()
    # gateway = JavaGateway(
    #     gateway_parameters=GatewayParameters(port=25333),
    #     callback_server_parameters=CallbackServerParameters(port=22536),
    #     python_server_entry_point=average)
    clientServer = ClientServer(
        java_parameters=JavaParameters(port=25333),
        python_parameters=PythonParameters(port=25336),
        python_server_entry_point=op_test)
    op_test.set_server(clientServer)
    print("server started")
