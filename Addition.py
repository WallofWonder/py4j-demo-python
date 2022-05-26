from py4j.clientserver import ClientServer, JavaParameters, PythonParameters


class Addition(object):
    # def __init__(self):
    #     self.gateway = None
    #
    # def set_gateway(self, gateway):
    #     self.gateway = gateway

    def add(self, a, b):
        # gateway.jvm.System.out.println("完成加法计算！")
        return a + b

    class Java:
        implements = ["com.example.py4jdemo.utils.operators.Addition"]


if __name__ == '__main__':
    addition = Addition()
    clientServer = ClientServer(
        java_parameters=JavaParameters(port=25333),
        python_parameters=PythonParameters(port=25337),
        python_server_entry_point=addition)
    print("server started")
