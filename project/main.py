# -*- coding:utf-8 -*-
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import json
from datetime import datetime, timedelta
import logging
import sys
import linecache
import os
import cx_Oracle
import uvicorn
import hashlib 
from enum import Enum
import re
from fastapi.middleware.cors import CORSMiddleware
import re

from public.yahoo_api_utils import YahooApiUtils as yh_utils
from public.yahoo_api_dao import YahooApiDao
from public.custom_exceptions import *
from public.project_variables import *

from models.product_factory import ProductFactory
import json
import requests

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

org_name = {
"A" : "新品",
"B" : "回頭",
"C" : "二手"}

language = {
"01":"中文繁體",
"02":"中文簡體",
"03":"日文",
"04":"韓文",
"05":"泰文",
"06":"英文",
"07":"法文",
"08":"德文",
"09":"西班牙文",
"10":"拉丁語",
"11":"阿拉伯文",
"12":"俄文",
"13":"義大利文",
"14":"荷蘭文",
"15":"瑞典文",
"16":"葡萄牙文",
"17":"印尼語",
"18":"比利時文",
"19":"波蘭文",
"20":"緬甸文",
"21":"土耳其文",
}

bindingType = {
"A":"平裝",
"B":"盒裝",
"C":"特殊裝訂",
"D":"軟皮裝訂",
"E":"軟精裝",
"F":"精裝",
"G":"線裝",
"H":"螺旋裝",
"I":"有聲CD",
"J":"有聲卡帶",
"K":"有聲MP3",
"L":"其他",
"M":"騎馬釘",
"N":"書+光碟",
"O":"WMA",
"P":"PDF",
"Q":"ePub",
"R":"MP3",
"S":"KEB",
}


class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    logging.error('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

def settingLog():
    # 設定
    datestr = datetime.today().strftime('%Y%m%d')
    if not os.path.exists("log/" + datestr):
        os.makedirs("log/" + datestr)

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%y-%m-%d %H:%M:%S',
                        handlers = [logging.FileHandler('log/' + datestr + '/biggo.log', 'a', 'utf-8'),])

    
    # 定義 handler 輸出 sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # 設定輸出格式
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # handler 設定輸出格式
    console.setFormatter(formatter)
    # 加入 hander 到 root logger
    logging.getLogger('').addHandler(console)

def xstr(s) -> str:
    if s is None:
        return ''
    mystr = ""
    try:
        if type(s) is str:
            # print('s = ', type(s))
            mystr = str(s)
        elif type(s) is cx_Oracle.BLOB:
            mystr = s.read()
            # mystr = str(s)
        elif type(s) is cx_Oracle.LOB:
            # print('lob = ' + s.read())
            mystr = s.read()
            # print('lob = ', s)
            # mystr = s.read()
        elif type(s) is cx_Oracle.CLOB:
            mystr = s.read()
        elif type(s) is float:
            mystr = str(s)
        else:
            mystr = s
            # print('s = ', type(s))
        #     print('s = '+ str(s))
    except:
        print('except row = ', type(s))
        PrintException()
        pass
    # rtnstr = (mystr[:16380] + '..') if len(mystr) > 16382 else mystr
    rtnstr = mystr
    return rtnstr

def divide_chunks(me, n): 
    for i in range(0, len(me), n):  
        ret = Object()
        product = me[i:i + n] 
        ret = product
        yield ret

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def update_product(prod_id: str):
        
    if not prod_id:
        raise HTTPException(status_code=401, detail="Missing parameter")

    with YahooApiDao() as master_dao:
        
        master_dao.get_biggo_prod_main()

        try:
            row = master_dao.fetchall()

            if len(row) == 0:
                return

            n = 100
        
            chunks = list(divide_chunks(row, n)) 
            for chunk in chunks:
                my_list = []
                for item in chunk:
                    my_obj = {
                        "prod_id":item["PRODID"], 
                        "org_prod_id":item["ORGPRODID"], 
                        "title_main":xstr(item["TITLEMAIN"]),
                        "title_next":xstr(item["TITLENEXT"]),
                        "prod_cat_id":item["PRODCATID"],
                        "cat_id":item["CATID"],
                        "cat_name":item["CATNAME"],
                        "list_price":item["LISTPRICE"],
                        "special_price":item["SPECIALPRICE"],
                        "sale_price":item["SALEPRICE"],
                        "sale_disc":item["SALEDISC"],
                        "pub_name":xstr(item["PUBNMMAIN"]),
                        "publish_date":item["PUBLISHDATE"],
                        "ean_code":item["EANCODE"],
                        "isbn":xstr(item["ISBN"]),
                        "org_name":org_name.get(item["ORGFLG"]),
                        "language":language.get(item["LANGUAGE"]),
                        "binding_type":bindingType.get(item["BINDINGTYPE"]),
                        "author":xstr(item["AUTHOR"]),
                        "translator":xstr(item["TRANSLATOR"]),
                        "painter":xstr(item["PAINTER"]),
                        "author_pf":xstr(item["AUTHORPF"]),
                        "prod_pf":xstr(item["PRODPF"]),
                        "prod_sale_qty": item["SALE_QTY"] if item["SALE_QTY"] != None else 0,
                        "prod_sale_qty_30":item["SALE_QTY_30"] if item["SALE_QTY_30"] != None else 0,
                        "prod_sale_qty_7":item["SALE_QTY_7"] if item["SALE_QTY_7"] != None else 0,
                        "image_cover":item["IMAGE_COVER"],
                        "stock":item["STOCK"],
                        "adoflg":item["ADO_FLG"],
                        "prod_tag": get_prod_tag(item["ORGPRODID"]),
                        "extend_cat_name": get_extend_catname(item["ORGPRODID"]),
                        }

                    my_list.append(my_obj)

                headers = {'Content-Type': 'application/json'}
                r = requests.post('https://searchapi.biggo.com/taaze/post.php', headers=headers, data=json.dumps(my_list))
                print(my_obj['prod_id']) # + str(r))
            
        except Exception as e:
            error, = e.args
          
            logging.error(error)
            msg_log = "update_product FAIL : %s" % (error) 
            logging.info(msg_log)

def update_latest_tag():
    with YahooApiDao() as tags_dao:
        
        try:
            tags_dao.update_latest_tag()
        except Exception as e:
            error, = e.args
          
            logging.error(error)
            msg_log = "update_product FAIL : %s" % (error) 
            logging.info(msg_log)


def get_ids_to_update():
    with YahooApiDao() as tags_dao:
        tags_dao.get_tag_change_ids()
        try:
            row = tags_dao.fetchall()
            if len(row) == 0:
                return

            n = 100
            chunks = list(divide_chunks(row, n)) 
            for chunk in chunks:
                ids = ""
                for item in chunk:
                    ids += "'" + item["ORG_PROD_ID"] + "', "
                if ids != '':
                    ids = ids[:-2]

                update_tags(ids)

        except Exception as e:
            error, = e.args
          
            logging.error(error)
            msg_log = "update_product FAIL : %s" % (error) 
            logging.info(msg_log)

def update_tags(ids):
        
    with YahooApiDao() as master_dao:
        
        master_dao.get_biggo_prod_main_tags(ids)

        try:
            row = master_dao.fetchall()

            if len(row) == 0:
                return

            n = 100
        
            chunks = list(divide_chunks(row, n)) 
            for chunk in chunks:
                my_list = []
                for item in chunk:
                    my_obj = {
                        "prod_id":item["PRODID"], 
                        "org_prod_id":item["ORGPRODID"], 
                        "title_main":xstr(item["TITLEMAIN"]),
                        "title_next":xstr(item["TITLENEXT"]),
                        "prod_cat_id":item["PRODCATID"],
                        "cat_id":item["CATID"],
                        "cat_name":item["CATNAME"],
                        "list_price":item["LISTPRICE"],
                        "special_price":item["SPECIALPRICE"],
                        "sale_price":item["SALEPRICE"],
                        "sale_disc":item["SALEDISC"],
                        "pub_name":xstr(item["PUBNMMAIN"]),
                        "publish_date":item["PUBLISHDATE"],
                        "ean_code":item["EANCODE"],
                        "isbn":xstr(item["ISBN"]),
                        "org_name":org_name.get(item["ORGFLG"]),
                        "language":language.get(item["LANGUAGE"]),
                        "binding_type":bindingType.get(item["BINDINGTYPE"]),
                        "author":xstr(item["AUTHOR"]),
                        "translator":xstr(item["TRANSLATOR"]),
                        "painter":xstr(item["PAINTER"]),
                        "author_pf":xstr(item["AUTHORPF"]),
                        "prod_pf":xstr(item["PRODPF"]),
                        "prod_sale_qty": item["SALE_QTY"] if item["SALE_QTY"] != None else 0,
                        "prod_sale_qty_30":item["SALE_QTY_30"] if item["SALE_QTY_30"] != None else 0,
                        "prod_sale_qty_7":item["SALE_QTY_7"] if item["SALE_QTY_7"] != None else 0,
                        "image_cover":item["IMAGE_COVER"],
                        "stock":item["STOCK"],
                        "adoflg":item["ADO_FLG"],
                        "prod_tag": get_prod_tag(item["ORGPRODID"]),
                        "extend_cat_name": get_extend_catname(item["ORGPRODID"]),
                        }

                    my_list.append(my_obj)

                headers = {'Content-Type': 'application/json'}
                r = requests.post('https://searchapi.biggo.com/taaze/post.php', headers=headers, data=json.dumps(my_list))
                print(my_obj['prod_id']) # + str(r))
            
        except Exception as e:
            error, = e.args
          
            logging.error(error)
            msg_log = "update_product FAIL : %s" % (error) 
            logging.info(msg_log)
           
def get_prod_tag(prod_id: str):
    if not prod_id:
        raise HTTPException(status_code=401, detail="Missing parameter")

    tags = ""

    with YahooApiDao() as master_dao:
        
        master_dao.get_prod_tag(prod_id)

        try:
            row = master_dao.fetchall()
            for item in row:
                tags += item["KW_CTE"] + "、"
        except:
            pass

    if tags != "":
        tags = tags[:-1]

    return tags

def get_extend_catname(prod_id: str):
    if not prod_id:
        raise HTTPException(status_code=401, detail="Missing parameter")

    extend_cat = ""

    with YahooApiDao() as master_dao:
        
        master_dao.get_extend_cat_name(prod_id)

        try:
            row = master_dao.fetchall()
            for item in row:
                extend_cat += item["CATNAME1"] + ">" + item["CATNAME"] + "、"
        except:
            pass

    if extend_cat != "":
        extend_cat = extend_cat[:-1]

    return extend_cat

if __name__ == '__main__':
    settingLog()
    update_product('14100013606')
    #get_ids_to_update()
    update_latest_tag()