from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for key in result:
        assert "title" in key
        assert "salary" in key
        assert "type" in key
