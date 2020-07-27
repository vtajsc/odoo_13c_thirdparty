================================
The modules update to version 13
================================

Module name
-----------
* as_vn_address
    - Author: Mai Tien Dung
    - website: https://aliensoftware.dev
    - Description:
        1. Delete view_type in xml file

* document_sidebar
    - Author: renjie <i@renjie.me>
    - website: https://renjie.me
    - Description:
        1. Inherit create function:
            - change stage_id SO after attachment
            - Create attachment file for Picking from SO
* auto_backup
    - Author: Yenthe Van Ginneken
    - website: http://www.odoo.yenthevg.com
    - Description:
        1. db_backup.py line 124: change "os.makedirs(rec.folder)" to "raise Warning"
        2. Add nextcall to cron

* web_float_menu
    - Author: VTA IT Team
    - website: https://www.viettinhanh.com.vn
    - Description:
        1. Go to *Settings > Menu Items > Menu* then toggle *Is Float* field to enable menu hidden

Contributors
------------

* Do Minh Thanh <thanh.dominh@viettinhanh.com.vn>
* website: https://viettinhanh.com.vn
