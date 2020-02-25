import pytest
from spanconsumer import ConnectionSettings


from service.consumer import consumer


@pytest.fixture
def service():
    # Use the test connection settings
    consumer.settings.connection = ConnectionSettings(port=57018)
    return consumer
