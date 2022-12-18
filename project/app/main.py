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

from public.yahoo_api_utils import YahooApiUtils as yh_utils
from public.yahoo_api_dao import YahooApiDao
from public.custom_exceptions import *
from public.project_variables import *

from models.product_factory import ProductFactory

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.get('/update_product')
async def update_product(prod_id: str, request: Request):
        
    if not prod_id:
        raise HTTPException(status_code=401, detail="Missing parameter")

    with YahooApiDao() as master_dao:
        
        master_dao.get_biggo_prod_main(prod_id)

        try:
            row = master_dao.fetchone()
            while row:
                obj = {
                        "prod_id":row["PRODID"], 
                        "org_prod_id":row["ORGPRODID"], 
                        "title_main":row["TITLEMAIN"],
                        "title_next":row["TITLENEXT"],
                        "prod_cat_id":row["PRODCATID"],
                        "cat_id":row["CATID"],
                        "cat_name":row["CATNAME"],
                        "list_price":row["LISTPRICE"],
                        "special_price":row["SPECIALPRICE"],
                        "sale_price":row["SALEPRICE"],
                        "sale_disc":row["SALEDISC"],
                        "pub_name":row["PUBNMMAIN"],
                        "publish_date":row["PUBLISHDATE"],
                        "ean_code":row["EANCODE"],
                        "isbn":row["ISBN"],
                        "org_name":row["ORGFLG"],
                        "language":row["LANGUAGE"],
                        "binding_type":row["BINDINGTYPE"],
                        "author":row["AUTHOR"],
                        "translator":row["TRANSLATOR"],
                        "painter":row["PAINTER"],
                        "author_pf":row["AUTHORPF"],
                        "prod_pf":row["PRODPF"],
                        "prod_sale_qty":row["SALE_QTY"],
                        "prod_sale_qty_30":row["SALE_QTY_30"],
                        "prod_sale_qty_7":row["SALE_QTY_7"],
                        "image_cover":row["IMAGE_COVER"],
                        "stock":row["STOCK"],
                        "adoflg":row["ADO_FLG"],
                        }

            
                row = master_dao.fetchone()
        except Exception as e:
            error, = e.args
          
            logging.error(error)
            msg_log = "update_product FAIL : %s" % (error) 
            logging.info(msg_log)
            obj = {
                    "RETURNCODE":"1001", 
                    "RETURNMSG":error
                    }
            return obj

    return obj


settingLog()