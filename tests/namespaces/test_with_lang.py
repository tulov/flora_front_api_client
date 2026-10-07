from flora_front_api_client.namespaces.cities import CitiesNamespace
from flora_front_api_client.namespaces.countries import CountriesNamespace
from flora_front_api_client.presentations.base import Querystring


def _ns(cls):
    # Для построения URL конструктор namespace не нужен.
    return cls.__new__(cls)


def test_with_lang_none_keeps_query_params_untouched():
    qs = Querystring(page=2, per_page=5)

    assert CitiesNamespace.with_lang(qs, None) is qs


def test_with_lang_adds_lang_to_existing_params():
    qs = Querystring(page=2, per_page=5)

    params = CitiesNamespace.with_lang(qs, "en")

    assert params == {"with_fields": None, "filters": None, "sorts": None, "page": 2, "per_page": 5, "lang": "en"}


def test_with_lang_without_params_adds_only_lang():
    assert CountriesNamespace.with_lang(None, "en") == {"lang": "en"}


def test_cities_all_url_contains_lang_only_when_given():
    ns = _ns(CitiesNamespace)

    assert ns.build_url(ns.with_lang(None, "en")) == "/cities/?lang=en"
    assert ns.build_url(ns.with_lang(None, None)) == "/cities/"


def test_countries_all_url_keeps_pagination_and_lang():
    ns = _ns(CountriesNamespace)

    url = ns.build_url(ns.with_lang(Querystring(per_page=10000), "en"))

    assert url.startswith("/countries/?")
    assert "per_page=10000" in url
    assert "lang=en" in url
