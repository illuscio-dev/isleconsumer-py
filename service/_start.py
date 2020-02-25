from .consumer import consumer


def start() -> None:
    consumer.run()
