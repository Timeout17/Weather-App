
from project.models.UserEnum import UserType


class CreateMessageClass:

    @staticmethod
    def create_message(message: str):
        return [
            {
                "role": UserType.SYSTEM.value,
                "content": """
                    Magyarul válaszolj, és használj emojikat. 😊

                    Az időjárási adatok alapján készíts jól tagolt,
                    könnyen olvasható időjárás-jelentést.

                    A választ az alábbi szerkezetben add:

                    ## 🌤️ Időjárás

                    Rövid, természetes összefoglaló az aktuális időjárásról.

                    ## 💡 Hasznos tippek

                    Adj 3-5 hasznos tippet az adott időjáráshoz.
                    Minden tipp külön sorban legyen.

                    ## 📊 Aktuális adatok

                    Az időjárási paramétereket Markdown táblázatban
                    jelenítsd meg.

                    ## 🌅 Napkelte és napnyugta

                    Írd ki külön a napkelte és napnyugta időpontját.

                    ## ☀️ Összegzés

                    Egy rövid összefoglaló arról, hogy milyen idő várható
                    és milyen programokat érdemes választani.

                    FONTOS:
                    - A szekciókat mindig különítsd el üres sorokkal.
                    - Ne írj egyetlen hosszú bekezdést.
                    - Használj Markdown címsorokat.
                    - A Markdown táblázat legyen jól formázott.
                    - Ne ismételd feleslegesen ugyanazokat az adatokat.
                """
            },
            {
                "role": UserType.USER.value,
                "content": message
            }
        ]