import pytest

import whatintime


@whatintime.whatintime()
def test_timer():
    print("Hello World!")


@whatintime.whatintime(whatintime.TimeFormat.S)
def test_timer_second_convert():
    print("Hello World!")


@whatintime.whatintime(whatintime.TimeFormat.M)
def test_timer_minute_convert():
    print("Hello World!")


@whatintime.whatintime(whatintime.TimeFormat.H)
def test_timer_hour_convert():
    print("Hello World!")


def test_timer_return():
    @whatintime.whatintime()
    def test_timer():
        print("Hello World!")
        return 1

    assert test_timer() == 1


def test_timer_args():
    @whatintime.whatintime()
    def test_timer(a, b):
        print("Hello World!")
        return a + b

    assert test_timer(1, 2) == 3


def test_timer_kwargs():
    @whatintime.whatintime()
    def test_timer(a, b):
        print("Hello World!")
        return a + b

    assert test_timer(a=1, b=2) == 3


def test_timer_args_kwargs():
    @whatintime.whatintime()
    def test_timer(a, b):
        print("Hello World!")
        return a + b

    assert test_timer(1, b=2) == 3


@pytest.mark.parametrize(
    "ns, target, expected",
    [
        (300, whatintime.TimeFormat.S, 3e-07),
        (300, whatintime.TimeFormat.M, 5e-09),
        (300, whatintime.TimeFormat.H, 8.333333333333e-11),
        (300, whatintime.TimeFormat.NS, 300),
        (300, whatintime.TimeFormat.MS, 0.0003),
    ],
)
def test_time_format(ns, target, expected):
    assert target(ns) == pytest.approx(expected)
