"""describe(): descriptive stats in pure Python.

Rules: no numpy, pandas or the statistics module inside describe().
std = SAMPLE standard deviation (divide by n - 1), the same as pandas .describe().
"""


def describe(data: list[float]) -> dict[str, float]:
    """Return count, mean, median, std, min and max. Raise ValueError on an empty list."""
    ...


if __name__ == "__main__":
    import statistics

    d = describe([1, 2, 3, 4, 100])
    assert d["count"] == 5
    assert d["mean"] == 22
    assert d["median"] == 3  # the outlier drags the mean, not the median
    assert d["min"] == 1 and d["max"] == 100

    data = [2, 4, 4, 4, 5, 5, 7, 9]
    d = describe(data)
    assert d["median"] == 4.5  # even count: average of the two middle values
    assert round(d["std"], 3) == round(statistics.stdev(data), 3)  # about 2.138

    try:
        describe([])
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    print("describe: all tests passed")
