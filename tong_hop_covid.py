from crawler import Crawl
from extract import Extract

# Crawl dữ liệu trên trang của Bộ Y Tế
results = Crawl(executable_path='./chromedriver.exe').get_data_crawler()

# Bóc tách thông tin
df_covid = Extract(results[0]).extract_info()
print(df_covid)

# Xuất ra file excel
df_covid.to_excel('tong_hop_covid.xlsx')
