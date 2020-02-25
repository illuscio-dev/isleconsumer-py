from spanconsumer import SpanConsumer


class TestConsume:
    def test_import_dicom(self, service: SpanConsumer):

        with service.test_client(delete_queues=True) as client:
            client.put_message(routing_key="in_queue", message="Hello, World!")
            message = client.pull_message("out_queue")

        assert message.media_loaded() == "Hello, World!"
