目前有數個檔案

1. template.html 是生成網頁的模板
2. template.css 是生成網頁的CSS樣式表
3. reportGenerator.py 是預計要放入資料的python原始碼(但現在卡在不知怎麼用python生成網頁...)
4. test.jpg 以及 testVertical.jpg 只是測試用的照片

目前資料如reportGenerator.py裡面的list與會用for迴圈取出載有每頁資訊的dictionary，
再用key去取value(標題與圖片位址)，但是不知道要怎麼樣把這些變數丟入html生成html

沒有要生成很複雜的網站，單純想生一些離線使用的報表

問題點:
1. 是否要裝生成html標籤的python資料庫? 有推薦哪一個?
2. 還是要土法煉鋼寫一些函式生成html標籤?
