# Студия разработки Bafomёd group
# Получить доступ можно у https://t.me/satana666mx
# Официальный канал https://t.me/osint_san_framework
# Наш сайт: https://osintsan.ru/
import os
from core.core import osint
from module.utils.licensysi import licence, check_licence
from module.utils.ban import page_start

# Вам необходимо использовать свои API для максимальной анонимности и защиты переваемых данных.

api = {
    "Shodan": "K09VkSIHkNrPZuCzJD0xwHQpkQyvvcb4",
    # Ваш личный token Shodan, вписывать между "сюда_вписывать_ваш_токен"  Получать токен в -->> https://www.shodan.io/

    "Gmap_g": "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",
    # Ваш личный token google, вписывать между "сюда_вписывать_ваш_токен" Получать токен в -->>
    # https://console.cloud.google.com/google/maps-apis/

    "IP_api": "K09VkSIHkNrPZuCzJD0xwHQpkQyvvcb4",  # API Массового сканирование ip address "сюда_вписывать_ваш_токен"
    # Получать токен в -->> https://ipapi.com/

    "ngrok.set_auth_token": "1x4e1bUVDcjsaIQSio1OmAVidRj_6MoL3Fmj2VgMz45sxZxhq",
    # big brother 13,  "сюда_вписывать_ваш_токен" # Получать токен в -->>
    # https://dashboard.ngrok.com/get-started/your-authtoken

    "virustotal_api": "f2db8f66c178028151969aee7e00094803669c159ce5dfcd4fb3b186a03809d6",
    # Выше впиши API вирус тотал
    "cms_detect_api": "",
    # Ниже пример как нужно указывать API
    "phone_apis": "80fd4720becad81c5d60f5364c7d4b2f", # API номер телефона phone_apis -- https://numverify.com/dashboard?logged_in=1

}

LICENCE_FILENAME = 'licence.json'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_LICENCE = os.path.join(BASE_DIR, LICENCE_FILENAME)


def osintsan():
    os.system('clear')
    print(page_start)
    osint()


if __name__ == '__main__':
    if not check_licence(PATH_TO_LICENCE):
        licence(PATH_TO_LICENCE)

    osintsan()


