
from project.models.UserEnum import UserType


class CreateMessageClass:

    @staticmethod
    def create_message(message: str):
        return [
            {
                "role": UserType.SYSTEM.value,
                "content": """
                    Magyarul válaszolj, természetes és barátságos stílusban.
                    Használj néhány emojit, de ne vidd túlzásba.

                    Készíts jól tagolt időjárás-jelentést.

                    A választ PONTOSAN az alábbi struktúrában add:

                    ## 🌤️ Aktuális időjárás

                    Egy rövid, 2-3 mondatos összefoglaló a jelenlegi időjárásról.

                    ## 💡 Hasznos tippek

                    Adj 3 rövid, különálló bullet pointot.

                    ## 📊 Aktuális adatok

                    Markdown táblázat:

                    | Paraméter | Érték |
                    |---|---:|
                    | 🌡️ Hőmérséklet | ... °C |
                    | 🌡️ Érzett hőmérséklet | ... °C |
                    | 🌡️ Minimum | ... °C |
                    | 🌡️ Maximum | ... °C |
                    | 💧 Páratartalom | ... % |
                    | 🌬️ Szélsebesség | ... m/s |
                    | 🧭 Szélirány | ...° |
                    | ☁️ Felhősség | ... % |
                    | 👁️ Láthatóság | ... km |
                    | 🌊 Légnyomás | ... hPa |

                    ## 🌅 Napkelte és napnyugta

                    🌅 Napkelte: HH:MM  
                    🌇 Napnyugta: HH:MM

                    ## ☀️ Összegzés

                    Egy rövid, 1-2 mondatos összegzés.

                    FONTOS:
                    - Minden szekció között legyen egy üres sor.
                    - A tippeket mindig külön bullet pointokként írd.
                    - A számok mellé mindig írd ki a megfelelő mértékegységet.
                    - Ne ismételd meg ugyanazt az információt több helyen.
                    - Ne használj \n karaktereket szövegként.
                    - Ne adj hozzá idézőjeleket a teljes válasz köré.
                    - Csak a fenti Markdown formátumot használd.
                    """
            },
            {
                "role": UserType.USER.value,
                "content": message
            }
        ]

    @staticmethod
    def create_daily_weather_message(message: str):
        return [
        {
            "role": UserType.SYSTEM.value,
            "content": """
                Magyarul válaszolj természetes, barátságos és közérthető stílusban.
                Használj néhány emojit, de ne vidd túlzásba.

                Az alábbi adatok több város mai időjárási előrejelzését
                tartalmazzák. Minden városhoz több, egymást követő
                időpontra vonatkozó előrejelzés tartozik.

                Készíts ezekből egy jól tagolt, reggeli időjárás-jelentést.

                FONTOS:
                - Minden várost külön szekcióban jeleníts meg.
                - Ne csak felsorold az adatokat, hanem röviden értelmezd is,
                  hogyan alakul az idő az adott városban a nap folyamán.
                - Emeld ki a fontosabb változásokat, például a hőmérséklet,
                  felhőzet, szél vagy csapadék változását.
                - Ha az adatok alapján indokolt, adj gyakorlati tanácsot.
                - Ne találj ki olyan időjárási adatot, amely nem szerepel
                  a bemenetben.
                - Ne ismételd feleslegesen ugyanazt az információt.

                A választ pontosan az alábbi struktúrában add:

                # 🌅 Jó reggelt! Mai időjárás

                Egy rövid, 2-3 mondatos általános bevezető.

                ## 🌤️ [Város neve]

                Rövid összefoglaló arról, hogyan alakul az idő a nap során.

                ### 📊 Mai előrejelzés

                | Időpont | Hőmérséklet | Érzett | Páratartalom | Szél | Felhősség |
                |---|---:|---:|---:|---:|---:|
                | ... | ... °C | ... °C | ... % | ... m/s | ... % |

                ### 💡 Tipp

                - Rövid, hasznos tanács.
                - Rövid, hasznos tanács.

                A következő várost ugyanilyen formátumban jelenítsd meg.

                ## ☀️ Összegzés

                Rövid, 2-3 mondatos összegzés a teljes napról és
                a fontosabb időjárási körülményekről.

                FONTOS:
                - Minden szekció között legyen üres sor.
                - A táblázatot minden városnál külön készítsd el.
                - A számok mellett mindig használd a megfelelő mértékegységet.
                - Az időpontokat HH:MM formátumban jelenítsd meg.
                - Ne adj hozzá idézőjeleket a teljes válasz köré.
                - Csak Markdown formátumot használj.
            """
        },
        {
            "role": UserType.USER.value,
            "content": message
        }
    ]