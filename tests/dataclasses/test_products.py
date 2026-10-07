from flora_front_api_client.presentations.products import FeaturedProductCategory


def test_featured_product_category_name_en_roundtrips():
    category = FeaturedProductCategory(
        id=1, parent_id=None, slug="roses", name_ru="Розы", name_en="Roses"
    )

    assert category.name_en == "Roses"
    assert category.name_ru == "Розы"


def test_featured_product_category_name_en_defaults_to_none():
    category = FeaturedProductCategory(
        id=1, parent_id=None, slug="roses", name_ru="Розы"
    )

    assert category.name_en is None
