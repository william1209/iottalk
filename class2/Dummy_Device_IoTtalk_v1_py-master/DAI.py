import time, DAN, requests, random

ServerURL = 'http://140.113.199.186:7788' #with no secure connection
#ServerURL = 'https://DomainName' #with SSL connection
Reg_addr = 'abcd' #if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy Device'
DAN.profile['df_list']=['temp','humi']   #DAN.profile['df_list']=['Acceleration', 'Dummy_Control']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerURL, Reg_addr)

while True:

    def get_element(soup, tag, class_name):
    data = []
    table = soup.find(tag, attrs={'class':class_name})
    rows = table.find_all('tr')
    del rows[0]
    
    for row in rows:
        first_col = row.find_all('th')
        cols = row.find_all('td')
        cols.insert(0, first_col[0])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) 
    return data

    region ='Hsinchu'
   
    file_name = region+".html"

    f = open (file_name,'r', encoding='utf-8')
    s = f.readlines()
    s = ''.join(s)

    soup = BeautifulSoup(s, "lxml")

    df_tmp = get_element(soup, 'table','BoxTable')
    temp=df_tmp[0][1]
    humi=df_tmp[0][8]




    try:
    #Pull data from a device feature called "Dummy_Control"
        

    #Push data to a device feature called "Dummy_Sensor"
        #value2=random.uniform(1, 10)
        DAN.push ('temp', temp)   #DAN.push ('Acceleration', value2, value2)
        DAN.push ('humi',humi)

    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(0.2)

