# HW_1

## 步驟
1. 引入 csv
1. 將檔案篩選
    * 我先是創造了一個兩層的list。第一個層級是 station ID ，也就是每個元素都是一個名稱是 station ID的 list。第二層是裡頭 station ID 名稱的list ，裏頭存放該station ID 的所有資料。這個部分是使用到 filter 函式。
1. 去除異常值，同時求出最大值
    * 再將每個 station 的資料做分類的同時，我也將每項資料當中需要處理的部分截取出來(我的是擷取station ID 和 TEMP，格式是['station_id', 'TEMP'])。這部分用[ ]達成，因為每一項資料(第二層資料裡的 element)還是 Dict 格式，所以可以輕易用 key-value 對去擷取資料。
    * 去除異常值得的時候，我用 for 迴圈將過濾每個 station ID 名稱的 list，將異常值刪除。接下來判斷每個 station ID 名稱的 list ，若是有 list 是空的，就會將['station ID', 'None']加入該 list，否則取其最大值，加入目標 list 中。
1. 列印目標資料。
1. 輸出成果
    * 每個 station 加上 其 TEMP 的最大值，若是沒有最大值的話，會顯示 'None'。
    * ex. [['C0A880', 27.0], ['C0F9A0', 22.0], ['C0G640', 28.0], ['C0R190', 'None'], ['C0X260', 27.0]]
