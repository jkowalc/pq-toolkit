from app.core.sample_manager import SampleManager, SampleDoesNotExistError
from app.core.config import settings
from io import BytesIO
import pytest


@pytest.fixture
def example_byte_stream():
    message = "Hello world!"
    return BytesIO(message.encode()), message


@pytest.fixture
def sample_manager_localhost():
    return SampleManager(
        endpoint="localhost",
        port=settings.MINIO_PORT,
        access_key=settings.MINIO_ROOT_USER,
        secret_key=settings.MINIO_ROOT_PASSWORD,
        sample_bucket_name="testbucket"
    )


def test_manager_init(sample_manager_localhost: SampleManager):
    manager = sample_manager_localhost


def test_manager_complete(example_byte_stream: tuple[BytesIO, str], sample_manager_localhost: SampleManager):
    byte_stream_out, message = example_byte_stream
    manager = sample_manager_localhost

    filename = "test.wav"
    experiment_name = "test"
    manager.upload_sample(experiment_name, filename, byte_stream_out)

    machting_samples = manager.list_matching_samples(experiment_name)
    assert filename in machting_samples

    for data in manager.get_sample(experiment_name, filename):
        assert data.decode() == message

    manager.remove_sample(experiment_name, filename)


def test_manager_non_existent_file(sample_manager_localhost: SampleManager):
    with pytest.raises(SampleDoesNotExistError):
        for _ in sample_manager_localhost.get_sample("this", "does not exist"):
            pass
