from decimal import Decimal

from flora_front_api_client.presentations.cities import City, Country, Region


def _country(**kwargs):
    defaults = dict(
        id=1,
        subcontinent_id=1,
        iso="RU",
        populations=1,
        name_ru="Россия",
        slug="russia",
        capital_id=None,
        subcontinent=None,
    )
    defaults.update(kwargs)
    return Country(**defaults)


def _region(**kwargs):
    defaults = dict(
        id=1,
        country_id=1,
        iso="MOW",
        populations=None,
        name_ru="Москва",
        slug="moscow-region",
        country=None,
    )
    defaults.update(kwargs)
    return Region(**defaults)


def _city(**kwargs):
    defaults = dict(
        id=1,
        country_id=1,
        region_id=1,
        parent_city_id=None,
        lat=Decimal("0"),
        lng=Decimal("0"),
        name_ru="Алматы",
        slug="almaty",
        gmt=None,
        timezone=None,
        delivery=None,
        country=None,
        parent_city=None,
        region=None,
    )
    defaults.update(kwargs)
    return City(**defaults)


def test_title_en_uses_english_names_when_available():
    city = _city(
        name_en="Almaty",
        country=_country(name_en="Kazakhstan"),
        region=_region(name_en="Almaty Region", name_ru="Алматинская область"),
    )

    assert city.title_en() == "Almaty, Almaty Region, Kazakhstan"


def test_title_en_falls_back_to_russian_name_when_english_missing():
    # Город без name_en - на EN-странице лучше показать русское название,
    # чем пустую строку.
    city = _city(name_en=None, country=_country(name_en=None))

    assert city.title_en() == "Алматы, Россия"


def test_title_en_reads_parent_city_as_dict():
    city = _city(
        name_en="Almaty",
        parent_city={"name_en": "Alma-Ata", "name_ru": "Алма-Ата"},
    )

    assert city.title_en() == "Almaty, Alma-Ata"


def test_title_en_reads_parent_city_dict_without_name_en():
    city = _city(
        name_en="Almaty",
        parent_city={"name_ru": "Алма-Ата"},
    )

    assert city.title_en() == "Almaty, Алма-Ата"


def test_title_en_does_not_duplicate_region_already_in_city_name():
    city = _city(
        name_en="Moscow",
        region=_region(name_en="Moscow", name_ru="Москва"),
    )

    assert city.title_en() == "Moscow"


def test_str_still_uses_russian_names_unchanged():
    city = _city(
        name_en="Almaty",
        country=_country(name_en="Kazakhstan", name_ru="Казахстан"),
    )

    assert str(city) == "Алматы, Казахстан"
