from datetime import datetime, timezone

import aioredis
from heslo_core import g


async def answer():
    return {'phrase': None,  # g['phrase'],
            'datetime': str(datetime.now(tz=timezone.utc))}, 200


async def messages():
    ret = []
    if g['message1']:
      ret.append({'body': g['message1']})
    if g['message2']:
      ret.append({'body': g['message2']})
    return ret, 200


async def play_store():
    return {'url': 'http://play.google.com/store/apps/details?id=tech.cze.heslo'}, 200


async def app_store():
    return {'url': None}, 200

async def faq():
    return [{'head': "Kdo je autor projektu?",
             'body': "Petr Czepiec, napísať mu môžete na petr@czepiec.me"},
            {'head': "Je to zadarmo?",
             'body': "V princípe áno, ale ak vďaka tejto aplikácii vyhráte, mohli by ste sa s autorom rozdeliť. Ak sa chcete odvďačiť aj bez výhry, možete to spraviť na https://www.patreon.com/czepiec alebo napíšte na email."},
            {'head': "Pre koho je aplikácia určená?",
             'body': "Pre všetkých, ktorým bráni v sledovaní súťaže ich zamestnanie alebo iné aktivity, nemajú televízor, chcú spať, sú pod vplyvom rôznych látok, sú na chate bez signálu, v nemocnici, na pláži... To znamená pre všetkých, ktorý súťaž pozerať nemôžu alebo jednoducho nechcú."},
            {'head': "Prečo to autor robí?",
             'body': "Má k tomu viacero dôvodov. Prezentuje tým služby vývoja IT riešení, baví ho to, ale áno, chce tým poukázať aj na amaterizmus a zlý návrh súťaže Byť zdravý je výhra."},
            {'head': "Je autor očkovaný?",
             'body': "Áno. Autor by rád poznamenal, že s očkovaním váhal a že je to prirodzené. Po postupnom príjmaní mnohých relevantných informácií si vyhodnotil vakcínu ako natoľko bezpečnú, že aj keď autor patrí do málo rizikovej skupiny, rád očkovaním predíde aj miernejšiemu priebehu a prípadným dlhodobejším príznakom ochorenia."},
            {'head': "Je autor registrovaný do súťaže?",
             'body': "Nie. Autor sa z dlhej chvíle skúsil registrovať, ale ani po niekoľkých týždňoch mu neprišla odpoveď. Očkoval sa však v zahraničí, takže NCZI to asi nevie (!) overiť. V každom prípade, aspoň odpovedať by od nich bolo slušné."},
            {'head': "Prečo sa nedá nájsť aplikácia pre iPhone?",
             'body': "App Store ju odstránil. Autor aktívne s Apple komunikoval, ale vzhľadom na App Store Review Guidelines, hlavne bod 5.1.1, aplikáciu ani po viacerých úpravách neschválili. Je to pochopiteľné, autor nemá so súťažou a ani s RTVS žiaden vzťah. V prípade záujmu o TestFlight Internal Testing kontaktujte autora."},
            {'head': "Ako sa získavajú heslá z RTVS?",
             'body': "Prepisujú ručne po vyhlásení a experimentuje sa aj s optickým rozoznávaním textu zo streamu RTVS, ale vždy bude nakoniec heslá validovať človek."},
            {'head': "Čo znamená, že je aplikácia open-source?",
             'body': "Aplikácia ma otvorený zdrojový kód, čo znamená, že ktokoľvek si može kód stiahnuť, upraviť ho a pridať sa k vývoju alebo si spraviť vlastnú verziu aplikácie. Domovský repozitár projektu je https://github.com/czetech/heslo."},
            {'head': "Aké sú v projekte použité technológie?",
             'body': "Frontend je aplikácia vo Flutteri s buildom pre 2 majoritné mobilné platformy a web. Backend API je v Pythone na frameworku Connexion (API first!) a AIOHTTP. Jednotlivé služby bežia v Kubernetes klastri."},
            {'head': "Vznikla táto aplikácia na Slovensku?",
             'body': "Nie."}], 200
