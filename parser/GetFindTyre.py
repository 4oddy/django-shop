from io import BytesIO

from PIL import Image

import psycopg2
import requests
from bs4 import BeautifulSoup

from store import settings


def get_all_tyre():
    url = 'http://api-b2b.4tochki.ru/WCF/ClientService.svc'
    LOGIN, PASS = 'sa30716', 's4ktKFX-pN'

    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'Wcf.ClientService.Client.WebAPI.TS3/ClientService/GetFindTyre'
    }

    page_count, cnt = 6, 0

    for page in range(0, page_count + 1):
        print(f'Обработка страницы {page + 1}')
        payload = f'''
        <soapenv:Envelope 
        xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
        xmlns:wcf="Wcf.ClientService.Client.WebAPI.TS3" 
        xmlns:ts3="http://schemas.datacontract.org/2004/07/TS3.Domain.Models.Client.ClientSoapService.SearchTires" 
        xmlns:arr="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
           <soapenv:Header/>
           <soapenv:Body>
              <wcf:GetFindTyre>
                 <!--Optional:-->
                 <wcf:login>{LOGIN}</wcf:login>
                 <!--Optional:-->
                 <wcf:password>{PASS}</wcf:password>
                 <!--Optional:-->
                 <wcf:filter>
                    <!--Optional:-->
                    <ts3:wrh_list>
                       <!--Zero or more repetitions:-->
                       <arr:int>22</arr:int>
                    </ts3:wrh_list>
                 </wcf:filter>
                 <!--Optional:-->
                 <wcf:page>{page}</wcf:page>
                 <!--Optional:-->
                 <wcf:pageSize>500</wcf:pageSize>
              </wcf:GetFindTyre>
           </soapenv:Body>
        </soapenv:Envelope>
        '''

        result = []
        response = requests.request("POST", url, headers=headers, data=payload)
        xml = BeautifulSoup(response.text, 'xml')

        params = {'code', 'marka', 'model', 'name', 'price', 'price_rozn',
                  'img_big_pish', 'quality', 'season', 'thorn', 'type', 'rest', 'wrh'}

        result = [{param: TyrePriceRest.find(param).text if TyrePriceRest.find(param) else None for param in params}for TyrePriceRest in xml.findAll('TyrePriceRest')]

        # print(result)

        connection = psycopg2.connect(dbname=settings.DB_NAME,
                                      user=settings.DB_USER,
                                      password=settings.DB_PASSWORD,
                                      host=settings.DB_HOST)
        cursor = connection.cursor()

        stmt = """
                INSERT INTO products_product 
                (code, marka, model, name, price, price_rozn, image, quality, season_list, thorn, 
                        type_list, rest, wrh_list, category_id, modify_time) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, localtimestamp)

                on conflict (code) do update 
                    set marka = excluded.marka,
                        model = excluded.model,
                        name = excluded.name,
                        price = excluded.price,
                        price_rozn = excluded.price_rozn,
                        image = excluded.image,
                        quality = excluded.quality,
                        season_list = excluded.season_list,
                        thorn = excluded.thorn,
                        type_list = excluded.type_list,
                        rest = excluded.rest,
                        modify_time = excluded.modify_time
                """

        for item in result:
            digital_fields = ['price', 'price_rozn']  # Список тегов, которые нужно преобразовать в цифру
            for filed in digital_fields:
                if item.get(filed):
                    item[filed] = float(item[filed])

            file = item['img_big_pish'].split('/')[-1].split('.')[0]
            file_name = f'{file}.webp'
            path = settings.BASE_DIR / 'media' / 'store_db' / file_name

            if not path.exists():
                if item['img_big_pish']:
                    img_response = requests.get(item['img_big_pish'])
                    img = Image.open(BytesIO(img_response.content))
                    img.save(path, format='webp')

            to_db = [item['code'],
                     item['marka'],
                     item['model'],
                     item['name'],
                     item['price'],
                     item['price_rozn'],
                     str(path),
                     item['quality'],
                     item['season'],
                     item['thorn'],
                     item['type'],
                     item['rest'],
                     'Екатеринбург',
                     1
                     ]
            cursor.execute(stmt, to_db)
            cnt += 1

        connection.commit()

        connection.close()

    print('', 'База шин заполнена!', f'Добавлено/обновлено строк: {cnt}', sep='\n')


def main():
    get_all_tyre()


if __name__ == '__main__':
    main()
