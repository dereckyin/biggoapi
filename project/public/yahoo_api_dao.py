import cx_Oracle
from .oracle_utils import OracleUtils

class YahooApiDao(OracleUtils):
    READY_TO_SHIP_STATUS = 'READY_TO_SHIP'

    def __enter__(self):
        self.initiate_connection()
        print('initiating connection')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('terminating connection')
        self.terminate_connection()

    def execute_custom_query(self, query):
        result = None
        try:
            result = self.execute_query(query)
            self.con.commit()
            return result

        except cx_Oracle.DatabaseError as e:
            self.con.rollback()
            print(e)
            raise e

    def execute_custom_non_query(self, query):
        try:
            self.execute_non_query(query)
            self.con.commit()

        except Exception as e:
            self.con.rollback()
            raise e

    def update_yahoo_sp_detail_cancel(self, receiptId='',
                                    resultFlg=''):
        sql = f"""
            UPDATE APP_YAHOO_SP_DETAIL SET
                SP_CANCEL_FLG = '{resultFlg}',
                SP_CANCEL_TIME = SYSDATE
            WHERE DELIVERYRECEIPTID = '{receiptId}'
        """
        self.execute_non_query(sql)
    
    def update_yahoo_sp_main_cancel(self, receiptId='',
                                    resultFlg=''):
        sql = f"""
            UPDATE APP_YAHOO_SP_MAIN SET
                SP_CANCEL_FLG = '{resultFlg}',
                SP_CANCEL_TIME = SYSDATE
            WHERE DELIVERYRECEIPTID = '{receiptId}'
        """
        self.execute_non_query(sql)

    def update_yahoo_sp_main_home(self, 
                            sp_no = '',
                            resultFlg = '',
                            ):
        sql = f"""
            UPDATE APP_YAHOO_SP_MAIN SET
                SP_CONFIRM_FLG = '{resultFlg}',
                SP_CONFIRM_TIME = SYSDATE
            WHERE SP_NO = '{sp_no}'
        """
        self.execute_non_query(sql)

    def update_yahoo_sp_detail_home_fail(self, 
                            sp_no = '',
                            OrderId = '',
                            ):
        sql = f"""
            UPDATE APP_YAHOO_SP_DETAIL SET
                SP_CONFIRM_FLG = 'D',
                SP_CONFIRM_TIME = SYSDATE
            WHERE SP_NO = '{sp_no}' AND ORDERID = '{OrderId}'
        """
        self.execute_non_query(sql)

    def update_yahoo_sp_detail_home(self, 
                            sp_no = '',
                            shippingNo = '',
                            OrderId = '',
                            ):
        sql = f"""
            UPDATE APP_YAHOO_SP_DETAIL SET
                SHIPPINGNUMBER = '{shippingNo}',
                SP_CONFIRM_FLG = 'H',
                SP_CONFIRM_TIME = SYSDATE
            WHERE SP_NO = '{sp_no}' AND ORDERID = '{OrderId}'
        """
        self.execute_non_query(sql)

    def update_yahoo_sp_main_fail(self, 
                            sp_no = '',
                            status = 'F',
                            ):
        sql = f"""
            UPDATE APP_YAHOO_SP_MAIN SET
                SP_CONFIRM_FLG = '{status}',
                SP_CONFIRM_TIME = SYSDATE
            WHERE SP_NO = '{sp_no}'
        """
        self.execute_non_query(sql)

    def update_yahoo_sp_detail_fail(self, 
                            sp_no = '',
                            status = 'F',
                            ):
        sql = f"""
            UPDATE APP_YAHOO_SP_DETAIL SET
                SP_CONFIRM_FLG = '{status}',
                SP_CONFIRM_TIME = SYSDATE
            WHERE SP_NO = '{sp_no}'
        """
        self.execute_non_query(sql)

    def update_sp_main_fail(self, 
                            sp_no = '',
                            status = 'F',
                            ):
        sql = f"""
            UPDATE SP_MAIN SET
                MALL_SP_ASK = '{status}'
            WHERE SP_NO = '{sp_no}'
        """
        self.execute_non_query(sql)

    def update_sp_main(self, 
                            sp_no = '',
                            Id = '',
                            _ReceiverName = '',
                            _TakeDeliveryConvenienceStoreName = '',
                            TakeDeliveryConvenienceStoreId = '',
                            Barcode = '',
                            DeliveryToConvenienceStoreDate = '',
                            ConvenienceStoreReturnDate = '',
                            ConvenienceStoreOrderId = '',
                            _StoreName = '',
                            _CustomerCareInfo = '',
                            _Url = '',
                            StoreRegion = '',
                            StoreRoute = '',
                            StoreRouteTrim = '',
                            _QrCode = '',
                            ):
        sql = f"""
            UPDATE SP_MAIN SET
                MALL_SP_NO = '{Id}',
                RCV_NM = '{_ReceiverName}',
                STNM = '{_TakeDeliveryConvenienceStoreName}',
                STNO = '{TakeDeliveryConvenienceStoreId}',
                MALL_BARCODE = '{Barcode}',
                DCQCBC = '{Barcode}',
                STINDT = '{DeliveryToConvenienceStoreDate.replace("/", "")}',
                STOUTDT = '{ConvenienceStoreReturnDate.replace("/", "")}',
                DLV_OD_ID = '{ConvenienceStoreOrderId}',
                MALL_SUP_NM = '{_StoreName}',
                MALL_SUP_CS_INF = '{_CustomerCareInfo}',
                MALL_SUP_URL = '{_Url}',
                STAREA = '0' + '{StoreRegion}',
                DCRONO = '{StoreRoute + StoreRouteTrim}',
                CVS_RSNO = '{StoreRoute + StoreRouteTrim}',
                SP_QRCODE = '{_QrCode}',
                MALL_SP_ASK = 'C'
            WHERE SP_NO = '{sp_no}'
        """
        self.execute_non_query(sql)

    def update_sp_main_hilife(self, 
                            sp_no = '',
                            Id = '',
                            _ReceiverName = '',
                            _TakeDeliveryConvenienceStoreName = '',
                            TakeDeliveryConvenienceStoreId = '',
                            Barcode = '',
                            DeliveryToConvenienceStoreDate = '',
                            ConvenienceStoreReturnDate = '',
                            ConvenienceStoreOrderId = '',
                            _StoreName = '',
                            _CustomerCareInfo = '',
                            _Url = '',
                            StoreRegion = '',
                            StoreRoute = '',
                            StoreRouteTrim = '',
                            _QrCode = '',
                            ):
        sql = f"""
            UPDATE SP_MAIN SET
                MALL_SP_NO = '{Id}',
                RCV_NM = '{_ReceiverName}',
                STNM = '{_TakeDeliveryConvenienceStoreName}',
                STNO = '{TakeDeliveryConvenienceStoreId}',
                MALL_BARCODE = '{Barcode}',
                DCQCBC = '{Barcode}',
                STINDT = '{DeliveryToConvenienceStoreDate.replace("/", "")}',
                STOUTDT = '{ConvenienceStoreReturnDate.replace("/", "")}',
                DLV_OD_ID = '{ConvenienceStoreOrderId}',
                MALL_SUP_NM = '{_StoreName}',
                MALL_SUP_CS_INF = '{_CustomerCareInfo}',
                MALL_SUP_URL = '{_Url}',
                STAREA = '0' + '{StoreRegion}',
                DCRONO = '{StoreRoute}',
                CVS_RSNO = '{StoreRouteTrim}',
                SP_QRCODE = '{_QrCode}',
                MALL_SP_ASK = 'C'
            WHERE SP_NO = '{sp_no}'
        """
        self.execute_non_query(sql)

    def update_yahoo_sp_detail(self, 
                            sp_no = '',
                            TransactionId = '',
                            Id = '',
                            ):
        sql = f"""
            UPDATE APP_YAHOO_SP_DETAIL SET
                TRANSACTIONID = '{TransactionId}',
                DELIVERYRECEIPTID = '{Id}',
                SP_CONFIRM_FLG = 'H',
                SP_CONFIRM_TIME = SYSDATE
            WHERE SP_NO = '{sp_no}'
        """
        self.execute_non_query(sql)

    def update_yahoo_sp_main(self, 
                            sp_no = '',
                            TransactionId = '',
                            Id = '',
                            StoreType = '',
                            SerialNumber = '',
                            DeliveryReceiptPrice = '',
                            DistributionChannelStatus = '',
                            _DistributionChannelStatusDesc = '',
                            OrderShippingConfirmDate = '',
                            LastDeliveryDate = '',
                            OrderDelayShippingDate = '',
                            _ReceiverName = '',
                            _TakeDeliveryConvenienceStoreName = '',
                            TakeDeliveryConvenienceStoreId = '',
                            Barcode = '',
                            DeliveryToConvenienceStoreDate = '',
                            ConvenienceStoreReturnDate = '',
                            ConvenienceStoreOrderId = '',
                            _StoreName = '',
                            _CustomerCareInfo = '',
                            _Url = '',
                            FirstBarcode = '',
                            RoutingBarcode = '',
                            PickupEShopBarcode = '',
                            PickupCodBarcode = '',
                            PickupLogisticCode = '',
                            LogisticCode = '',
                            LogisticCheckSum = '',
                            _QrCode = '',
                            StoreEquimentId = '',
                            StoreRegion = '',
                            StoreRoute = '',
                            StoreRouteTrim = '',
                            _ReturnPeriod = '',
                            _ReturnType = '',
                            MobilePhone = '',
                            ConvenienceStoreId = '',
                            _ConvenienceStoreName = '',
                            OrderInformation = '',
                            LogisticOrderNumber = '',
                            DistributionCenter = '',
                            ):
        sql = f"""
            UPDATE APP_YAHOO_SP_MAIN SET
                TRANSACTIONID = '{TransactionId}',
                DELIVERYRECEIPTID = '{Id}',
                STORETYPE = '{StoreType}',
                SERIALNUMBER = '{SerialNumber}',
                DELIVERYRECEIPTPRICE = '{DeliveryReceiptPrice}',
                DISTRIBUTIONCHANNELSTATUS = '{DistributionChannelStatus}',
                DISTRIBUTIONCHANNELSTATUSDESC = '{_DistributionChannelStatusDesc}',
                ORDERSHIPPINGCONFIRMDATE = '{OrderShippingConfirmDate.replace("/", "")}',
                LASTDELIVERYDATE = '{LastDeliveryDate.replace("/", "")}',
                ORDERDELAYSHIPPINGDATE = '{OrderDelayShippingDate.replace("/", "")}',
                RECEIVERNAME = '{_ReceiverName}',
                TAKEDELIVERYCONVENIENCESTNM = '{_TakeDeliveryConvenienceStoreName}',
                TAKEDELIVERYCONVENIENCESTID = '{TakeDeliveryConvenienceStoreId}',
                BARCODE = '{Barcode}',
                DELIVERYTOCONVENIENCESTOREDATE = '{DeliveryToConvenienceStoreDate.replace("/", "")}',
                CONVENIENCESTORERETURNDATE = '{ConvenienceStoreReturnDate.replace("/", "")}',
                CONVENIENCESTOREORDERID = '{ConvenienceStoreOrderId}',
                STORENAME = '{_StoreName}',
                CUSTOMERCAREINFO = '{_CustomerCareInfo}',
                URL = '{_Url}',
                FIRSTBARCODE = '{FirstBarcode}',
                ROUTINGBARCODE = '{RoutingBarcode}',
                PICKUPESHOPBARCODE = '{PickupEShopBarcode}',
                PICKUPCODBARCODE = '{PickupCodBarcode}',
                PICKUPLOGISTICCODE = '{PickupLogisticCode}',
                LOGISTICCODE = '{LogisticCode}',
                LOGISTICCHECKSUM = '{LogisticCheckSum}',
                QRCODE = '{_QrCode}',
                STOREEQUIMENTID = '{StoreEquimentId}',
                STOREREGION = '{StoreRegion}',
                STOREROUTE = '{StoreRoute}',
                STOREROUTETRIM = '{StoreRouteTrim}',
                RETURNPERIOD = '{_ReturnPeriod}',
                RETURNTYPE = '{_ReturnType}',
                MOBILEPHONE = '{MobilePhone}',
                CONVENIENCESTOREID = '{ConvenienceStoreId}',
                CONVENIENCESTORENAME = '{_ConvenienceStoreName}',
                ORDERINFORMATION = '{OrderInformation}',
                LOGISTICORDERNUMBER = '{LogisticOrderNumber}',
                DISTRIBUTIONCENTER = '{DistributionCenter}', 
                CUSTOMERINFORMATION = '(02)7722-9966 / TW.MALL.YAHOO.COM',
                REMARK = '請收款結帳',
                OFFICIALNAME = '雅虎奇摩', 			
                SP_CONFIRM_FLG = 'H',
                SP_CONFIRM_TIME = SYSDATE
            WHERE SP_NO = '{sp_no}'
        """
        self.execute_non_query(sql)

    def update_yahoo_product(self, yahoo_prod_id, prod_id):
        sql = """
            UPDATE APP_YAHOO_PRODUCT SET PROD_ID_YHO = '%s' , UPD_TIME = SYSDATE WHERE PROD_ID = '%s'
        """
        self.execute_non_query(sql % (str(yahoo_prod_id), str(prod_id)))

    def update_yahoo_image_list(self, yahoo_prod_id, prod_id, is_success=0):
        sql = """
            UPDATE APP_YAHOO_PRODUCT SET 
                                IMAGELIST = %s, IMAGELIST_TIME = SYSDATE
                                WHERE
                                PROD_ID = '%s' AND PROD_ID_YHO = '%s'
        """
        self.execute_non_query(sql % (str(is_success), str(prod_id), str(yahoo_prod_id)))

    def update_yahoo_tmp_0818(self, yahoo_prod_id, prod_id):
        sql = """
            UPDATE APP_YAHOO_PRODUCT SET PROD_ID_YHO = '%s' , UPD_TIME = SYSDATE WHERE PROD_ID = '%s'
        """
        self.execute_non_query(sql % (str(yahoo_prod_id), str(prod_id)))

    def insert_into_tmp_0818(self, prod_id):
        sql = """
            INSERT INTO APP_YAHOO_TMP_0818 VALUES ('%s', 'NULL', '2150', 'A')
        """

        self.execute_non_query(sql % (prod_id))

    def insert_yahoo_product(self, prodId, mdfTime, catId, catIdYho, rank, prodIds):
        sql = """
                INSERT INTO app_yahoo_product
                    VALUES     
                    ('%s',
                    To_date('%s', 'YYYYMMDDHH24MISS'),
                    '%s',
                    NULL,
                    '%s',
                    '%s',
                    ( To_char(SYSDATE, 'YYMMDD')
                    ||'%s' ),
                    SYSDATE,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    'N') """

        self.execute_non_query(sql % (prodId, mdfTime, catId, catIdYho, rank, prodIds))

    def get_yahoo_sp_main(self, spNo, as_dict=True):
        sql = """
            SELECT * FROM APP_YAHOO_SP_MAIN WHERE SP_NO = '{0}'
        """

        self.execute_query(query=sql.format(spNo), as_dict=True)


    def get_biggo_prod_main(self, as_dict=True):
        sql = """
                select 
                p.prod_id prodid, p.org_prod_id orgprodid, p.title_main titlemain, p.title_next titlenext, p.prod_cat_id prodcatid, 
                case when  LENGTH(pm.cat_id) < 12 then '000000000000' WHEN (select cat_nm from cat4xsx where substr(cat_id,0,2) = substr(pm.cat_id,0,2) and prod_cat_id = pm.prod_cat_id and cat_level='1') is null THEN '000000000000' WHEN (select cat_nm from cat4xsx where substr(cat_id,0,4) = substr(pm.cat_id,0,4) and prod_cat_id = pm.prod_cat_id and cat_level='2') is null THEN RPAD(substr(pm.cat_id,0,2), 12,'0') ELSE RPAD(substr(pm.cat_id,0,4), 12,'0') end as catid,
                case when (select cat_nm from cat4xsx where substr(cat_id,0,4) = substr(pm.cat_id,0,4) and prod_cat_id = pm.prod_cat_id and cat_level='2') is null then '' else (select cat_nm from cat4xsx where substr(cat_id,0,4) = substr(pm.cat_id,0,4) and prod_cat_id = pm.prod_cat_id and cat_level='2') end as catname,
                p.list_price listprice, p.special_price specialprice, p.sale_price saleprice, p.sale_disc saledisc,
                pub.pub_nm_main pubnmmain, pm.publish_date publishdate, p.eancode eancode, pm.isbn isbn,
                p.org_flg orgflg, p.prod_rank, p.add_mark_flg,
                substr(pm.age_begin,0,2) age_begin, substr(pm.age_end,0,2) age_end, pb.language language, pb.binding_type bindingtype,
                pm.author_main author, pb.translator translator, pb.painter painter, pp.author_pf authorpf , pp.translator_pf translatorpf,
                pp.media_rcm mediarcm, pp.award_rec awardrec, pp.person_rcm personrcm, pp.sp_rec sprec, pp.person_guide personguide, 
                pp.prod_pf prodpf, pp.viewdata viewdata, pp.preface preface, pp.catalogue catalogue,
                pd.prod_color prodcolor,ec.sale_qty,ec.sale_qty_30,ec.sale_qty_7,
                case when (p.prod_cat_id = '81' and p.org_flg = 'C') then NVL((select distinct 1 from prod_image img where img.prod_id = p.sup_org_prod_id and status_flg = 'Y'),0)
                when  (p.prod_cat_id not in '81' and p.org_flg = 'C') then NVL((select distinct 1 from prod_image img where img.prod_id = p.org_prod_id and status_flg = 'Y'),0)
                else  NVL((select distinct 1 from prod_image img where img.prod_id = p.prod_id  and status_flg = 'Y'),0) end as image_cover,
                case when  (p.prod_cat_id in ('14','25','17','26')) then NVL((select 1 from product where prod_id = p.prod_id and forsale_flg = 'Y' and status_flg = 'Y'),0)
                else  NVL((select 1 from vstk a where a.prod_id = p.prod_id),0) end as stock,
                case when (p.prod_cat_id = '61' or p.prod_cat_id = '62') then (select prod_spec from prodinfo_dpm where org_prod_id = p.org_prod_id)
                when (p.prod_cat_id = '31' or p.prod_cat_id = '32') then (select prod_spec from prodinfo_av where org_prod_id = p.org_prod_id)
                else null end as prodspec,
                case when LENGTH(pm.cat_id) < 12 then '其他' when (select cat_nm from cat4xsx where substr(cat_id,0,2) = substr(pm.cat_id,0,2) and prod_cat_id = pm.prod_cat_id and cat_level='1') is null then '其他' else (select cat_nm from cat4xsx where substr(cat_id,0,2) = substr(pm.cat_id,0,2) and prod_cat_id = pm.prod_cat_id and cat_level = 1) end as catname1,
                pb.ADO_FLG
                from product p, prodinfo_main pm, publisher pub, prodinfo_book pb, prod_profile pp, prodinfo_dpm pd,ec_dtl ec
                where p.org_prod_id = pm.org_prod_id
                and pm.pub_id = pub.pub_id(+)
                and pm.org_prod_id = pb.org_prod_id(+)
                and pm.org_prod_id = pp.org_prod_id(+)
                and pm.org_prod_id = pd.org_prod_id(+)
                and pm.org_prod_id = ec.prod_id(+)
                and p.status_flg = 'Y'
                and pb.ADO_FLG <> 'N'
                order by p.prod_id asc
        """

        self.execute_query(query=sql, as_dict=True)


    def get_biggo_prod_main_daily(self, batch_date, end_date, as_dict=True):
        sql = """
                select 
                p.prod_id prodid, p.org_prod_id orgprodid, p.title_main titlemain, p.title_next titlenext, p.prod_cat_id prodcatid, 
                case when  LENGTH(pm.cat_id) < 12 then '000000000000' WHEN (select cat_nm from cat4xsx where substr(cat_id,0,2) = substr(pm.cat_id,0,2) and prod_cat_id = pm.prod_cat_id and cat_level='1') is null THEN '000000000000' WHEN (select cat_nm from cat4xsx where substr(cat_id,0,4) = substr(pm.cat_id,0,4) and prod_cat_id = pm.prod_cat_id and cat_level='2') is null THEN RPAD(substr(pm.cat_id,0,2), 12,'0') ELSE RPAD(substr(pm.cat_id,0,4), 12,'0') end as catid,
                (select cat_nm from cat4xsx where cat_id = pm.cat_id and prod_cat_id = pm.prod_cat_id) catname, 
                p.list_price listprice, p.special_price specialprice, p.sale_price saleprice, p.sale_disc saledisc,
                pub.pub_nm_main pubnmmain, pm.publish_date publishdate, p.eancode eancode, pm.isbn isbn,
                p.org_flg orgflg, p.prod_rank, p.add_mark_flg,
                substr(pm.age_begin,0,2) age_begin, substr(pm.age_end,0,2) age_end, pb.language language, pb.binding_type bindingtype,
                pm.author_main author, pb.translator translator, pb.painter painter, pp.author_pf authorpf , pp.translator_pf translatorpf,
                pp.media_rcm mediarcm, pp.award_rec awardrec, pp.person_rcm personrcm, pp.sp_rec sprec, pp.person_guide personguide, 
                pp.prod_pf prodpf, pp.viewdata viewdata, pp.preface preface, pp.catalogue catalogue,
                pd.prod_color prodcolor,ec.sale_qty,ec.sale_qty_30,ec.sale_qty_7,
                case when (p.prod_cat_id = '81' and p.org_flg = 'C') then NVL((select distinct 1 from prod_image img where img.prod_id = p.sup_org_prod_id and status_flg = 'Y'),0)
                when  (p.prod_cat_id not in '81' and p.org_flg = 'C') then NVL((select distinct 1 from prod_image img where img.prod_id = p.org_prod_id and status_flg = 'Y'),0)
                else  NVL((select distinct 1 from prod_image img where img.prod_id = p.prod_id  and status_flg = 'Y'),0) end as image_cover,
                case when  (p.prod_cat_id in ('14','25','17','26')) then NVL((select 1 from product where prod_id = p.prod_id and forsale_flg = 'Y' and status_flg = 'Y'),0)
                else  NVL((select 1 from vstk a where a.prod_id = p.prod_id),0) end as stock,
                case when (p.prod_cat_id = '61' or p.prod_cat_id = '62') then (select prod_spec from prodinfo_dpm where org_prod_id = p.org_prod_id)
                when (p.prod_cat_id = '31' or p.prod_cat_id = '32') then (select prod_spec from prodinfo_av where org_prod_id = p.org_prod_id)
                else null end as prodspec,
                case when LENGTH(pm.cat_id) < 12 then '其他' when (select cat_nm from cat4xsx where substr(cat_id,0,2) = substr(pm.cat_id,0,2) and prod_cat_id = pm.prod_cat_id and cat_level='1') is null then '其他' else (select cat_nm from cat4xsx where substr(cat_id,0,2) = substr(pm.cat_id,0,2) and prod_cat_id = pm.prod_cat_id and cat_level = 1) end as catname1,
                pb.ADO_FLG
                from product p, prodinfo_main pm, publisher pub, prodinfo_book pb, prod_profile pp, prodinfo_dpm pd,ec_dtl ec
                where p.org_prod_id = pm.org_prod_id
                and pm.pub_id = pub.pub_id(+)
                and pm.org_prod_id = pb.org_prod_id(+)
                and pm.org_prod_id = pp.org_prod_id(+)
                and pm.org_prod_id = pd.org_prod_id(+)
                and pm.org_prod_id = ec.prod_id(+)
                and p.status_flg = 'Y'
                AND (
                (TO_CHAR(P.CRT_TIME, 'yyyymmdd') >= '{0}' AND TO_CHAR(P.CRT_TIME, 'yyyymmdd') < '{1}')
                 OR (TO_CHAR(P.MDF_TIME, 'yyyymmdd') >= '{0}' AND TO_CHAR(P.MDF_TIME, 'yyyymmdd') < '{1}')
                 OR (TO_CHAR(P.SALE_LAST_TIME, 'yyyymmdd') >= '{0}' AND TO_CHAR(P.SALE_LAST_TIME, 'yyyymmdd') < '{1}')
                )
                and SUBSTR(p.prod_id,1,3) in ('111')
                order by p.prod_id asc
        """

        self.execute_query(query=sql.format(batch_date, end_date), as_dict=True)

    def get_yahoo_sp_detail(self, spNo, as_dict=True):
        sql = """
            SELECT 
                SPD.ORDERID AS ORDERID, 
                OD.TRANSACTIONID AS TRANSACTIONID, 
                SPD.SHIPPINGNUMBER AS SHIPPINGNUMBER 
            FROM APP_YAHOO_SP_DETAIL SPD, APP_YAHOO_OD_DETAIL OD WHERE 
                SPD.ORDERID = OD.ORDERID 
                AND SPD.SP_NO = '{0}'
        """

        self.execute_query(query=sql.format(spNo), as_dict=True)

    def get_yahoo_category(self):
        sql = """
            SELECT
                CAT_ID,
                PROD_CAT_ID,
                CAT_NM,
                YAHOO_CAT_ID,
                YAHOO_CAT_NM,
                STATUS_FLG
            FROM
                APP_YAHOO_CATEGORY_MAPPING
        """

        self.execute_query(sql, as_dict=True)

    def get_yahoo_product(self, catId, prodId):
        sql = """
            SELECT P.PROD_ID, p.title_main       title_main,
                    p.list_price       list_price,
                    p.sale_price       sale_price,
                    pm.publish_date AS publish_date,
                    p.org_prod_id   AS org_prod_id,
                    pm.isbn         AS isbn,
                    pb.author_main  AS author_main,
                    pb.translator   AS translator,
                    Decode(pb.binding_type,
                            'A','平裝',
                            'B','盒裝',
                            'C','特殊裝訂',
                            'D','軟皮裝訂',
                            'E','軟精裝',
                            'F','精裝',
                            'G','線裝',
                            'H','螺旋裝',
                            'I','有聲CD',
                            'J','有聲卡帶',
                            'K','有聲MP3',
                            'L','其他',
                            'O','WMA',
                            'P','PDF',
                            'Q','ePub',
                            'R','keb',
                            NULL)     AS binding_type,
                    pp.prod_pf       AS prod_pf,
                    pp.author_pf     AS author_pf,
                    pp.viewdata      AS viewdata,
                    pp.catalogue     AS catalogue,
                    pp.translator_pf AS translator_pf,
                    pub.pub_nm_main     pub_nm_main,
                    p.note           AS note,
                    (
                            SELECT cat_id_yho
                            FROM   app_yahoo_sc_map
                            WHERE  prod_cat_id = '{0}'
                            AND    cat_id = Substr(pm.cat_id,0,4)) cat_id_yho_cust1,
                    (
                                SELECT   rtrim(xmlagg(XMLELEMENT("CAT", cat_id_yho_cust
                                                ||',')).extract('/cat/text()'),',') scorelist
                                FROM     app_yahoo_tmp_0818
                                WHERE    prod_id = p.prod_id
                                GROUP BY prod_id)    cat_id_yho_cust2,
                    pm.size_l                  AS size_l,
                    pm.size_w                  AS size_w,
                    pm.size_h                  AS size_h,
                    pd.prod_color              AS prod_color,
                    pd.prod_size               AS prod_size,
                    p.add_mark_flg             AS add_mark_flg,
                    p.org_flg,
                    p.prod_rank,
                    decode(p.prod_rank,
                            'A','全新品',
                            'B','近全新',
                            'C','良好',
                            'D','普通',
                            'E','差強人意') AS rank_desc,
                    p.vdo_nm,
                    p.logcode,
                    pm.TAX_FREE_FLG,
                    PM.RANK
                FROM   product p,
                    prodinfo_main pm,
                    prodinfo_book pb,
                    prod_profile pp,
                    publisher pub,
                    prodinfo_dpm pd
                WHERE  p.org_prod_id = pm.org_prod_id
                AND    pm.org_prod_id = pb.org_prod_id(+)
                AND    pm.org_prod_id = pp.org_prod_id(+)
                AND    pm.pub_id = pub.pub_id(+)
                AND    pm.org_prod_id = pd.org_prod_id(+)
                AND    p.prod_id = '{1}'
        """

        self.execute_query(query=sql.format(catId, prodId), as_dict=True)

    def get_daily_products_to_upload(self):
        sql = """
            SELECT
                p.prod_id
            FROM
                PRODINFO_MAIN PM,
                PRODUCT P,
                vstk v
            WHERE PM.ORG_PROD_ID=P.ORG_PROD_ID
        and p.prod_id = v.prod_id
        AND P.STATUS_FLG='Y'
        AND P.PROD_CAT_ID IN ('11')
        AND P.ORG_FLG IN ('A', 'B', 'C')
        AND (
        (P.CRT_TIME >= trunc(SYSDATE-1) AND P.CRT_TIME < trunc(SYSDATE))
         OR (P.MDF_TIME >= trunc(SYSDATE-1) AND P.MDF_TIME < trunc(SYSDATE))
         OR (P.SALE_LAST_TIME >= trunc(SYSDATE-1) AND P.SALE_LAST_TIME < trunc(SYSDATE))
        )
        and SUBSTR(p.prod_id,1,3) in ('113')
        and NVL(v.qty, 0) > 0
        AND (PM.RANK != 'D' OR PM.RANK is NULL)
        and p.prod_id not in(select prod_id from app_shopee_product)
        and p.org_prod_id not in (select prod_id from shopee_blacklist)
        and p.SO_CN_CDT not in ('HA', 'HH', 'HN', 'HS')
        and p.Sale_Price < 20000
        and p.prod_rank in ('C')
        and rownum < 100
        """

        result = None
        try:
            result = self.execute_query(sql)
            self.con.commit()
            return [x[0] for x in result]

        except cx_Oracle.DatabaseError as e:
            self.con.rollback()
            raise e

    def get_products_by_date_and_type_test(self, delta_date=1, type_list=['111'], as_dict=False):
        sql = """
            SELECT
                P.TITLE_MAIN,
                P.ISBN,
                P.EANCODE,
                P.PROD_SERIALNO,
                P.PROD_ID,
                SUP.SUP_NM_MAIN,
                PM.AUTHOR_MAIN,
                PB.AUTHOR_NEXT,
                PB.TRANSLATOR,
                PB.EDITOR,
                PB.PAINTER,
                PUB.PUB_NM_MAIN,
                PUB.PUB_NM_NEXT,
                P.PUBLISH_DATE,
                P.LIST_PRICE,
                P.SPECIAL_PRICE,
                (CASE   WHEN PB.LANGUAGE = '01' THEN '繁體/中文'
                    WHEN PB.LANGUAGE = '02' THEN '簡體/中文'
                    WHEN PB.LANGUAGE = '03' THEN '日文'
                    WHEN PB.LANGUAGE = '04' THEN '韓文'
                    WHEN PB.LANGUAGE = '05' THEN '泰文'
                    WHEN PB.LANGUAGE = '06' THEN '英文'
                    WHEN PB.LANGUAGE = '07' THEN '法文'
                    WHEN PB.LANGUAGE = '08' THEN '德文'
                    WHEN PB.LANGUAGE = '09' THEN '西文'
                    WHEN PB.LANGUAGE = '10' THEN '拉丁語'
                    WHEN PB.LANGUAGE = '11' THEN '阿拉伯文'
                    WHEN PB.LANGUAGE = '12' THEN '俄文'
                    WHEN PB.LANGUAGE = '13' THEN '義大利文'
                    WHEN PB.LANGUAGE = '14' THEN '荷文'
                    WHEN PB.LANGUAGE = '15' THEN '瑞典文'
                    WHEN PB.LANGUAGE = '16' THEN '葡萄牙文'
                    WHEN PB.LANGUAGE = '17' THEN '印尼文'
                    WHEN PB.LANGUAGE = '18' THEN '比利時文'
                    WHEN PB.LANGUAGE = '19' THEN '波蘭文'
                    WHEN PB.LANGUAGE = '20' THEN '緬甸文'
                    WHEN PB.LANGUAGE = '21' THEN '土耳其文'
                    ELSE '' END) LANGUAGE,
                (CASE   WHEN PM.RANK = 'A' THEN '普'
                    WHEN PM.RANK = 'B' THEN '保'
                    WHEN PM.RANK = 'C' THEN '輔'
                    WHEN PM.RANK = 'D' THEN '限'
                    ELSE '普' END) RANK,
                (SELECT SERIES4PUB.SERIES4PUB_NM FROM SERIES4PUB WHERE SERIES4PUB.PUB_ID = PM.PUB_ID AND SERIES4PUB.SERIES4PUB_ID = PM.SERIES4PUB_ID AND ROWNUM = 1) SERIES4PUB_NM,
                PP.PROD_PF,
                --PP.AUTHOR_PF,
                PP.TRANSLATOR_PF,
                PP.CATALOGUE,
                PP.PREFACE,
                PP.VIEWDATA,
                PB.PAGES,
                --PB.BOOK_SIZE,
                PM.WEIGHT,
                PM.SIZE_L,
                PM.SIZE_W,
                PM.SIZE_H,
                (CASE   WHEN PB.BINDING_TYPE = 'A' THEN '平裝'
                        WHEN PB.BINDING_TYPE = 'B' THEN '盒裝'
                        WHEN PB.BINDING_TYPE = 'E' THEN '軟精裝'
                        WHEN PB.BINDING_TYPE = 'F' THEN '精裝'
                        ELSE '平裝' END) BINDING_TYPE,
                (CASE   WHEN PB.PRINTING = 'A' THEN '單色印刷'
                        WHEN PB.PRINTING = 'B' THEN '雙色印刷'
                        WHEN PB.PRINTING = 'C' THEN '全彩印刷'
                        WHEN PB.PRINTING = 'D' THEN '部分全彩'
                        ELSE '未知' END) PRINTING,
                CP.COUNTRY_NM_CN,
                P.PROD_ID,
                (CASE   WHEN P.ORG_FLG = 'A' THEN '新品'
                        WHEN P.ORG_FLG = 'C' THEN '二手'
                        ELSE '' END) ORG_FLG,
                (CASE   WHEN P.RETN_FLG = 'Y' THEN '允許退貨'
                        WHEN P.RETN_FLG = 'N' THEN '不可退貨'
                        ELSE '' END) RETN_FLG,
                (CASE   WHEN P.PUR_TAX = 'A' THEN '應稅'
                        WHEN P.PUR_TAX = 'B' THEN '零稅'
                        WHEN P.PUR_TAX = 'C' THEN '免稅'
                        ELSE '' END) PUR_TAX,
                P.PUR_DISC,
                P.SALE_PRICE,
                P.SALE_DISC,
                (CASE   WHEN P.FORSALE_FLG = 'Y' THEN '是'
                        WHEN P.FORSALE_FLG = 'N' THEN '否'
                        ELSE '' END) FORSALE_FLG,
                (CASE   WHEN PM.FORSALE = 'Y' THEN '是'
                        WHEN PM.FORSALE = 'N' THEN '否'
                        ELSE '' END) FORSALE,
                (CASE   WHEN PM.OUT_OF_PRINT = 'Y' THEN '是'
                        WHEN PM.OUT_OF_PRINT = 'N' THEN '否'
                        ELSE '' END) OUT_OF_PRINT,
                (CASE   WHEN P.STK_SELL_FLG = 'Y' THEN '是'
                        WHEN P.STK_SELL_FLG = 'N' THEN '否'
                        ELSE '' END) STK_SELL_FLG,
                (CASE   WHEN PM.SUP_MODE = 'A' THEN '正常供貨'
                        WHEN PM.SUP_MODE = 'B' THEN '有貨通知'
                        ELSE '' END) SUP_MODE,
                (SELECT CASE WHEN ISLIMIT_FLG = 'Y' THEN '是' WHEN ISLIMIT_FLG = 'N' THEN '否' ELSE '否' END FROM MC_ITEM WHERE P.PROD_ID = MC_ITEM.PROD_ID AND ROWNUM=1 ) AS ISLIMIT_FLG,
                (CASE   WHEN PM.COPYRIGHT = 'Y' THEN '是'
                        WHEN PM.COPYRIGHT = 'N' THEN '否'
                        ELSE '' END) COPYRIGHT,
                (CASE   WHEN P.STATUS_FLG = 'D' THEN '是'
                        WHEN P.STATUS_FLG = 'Y' THEN '否'
                        ELSE '' END) STATUS_FLG,
                TO_CHAR(P.MDF_TIME, 'YYYYMMDDHHMMSS'),
                PP.MEDIA_RCM,
                PP.PERSON_RCM,
                P.SO_CN_CDT,
                NVL((SELECT CAT4XSX.CAT_NM FROM CAT4XSX WHERE CAT4XSX.CAT_ID = PM.CAT_ID  AND ROWNUM = 1), '其他') CAT_NM,
                NVL(PM.CAT_ID, '000000000000') CAT_ID,
                NVL(V.QTY, 0) VAL,
                NVL((SELECT CAT4XSX.CAT_NM FROM CAT4XSX WHERE CAT4XSX.CAT_ID = CONCAT(SUBSTR(PM.CAT_ID, 1, 2), '0000000000') AND ROWNUM = 1), '其他') CAT_NAME,
                (CASE   WHEN P.PROD_RANK = 'A' THEN '全新'
                        WHEN P.PROD_RANK = 'B' THEN '近全新'
                        WHEN P.PROD_RANK = 'C' THEN '良好'
                        WHEN P.PROD_RANK = 'D' THEN '普通'
                        WHEN P.PROD_RANK = 'C' THEN '差強人意'
                        ELSE '' END) PROD_RANK,
                P.NOTE,
                P.ORG_PROD_ID,
                P.PUB_ID,
                SPM.PUB_SPE_NM
            FROM 
                PRODINFO_MAIN PM, 
                PRODUCT P, 
                PUBLISHER PUB, 
                PRODINFO_BOOK PB, 
                PROD_PROFILE PP, 
                SUPPLIER SUP, 
                COUNTRY_PAMT CP, 
                VSTK V, 
                APP_SHOPEE_PUBLISHER_MAPPING SPM
            WHERE 
                PM.ORG_PROD_ID=P.ORG_PROD_ID
                AND PM.ORG_PROD_ID=PB.ORG_PROD_ID(+)
                AND PM.PUB_ID=PUB.PUB_ID(+)
                AND P.SUP_ID = SUP.SUP_ID(+)
                AND PB.COUNTRY_ID = CP.COUNTRY_ID(+)
                AND PM.ORG_PROD_ID=PP.ORG_PROD_ID(+)
                AND P.PROD_ID = V.PROD_ID(+)
                AND SPM.PUB_ID(+)=P.PUB_ID
                AND P.STATUS_FLG='Y'
                AND P.PROD_CAT_ID IN ('11')
                AND P.ORG_FLG IN ('A', 'B', 'C')
                --AND (
                --(P.CRT_TIME >= TRUNC(SYSDATE-{0}) AND P.CRT_TIME < TRUNC(SYSDATE-{1}))
                --OR (P.MDF_TIME >= TRUNC(SYSDATE-{0}) AND P.MDF_TIME < TRUNC(SYSDATE-{1}))
                --OR (P.SALE_LAST_TIME >= TRUNC(SYSDATE-{0}) AND P.SALE_LAST_TIME < TRUNC(SYSDATE-{1}))
                --)
                AND SUBSTR(P.PROD_ID,1,3) IN ({2})
                AND NVL(V.QTY, 0) > 0
                AND (PM.RANK != 'D' OR PM.RANK IS NULL)
                AND NOT EXISTS(SELECT * FROM APP_SHOPEE_PRODUCT SP WHERE SP.PROD_ID = P.PROD_ID)
                AND NOT EXISTS(SELECT * FROM SHOPEE_BLACKLIST BLK WHERE BLK.PROD_ID = P.ORG_PROD_ID AND BLK.REASON != '下載失敗')
                AND P.SO_CN_CDT NOT IN ('HA', 'HH', 'HN', 'HS')
                AND P.SALE_PRICE < 20000
                AND P.PROD_RANK IN ('A', 'B', 'C')
                AND P.PROD_ID IN ('11100858175',
'11100888418',
'11100893162',
'11100903062',
'11100914381',
'11100923360',
'11100925697',
'11100929845',
'11100931734',
'11100931735',
'11100931986',
'11100932832',
'11100932969',
'11100933165',
'11100933917',
'11100934496',
'11100934500',
'11100934501',
'11100934599',
'11100935041',
'11100935051',
'11100935371',
'11100935382',
'11100935604',
'11100935608',
'11100936287',
'11100936293')
                """
        
        self.execute_query(query=sql.format(delta_date, delta_date-1, ','.join([f"'{x}'" for x in type_list])), 
                            as_dict=as_dict)

    def get_products_by_date_and_type(self, type_list=['111'], as_dict=False):
        sql = """
            SELECT P.prod_id,
                to_char(P.mdf_time, 'YYYYMMDDHH24MISS') mdf_time,
                PM.cat_id,
                PM.rank,
                Substr(P.prod_id, 0, 3) prodIds
            FROM   product P,
                prodinfo_main PM,
                vstk V
            WHERE  P.prod_id = V.prod_id(+)
                AND P.org_prod_id = PM.org_prod_id
                AND Substr(P.prod_id, 0, 3) in ({0})
                AND V.qty > 0
                AND P.publish_date <= To_char(SYSDATE, 'YYYYMMDD')
                AND NOT EXISTS(SELECT 1
                                FROM   app_yahoo_product AYP01
                                WHERE  P.prod_id = AYP01.prod_id) 
        """
        
        self.execute_query(query=sql.format(','.join([f"'{x}'" for x in type_list])), 
                            as_dict=as_dict)

    def get_shopee_products_by_modify_date(self, delta_date, as_dict):
        sql = """
            SELECT
                P.TITLE_MAIN,
                P.ISBN,
                P.EANCODE,
                P.PROD_SERIALNO,
                P.TITLE_NEXT,
                SUP.SUP_NM_MAIN,
                PM.AUTHOR_MAIN,
                PB.AUTHOR_NEXT,
                PB.TRANSLATOR,
                PB.EDITOR,
                PB.PAINTER,
                PUB.PUB_NM_MAIN,
                PUB.PUB_NM_NEXT,
                P.PUBLISH_DATE,
                P.LIST_PRICE,
                P.SPECIAL_PRICE,
                (CASE   WHEN PB.LANGUAGE = '01' THEN '繁體/中文'
                        WHEN PB.LANGUAGE = '02' THEN '簡體/中文'
                        WHEN PB.LANGUAGE = '03' THEN '日文'
                        WHEN PB.LANGUAGE = '04' THEN '韓文'
                        WHEN PB.LANGUAGE = '05' THEN '泰文'
                        WHEN PB.LANGUAGE = '06' THEN '英文'
                        WHEN PB.LANGUAGE = '07' THEN '法文'
                        WHEN PB.LANGUAGE = '08' THEN '德文'
                        WHEN PB.LANGUAGE = '09' THEN '西文'
                        WHEN PB.LANGUAGE = '10' THEN '拉丁語'
                        WHEN PB.LANGUAGE = '11' THEN '阿拉伯文'
                        WHEN PB.LANGUAGE = '12' THEN '俄文'
                        WHEN PB.LANGUAGE = '13' THEN '義大利文'
                        WHEN PB.LANGUAGE = '14' THEN '荷文'
                        WHEN PB.LANGUAGE = '15' THEN '瑞典文'
                        WHEN PB.LANGUAGE = '16' THEN '葡萄牙文'
                        WHEN PB.LANGUAGE = '17' THEN '印尼文'
                        WHEN PB.LANGUAGE = '18' THEN '比利時文'
                        WHEN PB.LANGUAGE = '19' THEN '波蘭文'
                        WHEN PB.LANGUAGE = '20' THEN '緬甸文'
                        WHEN PB.LANGUAGE = '21' THEN '土耳其文'
                        ELSE '' END) LANGUAGE,
                (CASE   WHEN PM.RANK = 'A' THEN '普'
                        WHEN PM.RANK = 'B' THEN '保'
                        WHEN PM.RANK = 'C' THEN '輔'
                        WHEN PM.RANK = 'D' THEN '限'
                        ELSE '普' END) RANK,
                (SELECT SERIES4PUB.SERIES4PUB_NM FROM SERIES4PUB WHERE SERIES4PUB.PUB_ID = PM.PUB_ID AND SERIES4PUB.SERIES4PUB_ID = PM.SERIES4PUB_ID AND ROWNUM = 1) SERIES4PUB_NM,
                PP.PROD_PF,
                PP.AUTHOR_PF,
                PP.TRANSLATOR_PF,
                PP.CATALOGUE,
                PP.PREFACE,
                PP.VIEWDATA,
                PB.PAGES,
                PB.BOOK_SIZE,
                PM.WEIGHT,
                PM.SIZE_L,
                PM.SIZE_W,
                PM.SIZE_H,
                (CASE   WHEN PB.BINDING_TYPE = 'A' THEN '平裝'
                        WHEN PB.BINDING_TYPE = 'B' THEN '盒裝'
                        WHEN PB.BINDING_TYPE = 'E' THEN '軟精裝'
                        WHEN PB.BINDING_TYPE = 'F' THEN '精裝'
                        ELSE '平裝' END) BINDING_TYPE,
                (CASE   WHEN PB.PRINTING = 'A' THEN '單色印刷'
                        WHEN PB.PRINTING = 'B' THEN '雙色印刷'
                        WHEN PB.PRINTING = 'C' THEN '全彩印刷'
                        WHEN PB.PRINTING = 'D' THEN '部分全彩'
                        ELSE '未知' END) PRINTING,
                CP.COUNTRY_NM_CN,
                P.PROD_ID,
                (CASE   WHEN P.ORG_FLG = 'A' THEN '新品'
                        WHEN P.ORG_FLG = 'C' THEN '二手'
                        ELSE '' END) ORG_FLG,
                (CASE   WHEN P.RETN_FLG = 'Y' THEN '允許退貨'
                        WHEN P.RETN_FLG = 'N' THEN '不可退貨'
                        ELSE '' END) RETN_FLG,
                (CASE   WHEN P.PUR_TAX = 'A' THEN '應稅'
                        WHEN P.PUR_TAX = 'B' THEN '零稅'
                        WHEN P.PUR_TAX = 'C' THEN '免稅'
                        ELSE '' END) PUR_TAX,
                P.PUR_DISC,
                P.SALE_PRICE,
                P.SALE_DISC,
                (CASE   WHEN P.FORSALE_FLG = 'Y' THEN '是'
                        WHEN P.FORSALE_FLG = 'N' THEN '否'
                        ELSE '' END) FORSALE_FLG,
                (CASE   WHEN PM.FORSALE = 'Y' THEN '是'
                        WHEN PM.FORSALE = 'N' THEN '否'
                        ELSE '' END) FORSALE,
                (CASE   WHEN PM.OUT_OF_PRINT = 'Y' THEN '是'
                        WHEN PM.OUT_OF_PRINT = 'N' THEN '否'
                        ELSE '' END) OUT_OF_PRINT,
                (CASE   WHEN P.STK_SELL_FLG = 'Y' THEN '是'
                        WHEN P.STK_SELL_FLG = 'N' THEN '否'
                        ELSE '' END) STK_SELL_FLG,
                (CASE   WHEN PM.SUP_MODE = 'A' THEN '正常供貨'
                        WHEN PM.SUP_MODE = 'B' THEN '有貨通知'
                        ELSE '' END) SUP_MODE,
                (SELECT CASE WHEN ISLIMIT_FLG = 'Y' THEN '是' WHEN ISLIMIT_FLG = 'N' THEN '否' ELSE '否' END FROM MC_ITEM WHERE P.PROD_ID = MC_ITEM.PROD_ID AND ROWNUM=1 ) AS ISLIMIT_FLG,
                (CASE   WHEN PM.COPYRIGHT = 'Y' THEN '是'
                        WHEN PM.COPYRIGHT = 'N' THEN '否'
                        ELSE '' END) COPYRIGHT,
                (CASE   WHEN P.STATUS_FLG = 'D' THEN '是'
                        WHEN P.STATUS_FLG = 'Y' THEN '否'
                        ELSE '' END) STATUS_FLG,
                TO_CHAR(P.MDF_TIME, 'YYYYMMDDHHMMSS'),
                PP.MEDIA_RCM,
                PP.PERSON_RCM,
                P.SO_CN_CDT,
                NVL((SELECT CAT4XSX.CAT_NM FROM CAT4XSX WHERE CAT4XSX.CAT_ID = PM.CAT_ID  AND ROWNUM = 1), '其他') CAT_NM,
                NVL(PM.CAT_ID, '000000000000') CAT_ID,
                NVL(V.QTY, 0) VAL,
                NVL((SELECT CAT4XSX.CAT_NM FROM CAT4XSX WHERE CAT4XSX.CAT_ID = CONCAT(SUBSTR(PM.CAT_ID, 1, 2), '0000000000') AND ROWNUM = 1), '其他') CAT_NAME,
                (CASE   WHEN P.PROD_RANK = 'A' THEN '全新'
                        WHEN P.PROD_RANK = 'B' THEN '近全新'
                        WHEN P.PROD_RANK = 'C' THEN '良好'
                        WHEN P.PROD_RANK = 'D' THEN '普通'
                        WHEN P.PROD_RANK = 'C' THEN '差強人意'
                        ELSE '' END) PROD_RANK,
                P.FORSALE_FLG,
                SP.ITEM_ID,
                P.NOTE,
                P.PUR_LAST_TIME,
                PUB.PUB_ID,
                SPM.PUB_SPE_NM
            FROM 
                APP_SHOPEE_PRODUCT SP, 
                PRODINFO_MAIN PM, 
                PRODUCT P, 
                PUBLISHER PUB, 
                PRODINFO_BOOK PB, 
                PROD_PROFILE PP, 
                SUPPLIER SUP, 
                COUNTRY_PAMT CP, 
                VSTK V,
                APP_SHOPEE_PUBLISHER_MAPPING SPM
            WHERE 
                SP.PROD_ID = P.PROD_ID
                AND PM.ORG_PROD_ID=P.ORG_PROD_ID
                AND PM.ORG_PROD_ID=PB.ORG_PROD_ID(+)
                AND PM.PUB_ID=PUB.PUB_ID(+)
                AND P.SUP_ID = SUP.SUP_ID(+)
                AND PB.COUNTRY_ID = CP.COUNTRY_ID(+)
                AND PM.ORG_PROD_ID=PP.ORG_PROD_ID(+)
                AND P.PROD_ID = V.PROD_ID(+)
                AND SPM.PUB_ID(+)=P.PUB_ID
                --AND (
                --    (P.MDF_TIME >= TRUNC(SYSDATE-{0}))
                --     OR (P.SALE_LAST_TIME >= TRUNC(SYSDATE-{0}))
                --)
                AND P.MDF_TIME >= to_date('2021', 'YYYY')
        """
        
        # print(sql.format(delta_date))
        self.execute_query(query=sql.format(delta_date), as_dict=as_dict)

    def get_price_changed_items(self, delta_time=1/24):
        sql = """
                SELECT 
                    P.PROD_ID,
                    YP.PROD_ID_YHO,
                    P.LIST_PRICE,
                    P.SALE_PRICE
                FROM   
                    PRODUCT P,
                    APP_YAHOO_PRODUCT YP
                WHERE
                    YP.PROD_ID = P.PROD_ID
                    AND ( P.MDF_TIME >= ( SYSDATE - '%s' ) )
                ORDER BY
                    P.SALE_PRICE
        """

        self.execute_query(query=sql % delta_time, as_dict=True)

    def insert_order_income_details(self, ordersn, seller_return_refund_amount, is_completed, voucher_name, escrow_amount, final_shipping_fee, seller_coin_cash_back, coin, seller_rebate, cross_border_tax, commision_fee, buyer_shopee_kredit, shipping_fee_rebate, seller_transaction_fee, service_fee, voucher_code, credit_card_transaction_fee, total_amount, credit_card_promotion, buyer_transaction_fee, actual_shipping_cost, voucher_type, voucher, voucher_seller):
        sql = """INSERT INTO APP_SHOPEE_INCOME_DETAILS(ORDERSN, SELLER_RETURN_REFUND_AMOUNT, IS_COMPLETED, VOUCHER_NAME, ESCROW_AMOUNT, FINAL_SHIPPING_FEE, SELLER_COIN_CASH_BACK, COIN, SELLER_REBATE, CROSS_BORDER_TAX, COMMISION_FEE, BUYER_SHOPEE_KREDIT, SHIPPING_FEE_REBATE, SELLER_TRANSACTION_FEE, SERVICE_FEE, VOUCHER_CODE, CREDIT_CARD_TRANSACTION_FEE, TOTAL_AMOUNT, CREDIT_CARD_PROMOTION, BUYER_TRANSACTION_FEE, ACTUAL_SHIPPING_COST, VOUCHER_TYPE, VOUCHER, VOUCHER_SELLER)
                VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""

        # print(sql % (
        #     ordersn, 
        #     seller_return_refund_amount, 
        #     is_completed, 
        #     voucher_name, 
        #     escrow_amount, 
        #     final_shipping_fee, 
        #     seller_coin_cash_back, 
        #     coin, 
        #     seller_rebate, 
        #     cross_border_tax, 
        #     commision_fee, 
        #     buyer_shopee_kredit, 
        #     shipping_fee_rebate, 
        #     seller_transaction_fee, 
        #     service_fee, 
        #     voucher_code, 
        #     credit_card_transaction_fee, 
        #     total_amount, 
        #     credit_card_promotion, 
        #     buyer_transaction_fee, 
        #     actual_shipping_cost, 
        #     voucher_type, 
        #     voucher, 
        #     voucher_seller))

        try:
            self.execute_non_query(sql % (
                    ordersn, 
                    seller_return_refund_amount, 
                    is_completed, 
                    voucher_name, 
                    escrow_amount, 
                    final_shipping_fee, 
                    seller_coin_cash_back, 
                    coin, 
                    seller_rebate, 
                    cross_border_tax, 
                    commision_fee, 
                    buyer_shopee_kredit, 
                    shipping_fee_rebate, 
                    seller_transaction_fee, 
                    service_fee, 
                    voucher_code, 
                    credit_card_transaction_fee, 
                    total_amount, 
                    credit_card_promotion, 
                    buyer_transaction_fee, 
                    actual_shipping_cost, 
                    voucher_type, 
                    voucher, 
                    voucher_seller)
            )
            self.con.commit()

        except Exception as e:
            self.con.rollback()
            raise e


    def get_limit_item_promotion_stock(self, prod_id):
        sql = """
            SELECT
                LIMIT_INV
            FROM
                MC_ITEM
            WHERE
                PROD_ID = '%s' AND
                ISLIMIT_FLG = 'Y'
        """

        self.execute_query(sql % prod_id)

    def get_item_images(self, prod_id):
        sql = """
            SELECT
                PK_NO,
                PI.IMAGE
            from
                PRODINFO_MAIN PM,
                PRODUCT P,
                PROD_IMAGE PI
            WHERE
                PM.ORG_PROD_ID = PI.PROD_ID
                AND PM.ORG_PROD_ID=P.ORG_PROD_ID
                AND P.PROD_ID = '%s'
                ORDER BY FIELD_INDEX ASC
        """

        self.execute_query(sql % prod_id)

    def update_yahoo_stock_status(self, prod_id, status):
        sql = """
            UPDATE
                VSTK
            SET
                YAH_CHG_FLG = '%s'
            WHERE
                PROD_ID = '%s'
        """

        try:
            self.execute_non_query(sql % (status, str(prod_id)))
            self.con.commit()

        except Exception as e:
            self.con.rollback()
            raise e
    
    def update_shopee_item_mdf_time(self, item_id):
        sql = """
            UPDATE
                APP_SHOPEE_PRODUCT
            SET
                MDF_TIME = SYSDATE
            WHERE
                ITEM_ID = %s
        """

        try:
            self.execute_non_query(sql % (item_id))
            self.con.commit()

        except Exception as e:
            self.con.rollback()
            raise e

    def get_product_stock(self, prod_id):
        sql = """
            select
                NVL(v.qty, 0)
            from
                vstk v
            where
                v.prod_id = '%s'
        """

        self.execute_query(sql % prod_id)

    def get_stock_change_products(self, as_dict=True):
        sql = """
            SELECT 
                YP.PROD_ID_YHO,
                P.PROD_ID,
                NVL(V.QTY, 0) AS STOCK
            FROM   
                APP_YAHOO_PRODUCT YP,
                PRODUCT P,
                VSTK V
            WHERE  
                P.PROD_ID = V.PROD_ID(+)
                AND YP.PROD_ID = P.PROD_ID
                AND V.YAH_CHG_FLG = 'Y'
            ORDER BY 
                V.QTY ASC
        """

        self.execute_query(sql, as_dict)

    def is_product_exist(self, prod_id):
        sql = """
            SELECT
                *
            FROM
                APP_SHOPEE_PRODUCT
            WHERE
                PROD_ID = '%s'
        """

        return self.is_record_exists(sql % prod_id)

    def get_baihuo_product_data(self, prod_id):
        sql = """
            SELECT
                CAT_ID1,
                CAT_NM1
            FROM
                CAT_SPE_201012_ITEM
            WhERE
                PROD_ID = '%s'
        """

        return self.execute_and_retrieve_data(sql % prod_id)

    def get_baihuo_shopee_data(self, prod_id):
        sql = """
            SELECT
                *
            FROM
                APP_SHOPEE_PRODUCT
            WhERE
                PROD_ID = '%s'
        """

        return self.execute_and_retrieve_data(sql % prod_id)

    def update_item_promotion_id(self, ordersn, item_id, promotion_id, order_promotion_id):
        sql = """
            UPDATE
                APP_SHOPEE_ORDER_ITEM
            SET
                GP_ID = %s
            WHERE
                ORDERSN = '%s' AND
                ITEM_ID = %s AND
                PROMOTION_ID = '%s'
        """

        try:
            self.execute_non_query(sql % (order_promotion_id, ordersn, item_id, promotion_id))
            self.con.commit()

        except Exception as e:
            self.con.rollback()
            raise e

    def insert_item_into_blacklist(self, prod_id, item_id, message):
        sql = """
            INSERT INTO SHOPEE_BLACKLIST
                (PROD_ID, ITEM_ID, REASON)
            VALUES 
                ('%s', '%s', '%s')
        """

        self.execute_non_query(sql % (prod_id, item_id, message))

    def insert_promotion_items(self, ordersn, org_price, disc_price, bundle_type, activity_id, order_promotion_id):
        sql = """
            INSERT INTO
                APP_SHOPEE_ORDER_ACT (ORDERSN, ACTIVITY_ID, ACTIVITY_TYPE, ORIGINAL_PRICE, DISCOUNTED_PRICE, GP_ID, CRT_TIME, CRT_USER)
            VALUES
                ('%s', '%s', '%s', '%s', '%s', %s, sysdate, 'sys')
        """

        try:
            self.execute_non_query(sql % (ordersn, activity_id, bundle_type, org_price, disc_price, order_promotion_id))
            self.con.commit()

        except Exception as e:
            self.con.rollback()
            raise e

    def get_promotion_orders(self):
        sql = """
            SELECT
                DISTINCT(O.ORDERSN)
            FROM
                APP_SHOPEE_ORDER O,
                APP_SHOPEE_ORDER_ITEM OI
            WHERE
                O.ORDERSN = OI.ORDERSN AND
                OI.PROMOTION_TYPE = 'bundle_deal' AND
                O.ORDERSN NOT IN (SELECT ORDERSN FROM APP_SHOPEE_ORDER_ACT)
        """

        self.execute_query(sql)

    def get_images_by_product_id(self, prod_id):
        sql = """
            SELECT 
                PK_NO, 
                PI.IMAGE
            FROM 
                PRODINFO_MAIN PM, 
                PRODUCT P, 
                PROD_IMAGE PI
            WHERE
                PM.ORG_PROD_ID = PI.PROD_ID
                AND PM.ORG_PROD_ID=P.ORG_PROD_ID
                AND P.PROD_ID = '%s'
            ORDER BY 
                FIELD_INDEX ASC
        """

        self.execute_query(sql % prod_id)

    def get_modified_items_by_hour(self, delta_hours):
        sql = """
            SELECT
                p.title_main,
                p.prod_id,
                sp.item_id,
                p.list_price,
                p.special_price,
                p.sale_price,
                p.sale_disc,
                sp.status,
                (case when p.prod_rank = 'A' then '全新'
                    when p.prod_rank = 'B' then '近全新'
                    when p.prod_rank = 'C' then '良好'
                    when p.prod_rank = 'D' then '普通'
                    when p.prod_rank = 'C' then '差強人意'
                    else '' end) prod_rank

            FROM
                PRODINFO_MAIN PM,
                PRODUCT P,
                app_shopee_product sp

            WHERE
                PM.ORG_PROD_ID=P.ORG_PROD_ID AND
                P.STATUS_FLG='Y'AND
                sp.prod_id = p.prod_id AND
                p.MDF_TIME >= (sysdate-%s/24)
        """

        return self.execute_and_retrieve_data(sql % delta_hours)

    def insert_shopee_item(self, prod_id, item_id):
        sql = """
            INSERT INTO APP_SHOPEE_PRODUCT
                (PROD_ID, ITEM_ID, STATUS, CRT_USER, CRT_TIME)
            VALUES
                ('%s', %d, 'A', 'SYS', SYSDATE)
        """

        self.execute_non_query(sql % (prod_id, int(item_id)))

    def insert_shopee_item_warning(self, prod_id, item_id, warning):
        sql = """
            INSERT INTO APP_SHOPEE_ERROR
                (PROD_ID, ITEM_ID, STATUS, WARNING, CRT_USER, CRT_TIME)
            VALUES
                ('%s', %d, 'W', '%s', 'SYS', SYSDATE)
        """

        self.execute_non_query(sql % (prod_id, int(item_id), warning))

    def insert_shopee_item_error(self, prod_id, error):
        sql = """
            INSERT INTO APP_SHOPEE_ERROR
                (PROD_ID, STATUS, ERROR, CRT_USER, CRT_TIME)
            VALUES
                ('%s', 'E', '%s', 'SYS', SYSDATE)
        """

        self.execute_non_query(sql % (prod_id, error))

    def execute_and_retrieve_data(self, sql):
        result = None
        try:
            result = self.execute_query(sql)
            self.con.commit()

            return result

        except cx_Oracle.DatabaseError as e:
            self.con.rollback()
            raise e

    def is_record_exists(self, sql):
        result = None
        try:
            result = self.execute_query(sql)
            self.con.commit()

            return len(result) > 0

        except cx_Oracle.DatabaseError as e:
            self.con.rollback()
            raise e

    def get_prod_tag(self, prod_id):
        sql = """
                 select kw_cte,count(kw_cte) counts, org_prod_id 
                    from (select kw_cte,org_prod_id from  prod_kw 
                    where org_prod_id = '%s' and status_flg='Y' and kw_cte is not null order by crt_time desc)
                    group by kw_cte, org_prod_id
                order by counts desc
        """

        self.execute_query(query=sql % prod_id, as_dict=True)

    def update_latest_tag(self):
        sql = """
            update app_biggo_product set status_flg = 'N', mdf_time = sysdate  where  prod_id in(
                select distinct org_prod_id from  prod_kw p group by org_prod_id, status_flg, kw_cte, cust_id, CRT_TIME, MDF_TIME
                                having  status_flg='Y' and kw_cte is not null
                                and cust_id = 'XSX' and 
                    (P.CRT_TIME >= trunc(SYSDATE-1) AND P.CRT_TIME < trunc(SYSDATE))
                    OR (P.MDF_TIME >= trunc(SYSDATE-1) AND P.MDF_TIME < trunc(SYSDATE))
                )
        """
        try:
            self.execute_non_query(sql)
            self.con.commit()

        except Exception as e:
            self.con.rollback()
            raise e

    def get_extend_cat_name(self, prod_id):
        sql = """
                select p.prod_cat_id, p.cat_id, (select cat_nm from cat4xsx where cat_id = p.cat_id and prod_cat_id = p.prod_cat_id) catname,
                case when substr(p.cat_id,3,2) = '00' then '' else (select cat_nm from cat4xsx where substr(cat_id,0,2) = substr(p.cat_id,0,2) and prod_cat_id = p.prod_cat_id and cat_level = 1) end as catname1 
                from prod_cat p where org_prod_id = '%s' and status_flg = 'Y' and main_cat_flg = 'N' and cat_type = 'S' order by cat_id asc
        """

        self.execute_query(query=sql % prod_id, as_dict=True)

    def get_tag_change_ids(self, as_dict=True):
        sql = """
                    select distinct org_prod_id from  prod_kw group by org_prod_id, status_flg, kw_cte, cust_id
                    having  status_flg='Y' and kw_cte is not null
                    and cust_id = 'XSX'
                    """
        self.execute_query(query=sql, as_dict=True)

    def get_biggo_prod_main_tags(self, prod_ids, as_dict=True):
        sql = """
                select 
                p.prod_id prodid, p.org_prod_id orgprodid, p.title_main titlemain, p.title_next titlenext, p.prod_cat_id prodcatid, 
                case when  LENGTH(pm.cat_id) < 12 then '000000000000' WHEN (select cat_nm from cat4xsx where substr(cat_id,0,2) = substr(pm.cat_id,0,2) and prod_cat_id = pm.prod_cat_id and cat_level='1') is null THEN '000000000000' WHEN (select cat_nm from cat4xsx where substr(cat_id,0,4) = substr(pm.cat_id,0,4) and prod_cat_id = pm.prod_cat_id and cat_level='2') is null THEN RPAD(substr(pm.cat_id,0,2), 12,'0') ELSE RPAD(substr(pm.cat_id,0,4), 12,'0') end as catid,
                case when (select cat_nm from cat4xsx where substr(cat_id,0,4) = substr(pm.cat_id,0,4) and prod_cat_id = pm.prod_cat_id and cat_level='2') is null then '' else (select cat_nm from cat4xsx where substr(cat_id,0,4) = substr(pm.cat_id,0,4) and prod_cat_id = pm.prod_cat_id and cat_level='2') end as catname,
                p.list_price listprice, p.special_price specialprice, p.sale_price saleprice, p.sale_disc saledisc,
                pub.pub_nm_main pubnmmain, pm.publish_date publishdate, p.eancode eancode, pm.isbn isbn,
                p.org_flg orgflg, p.prod_rank, p.add_mark_flg,
                substr(pm.age_begin,0,2) age_begin, substr(pm.age_end,0,2) age_end, pb.language language, pb.binding_type bindingtype,
                pm.author_main author, pb.translator translator, pb.painter painter, pp.author_pf authorpf , pp.translator_pf translatorpf,
                pp.media_rcm mediarcm, pp.award_rec awardrec, pp.person_rcm personrcm, pp.sp_rec sprec, pp.person_guide personguide, 
                pp.prod_pf prodpf, pp.viewdata viewdata, pp.preface preface, pp.catalogue catalogue,
                pd.prod_color prodcolor,ec.sale_qty,ec.sale_qty_30,ec.sale_qty_7,
                case when (p.prod_cat_id = '81' and p.org_flg = 'C') then NVL((select distinct 1 from prod_image img where img.prod_id = p.sup_org_prod_id and status_flg = 'Y'),0)
                when  (p.prod_cat_id not in '81' and p.org_flg = 'C') then NVL((select distinct 1 from prod_image img where img.prod_id = p.org_prod_id and status_flg = 'Y'),0)
                else  NVL((select distinct 1 from prod_image img where img.prod_id = p.prod_id  and status_flg = 'Y'),0) end as image_cover,
                case when  (p.prod_cat_id in ('14','25','17','26')) then NVL((select 1 from product where prod_id = p.prod_id and forsale_flg = 'Y' and status_flg = 'Y'),0)
                else  NVL((select 1 from vstk a where a.prod_id = p.prod_id),0) end as stock,
                case when (p.prod_cat_id = '61' or p.prod_cat_id = '62') then (select prod_spec from prodinfo_dpm where org_prod_id = p.org_prod_id)
                when (p.prod_cat_id = '31' or p.prod_cat_id = '32') then (select prod_spec from prodinfo_av where org_prod_id = p.org_prod_id)
                else null end as prodspec,
                case when LENGTH(pm.cat_id) < 12 then '其他' when (select cat_nm from cat4xsx where substr(cat_id,0,2) = substr(pm.cat_id,0,2) and prod_cat_id = pm.prod_cat_id and cat_level='1') is null then '其他' else (select cat_nm from cat4xsx where substr(cat_id,0,2) = substr(pm.cat_id,0,2) and prod_cat_id = pm.prod_cat_id and cat_level = 1) end as catname1,
                pb.ADO_FLG
                from product p, prodinfo_main pm, publisher pub, prodinfo_book pb, prod_profile pp, prodinfo_dpm pd,ec_dtl ec
                where p.org_prod_id = pm.org_prod_id
                and pm.pub_id = pub.pub_id(+)
                and pm.org_prod_id = pb.org_prod_id(+)
                and pm.org_prod_id = pp.org_prod_id(+)
                and pm.org_prod_id = pd.org_prod_id(+)
                and pm.org_prod_id = ec.prod_id(+)
                and p.status_flg = 'Y'
                and p.prod_id in (%s)
                order by p.prod_id asc
        """

        self.execute_query(query=sql % prod_ids, as_dict=True)