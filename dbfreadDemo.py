import dbfread
import pandas as pd

dbf_path = r'/Users/shy/Downloads/REP.dbf'          # 文件所在位置
xls_filename = r"{}.xlsx".format(dbf_path.split(r'\\')[-1].split('.')[0])  # 输出路径

# 读取DBF文件并转换为DataFrame
with dbfread.DBF(dbf_path, encoding='gbk') as table:
    records = [record for record in table]
    df = pd.DataFrame(records)
