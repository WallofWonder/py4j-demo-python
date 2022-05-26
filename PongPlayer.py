from py4j.java_gateway import JavaGateway, CallbackServerParameters


class PongPlayer(object):

    def start(self, player):
        return player.firstPing(self)

    def firstPong(self, player):
        return player.secondPing(self)

    def secondPong(self, player):
        return "Success"

    class Java:
        implements = ["com.example.py4jdemo.utils.operators.PongPlayer"]


if __name__ == '__main__':
    gateway = JavaGateway(
        callback_server_parameters=CallbackServerParameters())
    ping_player = gateway.jvm.com.example.py4jdemo.utils.operators.PingPlayer()
    pong_player = PongPlayer()
    print(pong_player.start(ping_player))
