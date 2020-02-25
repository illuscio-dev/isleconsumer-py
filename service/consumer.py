from spanconsumer import SpanConsumer, Incoming, Outgoing, MimeType

from ._name import SERVICE_NAME


consumer = SpanConsumer(name=SERVICE_NAME, prefetch_count=20)


# STARTUP TASKS #####


@consumer.on_startup
async def do_something_on_start(service: SpanConsumer) -> None:
    pass


# SHUTDOWN TASKS #####


@consumer.on_shutdown
async def do_something_on_close(service: SpanConsumer) -> None:
    pass


# PROCESSORS #####


@consumer.processor(in_key="in_queue", out_key="out_queue")
async def process_message(incoming: Incoming, outgoing: Outgoing) -> None:
    text = incoming.media_loaded()
    outgoing.media = text
    outgoing.mimetype = MimeType.TEXT
