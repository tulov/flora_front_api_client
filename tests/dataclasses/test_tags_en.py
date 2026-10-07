from flora_front_api_client.presentations.tags import TagsWithParents, TagTreeChild


def test_tree_child_accepts_name_en():
    child = TagTreeChild(id=1, name_ru="Свадьба", name_en="Wedding")

    assert child.name_en == "Wedding"


def test_tree_child_name_en_defaults_to_none():
    assert TagTreeChild(id=1, name_ru="Свадьба").name_en is None


def test_tags_with_parents_accepts_name_en():
    parent = TagsWithParents(
        id=2,
        name_ru="Повод",
        name_en="Occasions",
        children=[TagTreeChild(id=1, name_ru="Свадьба", name_en="Wedding")],
        parent_id=0,
        name="Occasions",
    )

    assert parent.name_en == "Occasions"
    assert parent.children[0].name_en == "Wedding"
