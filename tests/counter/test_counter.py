from src.counter import count_ocurrences


def test_counter():
    result_python = count_ocurrences("src/jobs.csv", "Python")
    result_javascript = count_ocurrences("src/jobs.csv", "Javascript")

    assert result_python == 1639
    assert result_javascript == 122
