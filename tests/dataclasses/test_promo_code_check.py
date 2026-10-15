"""
Регрессионный тест на баг: PromoCode.check() для промокода с ограничением
по датам (work_days == "date") всегда возвращал False, независимо от
реальной даты.

Причина: parse_date() парсит date_start/date_end форматом "%d/%m" (без
года) - Python подставляет год 1900. Сравнение `datetime.now() <=
parse_date(date_end)` (год 1900) структурно никогда не может быть верным
для реального (актуального) года, поэтому check() всегда отклонял такие
промокоды. date_start/date_end в БД хранятся как CHAR(5) ("ДД/ММ") - года
там нет вообще, то есть период задуман как ежегодно повторяющийся, а не
разовый - фикс сравнивает (месяц, день) и отдельно обрабатывает диапазон,
пересекающий границу года (например, "20/12".."10/01").
"""
from datetime import datetime

from flora_front_api_client.presentations.promo import PromoCode


def _promo(*, date_start=None, date_end=None, work_days="date", enabled=1, day_of_week=None):
    return PromoCode(
        id=1,
        code="SALE",
        discount=10,
        day_of_week=day_of_week,
        work_days=work_days,
        enabled=enabled,
        promo_type=1,
        date_start=date_start,
        date_end=date_end,
    )


def test_whole_year_range_is_always_valid():
    # Точный сценарий из репорта: промокод на весь год всё равно считался
    # недействительным.
    promo = _promo(date_start="01/01", date_end="31/12")

    assert promo.check(now=datetime(2026, 7, 15)) is True
    assert promo.check(now=datetime(2027, 1, 1)) is True


def test_date_inside_non_wrapping_range_is_valid():
    promo = _promo(date_start="01/06", date_end="31/08")

    assert promo.check(now=datetime(2026, 7, 15)) is True


def test_date_outside_non_wrapping_range_is_invalid():
    promo = _promo(date_start="01/06", date_end="31/08")

    assert promo.check(now=datetime(2026, 1, 1)) is False


def test_date_inside_year_wrapping_range_after_start_is_valid():
    promo = _promo(date_start="20/12", date_end="10/01")

    assert promo.check(now=datetime(2026, 12, 25)) is True


def test_date_inside_year_wrapping_range_before_end_is_valid():
    promo = _promo(date_start="20/12", date_end="10/01")

    assert promo.check(now=datetime(2027, 1, 5)) is True


def test_date_outside_year_wrapping_range_is_invalid():
    promo = _promo(date_start="20/12", date_end="10/01")

    assert promo.check(now=datetime(2026, 6, 15)) is False


def test_range_boundaries_are_inclusive():
    promo = _promo(date_start="01/06", date_end="31/08")

    assert promo.check(now=datetime(2026, 6, 1)) is True
    assert promo.check(now=datetime(2026, 8, 31)) is True


def test_disabled_promo_is_always_invalid_regardless_of_date():
    promo = _promo(date_start="01/01", date_end="31/12", enabled=0)

    assert promo.check(now=datetime(2026, 7, 15)) is False


def test_week_based_promo_still_checks_day_of_week():
    # Monday=0 .. Sunday=6 (datetime.weekday()); 2026-07-13 is a Monday.
    promo = _promo(work_days="week", day_of_week="0,2,4", date_start=None, date_end=None)

    assert promo.check(now=datetime(2026, 7, 13)) is True  # Monday
    assert promo.check(now=datetime(2026, 7, 14)) is False  # Tuesday


def test_non_date_non_week_work_days_is_always_valid():
    promo = _promo(work_days="all", date_start=None, date_end=None)

    assert promo.check(now=datetime(2026, 7, 15)) is True


def test_check_defaults_to_real_current_time_when_now_not_passed():
    # Existing caller (flora_api's get_user_discount) calls check() with no
    # arguments at all - must keep working exactly as before.
    promo = _promo(date_start="01/01", date_end="31/12")

    assert promo.check() is True
