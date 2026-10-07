from flora_front_api_client.presentations.orders import Answer


def _answer(**kwargs):
    return Answer(**kwargs)


def test_answer_accepts_english_fields():
    a = _answer(txt="Хорошо", txt_en="Good", name="Анна", name_en="Anna")

    assert a.txt_en == "Good"
    assert a.name_en == "Anna"


def test_text_by_lang_en_uses_english_when_filled():
    a = _answer(txt="Хорошо", txt_en="Good")

    assert a.text_by_lang("en") == "Good"


def test_text_by_lang_en_falls_back_to_ru_when_empty():
    a = _answer(txt="Хорошо", txt_en="")

    assert a.text_by_lang("en") == "Хорошо"


def test_text_by_lang_ru_ignores_english():
    a = _answer(txt="Хорошо", txt_en="Good")

    assert a.text_by_lang("ru") == "Хорошо"
    assert a.text_by_lang() == "Хорошо"


def test_name_by_lang():
    a = _answer(name="Анна", name_en="Anna")

    assert a.name_by_lang("en") == "Anna"
    assert a.name_by_lang("ru") == "Анна"
    assert _answer(name="Анна").name_by_lang("en") == "Анна"
