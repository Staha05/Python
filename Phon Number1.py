print("بررسی شماره تلفن")

country_codes = {
    "98": "ایران",
    "1": "ایالات متحده آمریکا",
    "44": "انگلستان",
    "49": "آلمان",
    "33": "فرانسه",
    "7": "روسیه",
    "86": "چین",
    "91": "هند",
    "61": "استرالیا",
    "81": "ژاپن",
    "55": "برزیل",
    "39": "ایتالیا",
    "52": "مکزیک",
    "20": "مصر"
}

codcountry = input("کد کشور را وارد کنید:+")


if codcountry in country_codes:
    print(f"کشور انتخاب شده: {country_codes[codcountry]}")

    Phone = input("شماره تلفن خود را وارد کنید: ")

    if codcountry == "98":  
        if len(Phone) == 11:
            number = Phone[0:4]
            if number in ("0910", "0911", "0912", "0913", "0914", "0915", "0916", "0917", "0918", "0919",
                          "0990", "0991", "0992", "0993", "0994"):
                print("اپراتور: همراه اول (MCI)")
            elif number in ("0930", "0933", "0935", "0936", "0937", "0938", "0939"):
                print("اپراتور: ایرانسل (MTN)")
            elif number in ("0920", "0921", "0922", "0923"):
                print("اپراتور: رایتل")
            elif number in ("0935", "0933"):
                print("اپراتور: تالیا (شاتل موبایل)")
            else:
                print("اپراتور نامشخص")
        else:
            print("خطا: شماره تلفن ایران باید 11 رقم باشد.")
    
    elif codcountry == "1": 
        if len(Phone) == 10:
            number = Phone[0:3]
            if number in ("201", "202", "203"):
                print("اپراتور: Verizon")
            elif number in ("210", "212", "213"):
                print("اپراتور: AT&T")
            elif number in ("310", "312", "313"):
                print("اپراتور: T-Mobile")
            elif number in ("404", "415", "646"):
                print("اپراتور: Sprint")
            elif number in ("218", "320", "507"):
                print("اپراتور: US Cellular")
            else:
                print("اپراتور نامشخص")
        else:
            print("خطا: شماره تلفن آمریکا باید 10 رقم باشد.")
    
    elif codcountry == "44": 
        if len(Phone) == 10:
            number = Phone[0:4]
            if number in ("7700", "7711", "7722"):
                print("اپراتور: EE")
            elif number in ("7400", "7411", "7422"):
                print("اپراتور: Vodafone")
            elif number in ("7500", "7511", "7522"):
                print("اپراتور: O2")
            elif number in ("7300", "7311", "7322"):
                print("اپراتور: Three")
            elif number in ("7000", "7011", "7022"):
                print("اپراتور: BT Mobile")
            else:
                print("اپراتور نامشخص")
        else:
            print("خطا: شماره تلفن انگلستان باید 10 رقم باشد.")
 
    elif codcountry == "49": 
        if len(Phone) in (10, 11):
            number = Phone[0:3]
            if number in ("151", "160", "170"):
                print("اپراتور: Telekom")
            elif number in ("152", "162", "172"):
                print("اپراتور: Vodafone")
            elif number in ("157", "163", "163"):
                print("اپراتور: O2")
            elif number in ("155", "159", "176"):
                print("اپراتور: Drillisch")
            else:
                print("اپراتور نامشخص")
        else:
            print("خطا: شماره تلفن آلمان باید 10 رقم باشد.")
            
    elif codcountry == "91": 
        if len(Phone) == 10:
            number = Phone[0:3]
            if number in ("981", "982", "983"):
                print("اپراتور: Airtel")
            elif number in ("990", "991", "992"):
                print("اپراتور: Jio")
            elif number in ("984", "985", "986"):
                print("اپراتور: Vodafone Idea")
            elif number in ("940", "941", "942"):
                print("اپراتور: BSNL")
            elif number in ("993", "994", "995"):
                print("اپراتور: MTNL")
            else:
                print("اپراتور نامشخص")
        else:
            print("خطا: شماره تلفن هند باید 10 رقم باشد.")
            
    elif codcountry == "61": 
        if len(Phone) == 10:
            number = Phone[0:3]
            if number in ("040", "041", "042"):
                print("اپراتور: Telstra")
            elif number in ("043", "044", "045"):
                print("اپراتور: Optus")
            elif number in ("046", "047"):
                print("اپراتور: Vodafone")
            elif number in ("048", "049"):
                print("اپراتور: TPG Telecom")
            else:
                print("اپراتور نامشخص")
        else:
            print("خطا: شماره تلفن استرالیا باید 10 رقم باشد.")
            
    elif codcountry == "7": 
        if len(Phone) == 10:
            number = Phone[0:3]
            if number in ("910", "911", "912"):
                print("اپراتور: MTS")
            elif number in ("920", "921", "922"):
                print("اپراتور: MegaFon")
            elif number in ("900", "901", "902"):
                print("اپراتور: Beeline")
            elif number in ("950", "951", "952"):
                print("اپراتور: Tele2")
            else:
                print("اپراتور نامشخص")
        else:
            print("خطا: شماره تلفن روسیه باید 10 رقم باشد.")
        
    elif codcountry == "86": 
        if len(Phone) == 11:
            number = Phone[0:3]
            if number in ("134", "135", "36"):
                print("اپراتور: China Mobile")
            elif number in ("130", "132", "133"):
                print("اپراتور: China Unicom")
            elif number in ("133", "153", "180"):
                print("اپراتور: China Telecom")
            elif number in ("189", "191", "193"):
                print("اپراتور: China Tietong")
            else:
                print("اپراتور نامشخص")
        else:
            print("خطا: شماره تلفن چین باید 11 رقم باشد.")
    
    else:
        print("در حال حاضر اپراتورهای این کشور پشتیبانی نمی‌شوند.")

else:
    print("کد کشور وارد شده پذیرفته نشده است.")

if Phone in ("09926671386"):
    print("اطلاعات:")
    print("نام: سیدطاها")
    print("نام خانوادگی: اسدیان")
    print("کدملی: 9926671386")
    print("آدرس: رودهن")

else:
    print("اطلاعاتی یافت نشد!")