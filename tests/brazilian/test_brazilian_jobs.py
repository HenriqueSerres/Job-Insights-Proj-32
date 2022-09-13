from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    english_keys = [key for key in result]
    assert "title" in english_keys
    assert "salary" in english_keys
    assert "type" in english_keys
