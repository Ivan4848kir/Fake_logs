import datetime
import random
import datetime as dt
import pandas as pd

def add_secs_to_time(timeval, secs_to_add):
    secs = timeval.hour * 3600 + timeval.minute * 60 + timeval.second
    secs += secs_to_add
    add_time=datetime.time(secs // 3600, (secs % 3600) // 60, secs % 60)
    return add_time

def generate_dates_range(start_date, end_date) -> list: #функция генерит список дней по которым будут логи
    date_1=min(start_date, end_date)
    date_2=max(start_date, end_date)

    dates_list=[date_1]

    while date_1<date_2:
        date_1+=dt.timedelta(days=1)
        dates_list.append(date_1)
    return dates_list

def get_potreb_credit(date, time):
    credit_sources_list=["potrebCreditSite", "poterbCreditDopOffice", "potrebCreditMobileapp"]
    credit_source=random.choice(credit_sources_list)
    appNum=random.randint(1111111111, 9999999999)
    creditSum=random.choice([100000, 200000, 300000, 400000, 500000])
    creditStatus=random.choice(["approve", "decline"])
    logs_dict[str(time)]="INFO get credit request [cerditType: potreb, request source: %s]" % credit_source
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 1))]="INFO get credit offers request[cerditType: potreb, request source: %s ]" % credit_source
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 2))]="INFO createApp[cerditType: potreb, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d]" % (credit_source, creditSum, appNum)
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 3))]="INFO request to the credit history bureau[appNum: %d]" % appNum
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 4))]="INFO underwriter check[cerditType: potreb, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d]" % (credit_source, creditSum, appNum)
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 5))]="INFO get request to RTDM system[cerditType: potreb, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d]" % (credit_source, creditSum, appNum)
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 6))]="INFO RTDM system response[cerditType: potreb, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d, creditStatus: %s]" % (credit_source, creditSum, appNum, creditStatus)
    if creditStatus == "approve":
        logs_dict[str(date)+" "+str(add_secs_to_time(time, 7))]="INFO signing an agreement[appNum: %d]" % appNum
        logs_dict[str(date)+" "+str(add_secs_to_time(time, 8))]="INFO loan issued[appNum: %d]" % appNum
    else:
        logs_dict[str(date)+" "+str(add_secs_to_time(time, 7))]="INFO loan application has been rejected[appNum: %d]" % appNum

def get_auto_credit(date, time):
    credit_sources_list=["autoCreditSite", "autoCreditDopOffice", "autoCreditMobileapp"]
    credit_source=random.choice(credit_sources_list)
    appNum=random.randint(1111111111, 9999999999)
    creditSum=random.choice([500000, 1000000, 1500000, 2000000])
    creditStatus=random.choice(["approve", "decline"])
    logs_dict[str(time)]="INFO get credit request [cerditType: auto, request source: %s]" % credit_source
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 1))]="INFO get credit offers request[cerditType: auto, request source: %s ]" % credit_source
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 2))]="INFO createApp[cerditType: auto, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d]" % (credit_source, creditSum, appNum)
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 3))]="INFO request to the credit history bureau[appNum: %d]" % appNum
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 4))]="INFO underwriter check[cerditType: auto, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d]" % (credit_source, creditSum, appNum)
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 5))]="INFO get request to RTDM system[cerditType: auto, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d]" % (credit_source, creditSum, appNum)
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 6))]="INFO RTDM system response[cerditType: auto, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d, creditStatus: %s]" % (credit_source, creditSum, appNum, creditStatus)
    if creditStatus == "approve":
        logs_dict[str(date)+" "+str(add_secs_to_time(time, 7))]="INFO signing an agreement[appNum: %d]" % appNum
        logs_dict[str(date)+" "+str(add_secs_to_time(time, 8))]="INFO loan issued[appNum: %d]" % appNum
    else:
        logs_dict[str(date)+" "+str(add_secs_to_time(time, 7))]="INFO loan application has been rejected[appNum: %d]" % appNum

def get_mortgage_credit(date, time):
    credit_sources_list=["mortgageCreditSite", "mortgageCreditDopOffice"]
    credit_source=random.choice(credit_sources_list)
    appNum=random.randint(1111111111, 9999999999)
    creditSum=random.choice([5000000, 6000000, 7000000, 8000000])
    creditStatus=random.choice(["approve", "decline"])
    logs_dict[str(time)]="INFO get credit request [cerditType: mortgage, request source: %s]" % credit_source
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 1))]="INFO get credit offers request[cerditType: potreb, request source: %s ]" % credit_source
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 2))]="INFO createApp[cerditType: mortgage, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d]" % (credit_source, creditSum, appNum)
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 3))]="INFO request to the credit history bureau[appNum: %d]" % appNum
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 4))]="INFO underwriter check[cerditType: mortgage, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d]" % (credit_source, creditSum, appNum)
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 5))]="INFO get request to RTDM system[cerditType: mortgage, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d]" % (credit_source, creditSum, appNum)
    logs_dict[str(date)+" "+str(add_secs_to_time(time, 6))]="INFO RTDM system response[cerditType: mortgage, request source: %s,  creditSum: %d, rate: 11.5, appNum: %d, creditStatus: %s]" % (credit_source, creditSum, appNum, creditStatus)
    if creditStatus == "approve":
        logs_dict[str(date)+" "+str(add_secs_to_time(time, 7))]="INFO signing an agreement[appNum: %d]" % appNum
        logs_dict[str(date)+" "+str(add_secs_to_time(time, 8))]="INFO loan issued[appNum: %d]" % appNum
    else:
        logs_dict[str(date)+" "+str(add_secs_to_time(time, 7))]="INFO loan application has been rejected[appNum: %d]" % appNum

def garbage_logs(date, time):
    log_1 = "ERROR The session is not authenticated. (System.Web.Services.Protocols.SoapException)"
    log_2 =  "INFO [AP] (6ff9) output: --asyncNtf:Pipeline timeout: it seems that pipeline hanged"
    log_3 = "INFO [AP] (bf19) command: 'Invoke: DataTransfer.SyncDisk…"
    log_4 = "INFO Task session [3af0e723-b2a3-4054-b4e3-eea364041402] has been completed, status: Success, 107,374,182,400 of 107,374,182,400 bytes, 55,326,015,488 of 55,326,015,488 used bytes, 14 of 14 objects, details:"
    log_5 = "INFO Job session '0f8ad58b-4183-4500-9e49-cc94f0674d87' has been completed, status: 'Success', '100 GB' of '100 GB' bytes, '1' of '1' tasks, '1' successful, '0' failed, details: '', PointId: [d3e21f72-9a52-4dc9-bcbe-98d38498a3e8]"
    log_6 = "INFO Preparing point in full mode "
    log_7 = "INFO Preparing point in incremental mode "
    log_8 = "INFO [ProxyDetector] Proxy [dsg.test.local] lies in different subnet with host [VMware ESXi 6.5.0 build-16207673]"
    log_9 = "INFO VM task VM name: 'vudc01', VM host name: 'https://esxi.test.local', VM host info: 'VMware ESXi 6.5.0 build-16207673', VM host apiVersion: '6.5', source host name: 'vcenter.test.local', source host id: '3de6c11c-ad7e-4ec0-ba12-d99a0b30b493', source host type: 'VC', size: '107374182400', display name: 'vudc01'"
    log_10 = "INFO [Soap] Removing snapshot 'snapshot-536'"
    log_11 = "INFO [Soap] Loaded 2 elements"
    log_12 = "INFO [ViSnapshot] Consolidation is not needed"
    log_13 = "INFO [ViSnapshot] Checking if disks consolidation is needed for vm 'vm-26'"
    garbage_logs_list = [log_1, log_2, log_3, log_4, log_5, log_6, log_6, log_7, log_8, log_9, log_10, log_11, log_12, log_13]
    logs_dict[str(time)] = random.choice(garbage_logs_list)

if __name__ == '__main__':
    start_date=dt.date(2023, 1, 1)
    end_date=dt.date(2023, 4, 1)
    start_date_random_range=dt.date(2023, 2, 1)
    end_date_random_range=dt.date(2023, 2, 21)
    logs_dict={}

    full_dates_list=generate_dates_range(start_date, end_date)

    logfile = open("LOGS.txt", 'w+')
    for i in full_dates_list:
        for j in range(0, 600):
            start_time=str(i)+" %02d:%02d:%02d" % (random.normalvariate(14, 2), random.randint(0, 59,), random.randint(0, 52)) #часы берутся по нормальному распределению, мю-14, сигма-2
            time=dt.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            get_potreb_credit(i, time)

    for i in full_dates_list:
        for j in range(0, 300):
            start_time=str(i)+" %02d:%02d:%02d" % (random.normalvariate(15, 2), random.randint(0, 59,), random.randint(0, 52)) #часы берутся по нормальному распределению, мю-15, сигма-2
            time=dt.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            get_auto_credit(i, time)

    for i in full_dates_list:
        for j in range(0, 100):
            start_time = str(i) + " %02d:%02d:%02d" % (random.normalvariate(12, 2), random.randint(0, 59),random.randint(0,52))  # часы берутся по нормальному распределению, мю-12, сигма-2
            time = dt.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            get_mortgage_credit(i, time)

    for i in full_dates_list:
        for j in range(0, 100):
            start_time = str(i) + " %02d:%02d:%02d" % (random.randint(0, 23), random.randint(0, 59),random.randint(0, 59))
            time = dt.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            garbage_logs(i, time)

    logs_dict_keys_list=list(logs_dict.keys())
    logs_dict_keys_list=sorted(logs_dict_keys_list)
    for i in logs_dict_keys_list:
        logfile.write(str(i)+" "+str(logs_dict[i]+"\n"))
logfile.close()






