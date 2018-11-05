import datetime

# dt = datetime(2017, 9, 1)
# dt.month = datetime.now().month
# dt.year = datetime.now().year
#
# dt_now = datetime.now()
#
#
# print(dt, type(dt))
#
# print(dt_now, type(dt_now))
#
#
# str1, str2 = str(dt_now.year), str(dt_now.month)
#
# print(str1, str2)
#
# res1 = dt_now.isoformat()
# dt1 = datetime.date(2016, 1, 1)
# datetime
# print(dt1)
#
# # dt1 = dt + datetime.timedelta(month=1)
# dt = datetime.datetime(2017, 9, 1)
# print(dt.strftime("%Y%m"))
# print(dt.isoformat().replace("-", "")[0:6])
# print(dt1.isoformat().replace("-", "")[0:6])


y = datetime.date(2016, 12, 1)
z = datetime.date(2018, 9, 30)

print(y, z)



from datetime import datetime as dt

print(dt.now().year, type(dt.now().year))

dt = dt(2016, 8, 1)

print(dt)

print(str(dt), type(str(dt)))