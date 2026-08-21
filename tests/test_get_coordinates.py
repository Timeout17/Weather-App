import pytest
import httpx

from project.logic.services.localizaton import LoocalizationClass


@pytest.mark.anyio
async def test_get_coordinates(monkeypatch):

    class FakeResponse:

        def raise_for_status(self):
            pass

        def json(self):
            return [
                {
                    "lat": 46.253,
                    "lon": 20.141
                }
            ]


    class FakeClient:

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc_value, traceback):
            pass

        async def get(self, url, params):
            return FakeResponse()


    monkeypatch.setattr(
        httpx,
        "AsyncClient",
        lambda: FakeClient()
    )

    localization = LoocalizationClass()

    result = await localization.getCoordinates("Szeged")

    assert result == (46.253, 20.141)