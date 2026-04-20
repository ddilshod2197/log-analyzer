import re
import os

def log_analiz(log_file):
    try:
        with open(log_file, 'r') as f:
            log_data = f.read()
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return

    # Logga kirgan ma'lumotlarni ajratib olamiz
    log_lines = log_data.split('\n')

    # Logga kirgan ma'lumotlarni sanab bo'lamiz
    log_count = len(log_lines)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxat yaratamiz
    log_data_list = []

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatga qo'shamiz
    for line in log_lines:
        log_data_list.append(line)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni sanab bo'lamiz
    log_data_count = len(log_data_list)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatga qo'shamiz
    log_data_list = [line for line in log_data_list if line]

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni sanab bo'lamiz
    log_data_count = len(log_data_list)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatga qo'shamiz
    log_data_list = [line for line in log_data_list if re.search(r'\d{4}-\d{2}-\d{2}', line)]

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni sanab bo'lamiz
    log_data_count = len(log_data_list)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatga qo'shamiz
    log_data_list = [line for line in log_data_list if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)]

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni sanab bo'lamiz
    log_data_count = len(log_data_list)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatga qo'shamiz
    log_data_list = [line for line in log_data_list if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+', line)]

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni sanab bo'lamiz
    log_data_count = len(log_data_list)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatga qo'shamiz
    log_data_list = [line for line in log_data_list if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+ \d+', line)]

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni sanab bo'lamiz
    log_data_count = len(log_data_list)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatga qo'shamiz
    log_data_list = [line for line in log_data_list if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+ \d+ \w+', line)]

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni sanab bo'lamiz
    log_data_count = len(log_data_list)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatga qo'shamiz
    log_data_list = [line for line in log_data_list if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+ \d+ \w+ \d+', line)]

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni sanab bo'lamiz
    log_data_count = len(log_data_list)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatga qo'shamiz
    log_data_list = [line for line in log_data_list if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+ \d+ \w+ \d+ \w+', line)]

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni sanab bo'lamiz
    log_data_count = len(log_data_list)

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatga qo'shamiz
    log_data_list = [line for line in log_data_list if re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+ \d+ \w+ \d+ \w+ \d+', line)]

    # Logga kirgan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni qayta ishlash uchun yangi ro'yxatdan ma'lumotlarni sanab bo'lamiz
    log_data_count = len
