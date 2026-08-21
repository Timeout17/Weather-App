from project.backend.utils.city_loader import CityLoaderClass


def test_loadfile_reads_cities(tmp_path):

    city_file = tmp_path / "cities.txt"
    city_file.write_text(
        "Budapest\n"
        "Szeged\n"
        "Gyoma\n",
        encoding="utf-8"
    )

    loader = CityLoaderClass()

    result = loader.loadfile(str(city_file))

    assert result == [
        "Budapest",
        "Szeged",
        "Gyoma"
    ]


def test_loadfile_strips_whitespace(tmp_path):

    city_file = tmp_path / "cities.txt"
    city_file.write_text(
        "  Budapest  \n"
        "Szeged   \n"
        "  Gyoma\n",
        encoding="utf-8"
    )

    loader = CityLoaderClass()

    result = loader.loadfile(str(city_file))

    assert result == [
        "Budapest",
        "Szeged",
        "Gyoma"
    ]


def test_loadfile_missing_file():

    loader = CityLoaderClass()

    result = loader.loadfile("does_not_exist.txt")

    assert result == []