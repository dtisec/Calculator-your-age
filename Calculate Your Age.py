import time
from calendar import isleap

# Yılı tanımla
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# Her ayda ki gün sayısını tanımla.
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


isim = input("Adınızı girin: ")
yas = input("Yaşınızı girin: ")
yerel_zaman = time.localtime(time.time())

yıl = int(yas)
ay = yıl * 12 + yerel_zaman.tm_mon
gün = 0

begin_year = int(yerel_zaman.tm_year) - yıl
end_year = begin_year + yıl

# Günleri hesapla
for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        gün = gün + 366
    else:
        gün = gün + 365

leap_year = judge_leap_year(yerel_zaman.tm_year)
for m in range(1, yerel_zaman.tm_mon):
    gün = gün + month_days(m, leap_year)

gün = gün + yerel_zaman.tm_mday
print("%s's yaşı %d yıl yada " % (isim, yıl), end="")
print("%d ay yada %d gün" % (ay, ay))
