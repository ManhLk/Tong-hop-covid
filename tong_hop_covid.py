from crawler import Crawl
from extract import Extract

def check_number_patient(df):
    patient_code = df['Bệnh nhân'].apply(lambda x: int(x.replace('BN','')))
    patient_code = patient_code.values
    error = []
    for i in range(len(patient_code)-1):
        next_patient_code = patient_code[i] + 1
        if next_patient_code < patient_code[i+1]:
            e = 'Thiếu BN{} - BN{}'.format(next_patient_code, patient_code[i+1]-1)
            error.append(e)
        elif patient_code[i] == patient_code[i+1]:
            e = 'Thừa BN{}'.format(patient_code[i])
            error.append(e)
    print("Số lượng bệnh nhân đã tổng hợp:", len(patient_code))
    if len(error) == 0:
        print("Tổng hợp ĐỦ! happy for you")
    else:
        print("Tổng hợp LỖI:")
        for e in error:
            print(e)

if __name__ == "__main__":
    # Crawl dữ liệu trên trang của Bộ Y Tế
    results = Crawl(executable_path='./chromedriver.exe').get_data_crawler()

    # Tổng hợp thông tin
    df_covid = Extract(results[0]).extract_info()
    print(df_covid)

    # Kiểm tra lại thông tin 
    check_number_patient(df_covid)

    # Xuất ra file excel
    df_covid.to_excel('tong_hop_covid.xlsx')
