
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