import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 12)

# https://bnpb-inacovid19.hub.arcgis.com/datasets/statistik-perkembangan-covid19-indonesia-new/data?orderBy=Tanggal&orderByAsc=false
data = pd.read_csv('E:/Besha/belajar/pandas exercise/exercise 12/Statistik_Perkembangan_COVID19_Indonesia_New.csv')

data.sort_values(by='Hari_ke', ascending=True, inplace=True)
data = data.iloc[:, :13].reset_index()
data = data[data['Jumlah_Kasus_Kumulatif'].notna()]

data['Tanggal'] = pd.to_datetime(data['Tanggal'])

maret = data.loc[data['Tanggal'].dt.month == 3]
april = data.loc[data['Tanggal'].dt.month == 4]
mei = data.loc[data['Tanggal'].dt.month == 5]
juni = data.loc[data['Tanggal'].dt.month == 6]
juli = data.loc[data['Tanggal'].dt.month == 7]
agustus = data.loc[data['Tanggal'].dt.month == 8]
september = data.loc[data['Tanggal'].dt.month == 9]
oktober = data.loc[data['Tanggal'].dt.month == 10]


def growthcalc(mon1, mon2):
    return (mon1['Jumlah_Kasus_Kumulatif'].iloc[-1]) - (mon2['Jumlah_Kasus_Kumulatif'].iloc[-1])


def recgrowthcalc(mon1, mon2):
    return (mon1['Jumlah_Pasien_Sembuh'].iloc[-1]) - (mon2['Jumlah_Pasien_Sembuh'].iloc[-1])


def deagrowthcalc(mon1, mon2):
    return (mon1['Jumlah_Pasien_Meninggal'].iloc[-1]) - (mon2['Jumlah_Pasien_Meninggal'].iloc[-1])


margrowth = maret['Jumlah_Kasus_Kumulatif'].iloc[-1]
marrecgrowth = (maret['Jumlah_Pasien_Sembuh'].iloc[-1]) - (maret['Jumlah_Pasien_Sembuh'].iloc[0])
mardeagrowth = (maret['Jumlah_Pasien_Meninggal'].iloc[-1]) - (maret['Jumlah_Pasien_Meninggal'].iloc[0])

aprgrowth = growthcalc(april, maret)
aprrecgrowth = recgrowthcalc(april, maret)
aprdeagrowth = deagrowthcalc(april, maret)

meigrowth = growthcalc(mei, april)
meirecgrowth = recgrowthcalc(mei, april)
meideagrowth = deagrowthcalc(mei, april)

jungrowth = growthcalc(juni, mei)
junrecgrowth = recgrowthcalc(juni, mei)
jundeagrowth = deagrowthcalc(juni, mei)

julgrowth = growthcalc(juli, juni)
julrecgrowth = recgrowthcalc(juli, juni)
juldeagrowth = deagrowthcalc(juli, juni)

agugrowth = growthcalc(agustus, juli)
agurecgrowth = recgrowthcalc(agustus, juli)
agudeagrowth = deagrowthcalc(agustus, juli)

sepgrowth = growthcalc(september, agustus)
seprecgrowth = recgrowthcalc(september, agustus)
sepdeagrowth = deagrowthcalc(september, agustus)

oktgrowth = growthcalc(oktober, september)
oktrecgrowth = recgrowthcalc(oktober, september)
oktdeagrowth = deagrowthcalc(oktober, september)

print(data.tail())
print(data.head())
print(data.info())

dfmonths = ['Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober']
df1 = pd.DataFrame({'Bulan': dfmonths}).reset_index(drop=True)

dfkumulatif = data['Jumlah_Kasus_Kumulatif'].groupby(data['Tanggal'].dt.month).tail(1)[:8]
dfgrowth = [margrowth, aprgrowth, meigrowth, jungrowth, julgrowth, agugrowth, sepgrowth, oktgrowth]
df2 = pd.DataFrame({'Total Kasus': dfkumulatif, 'Kasus Baru': dfgrowth}).reset_index(drop=True)
df12 = pd.concat([df1, df2], axis=1)
# print(df12)


def recperccalc(month):
    return (month['Jumlah_Pasien_Sembuh'].iloc[-1] / month['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100


marrec = recperccalc(maret)
aprrec = recperccalc(april)
meirec = recperccalc(mei)
junrec = recperccalc(juni)
julrec = recperccalc(juli)
agurec = recperccalc(agustus)
seprec = recperccalc(september)
oktrec = recperccalc(oktober)

dfrec = data['Jumlah_Pasien_Sembuh'].groupby(data['Tanggal'].dt.month).tail(1)[:8]
dfrecgrowthperc = ['%.01f'%marrec+r'%', '%.01f'%aprrec+r'%', '%.01f'%meirec+r'%', '%.01f'%junrec+r'%', '%.01f'%julrec+r'%', '%.01f'%agurec+r'%', '%.01f'%seprec+r'%', '%.01f'%oktrec+r'%']
dfrecgrowth = [marrecgrowth, aprrecgrowth, meirecgrowth, junrecgrowth, julrecgrowth, agurecgrowth, seprecgrowth, oktrecgrowth]
df3 = pd.DataFrame({'Total Sembuh': dfrec, 'Persentase Sembuh(%)': dfrecgrowthperc}).reset_index(drop=True)
df13 = pd.concat([df1, df3], axis=1)
# print(df13)


def deaperccalc(month):
    return (month['Jumlah_Pasien_Meninggal'].iloc[-1] / month['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100


mardea = deaperccalc(maret)
aprdea = deaperccalc(april)
meidea = deaperccalc(mei)
jundea = deaperccalc(juni)
juldea = deaperccalc(juli)
agudea = deaperccalc(agustus)
sepdea = deaperccalc(september)
oktdea = deaperccalc(oktober)

dfdea = data['Jumlah_Pasien_Meninggal'].groupby(data['Tanggal'].dt.month).tail(1)[:8]
dfdeagrowthperc = ['%.01f'%mardea+r'%', '%.01f'%aprdea+r'%', '%.01f'%meidea+r'%', '%.01f'%jundea+r'%', '%.01f'%juldea+r'%', '%.01f'%agudea+r'%', '%.01f'%sepdea+r'%', '%.01f'%oktdea+r'%']
dfdeagrowth = [mardeagrowth, aprdeagrowth, meideagrowth, jundeagrowth, juldeagrowth, agudeagrowth, sepdeagrowth, oktdeagrowth]
df4 = pd.DataFrame({'Total Meninggal': dfdea, 'Persentase Meninggal(%)': dfdeagrowthperc}).reset_index(drop=True)
df14 = pd.concat([df1, df4], axis=1)
# print(df14)

df = pd.concat([df1, df2, df3, df4], axis=1)
df.set_index('Bulan', inplace=True)
gantiint = ['Total Kasus', 'Kasus Baru', 'Total Sembuh', 'Total Meninggal']
df[gantiint] = df[gantiint].astype('int64')
print(df)

dfgro = pd.DataFrame({'Case growth' : dfgrowth, 'Recovery growth' : dfrecgrowth, 'Death growth' : dfdeagrowth})
df1gro = pd.concat([df1, dfgro], axis=1)
print(df1gro)


ax = sns.lineplot(x='Bulan', y='Total Kasus', data=df)
ax = sns.lineplot(x='Bulan', y='Total Sembuh', data=df, color='green')
ax = sns.lineplot(x='Bulan', y='Total Meninggal', data=df, color='red')
ax.legend(['Total Kasus', 'Sembuh', 'Meninggal'])
plt.title('Kasus Covid-19 di Indonesia')
plt.text(0.7, 411000, int(oktober['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(0.7, 394500, int(oktober['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(0.7, 377000, int(oktober['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()


coleamonth = ['Total Kasus', 'Kasus Baru', 'Total Sembuh', 'Persentase Sembuh(%)', 'Total Meninggal', 'Persentase Meninggal(%)']
dfgrowthmar = df[coleamonth][:1]
print(dfgrowthmar)

maret1 = sns.lineplot(x=maret['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=maret)
maret1 = sns.lineplot(x=maret['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=maret, color='green')
maret1 = sns.lineplot(x=maret['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=maret, color='red')
maret1.set_xticks(maret['Tanggal'].dt.day)
maret1.legend(['Total Kasus', 'Sembuh', 'Meninggal'])
plt.title('Kasus Covid-19 Maret 2020')
maret1.set_xlabel('Tanggal')
maret1.set_ylabel('Total Kasus')
plt.text(5, 1530, int(maret['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(5, 1465, int(maret['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(5, 1400, int(maret['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()


dfgrowthapr = df[coleamonth][:2]
print(dfgrowthapr)

april1 = sns.lineplot(x=april['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=april)
april1 = sns.lineplot(x=april['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=april, color='green')
april1 = sns.lineplot(x=april['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=april, color='red')
april1.set_xticks(april['Tanggal'].dt.day)
april1.legend(['Total Kasus', 'Sembuh', 'Meninggal'])
plt.title('Kasus Covid-19 April 2020')
april1.set_xlabel('Tanggal')
april1.set_ylabel('Total Kasus')
plt.text(4, 10150, int(april['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 9700, int(april['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 9250, int(april['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()


dfgrowthmei = df[coleamonth][1:3]
print(dfgrowthmei)

mei1 = sns.lineplot(x=mei['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=mei)
mei1 = sns.lineplot(x=mei['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=mei, color='green')
mei1 = sns.lineplot(x=mei['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=mei, color='red')
mei1.set_xticks(mei['Tanggal'].dt.day)
mei1.legend(['Total Kasus', 'Sembuh', 'Meninggal'])
plt.title('Kasus Covid-19 Mei 2020')
mei1.set_xlabel('Tanggal')
mei1.set_ylabel('Total Kasus')
plt.text(4, 26550, int(mei['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 25450, int(mei['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 24350, int(mei['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()


dfgrowthjun = df[coleamonth][2:4]
print(dfgrowthjun)

juni1 = sns.lineplot(x=juni['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=juni)
juni1 = sns.lineplot(x=juni['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=juni, color='green')
juni1 = sns.lineplot(x=juni['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=juni, color='red')
juni1.set_xticks(juni['Tanggal'].dt.day)
juni1.legend(['Total Kasus', 'Sembuh', 'Meninggal'])
plt.title('Kasus Covid-19 Juni 2020')
juni1.set_xlabel('Tanggal')
juni1.set_ylabel('Total Kasus')
plt.text(4, 56500, int(juni['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 54250, int(juni['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 51750, int(juni['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()


dfgrowthjul = df[coleamonth][3:5]
print(dfgrowthjul)

juli1 = sns.lineplot(x=juli['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=juli)
juli1 = sns.lineplot(x=juli['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=juli, color='green')
juli1 = sns.lineplot(x=juli['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=juli, color='red')
juli1.set_xticks(juli['Tanggal'].dt.day)
juli1.legend(['Total Kasus', 'Sembuh', 'Meninggal'])
plt.title('Kasus Covid-19 Juli 2020')
juli1.set_xlabel('Tanggal')
juli1.set_ylabel('Total Kasus')
plt.text(4, 109000, int(juli['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 104000, int(juli['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 99000, int(juli['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()


dfgrowthagu = df[coleamonth][4:6]
print(dfgrowthagu)

agus1 = sns.lineplot(x=agustus['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=agustus)
agus1 = sns.lineplot(x=agustus['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=agustus, color='green')
agus1 = sns.lineplot(x=agustus['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=agustus, color='red')
agus1.set_xticks(agustus['Tanggal'].dt.day)
agus1.legend(['Total Kasus', 'Sembuh', 'Meninggal'])
plt.title('Kasus Covid-19 Agustus 2020')
agus1.set_xlabel('Tanggal')
agus1.set_ylabel('Total Kasus')
plt.text(4, 175500, int(agustus['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 168000, int(agustus['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 160500, int(agustus['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()


dfgrowthsep = df[coleamonth][5:7]
print(dfgrowthsep)

sep1 = sns.lineplot(x=september['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=september)
sep1 = sns.lineplot(x=september['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=september, color='green')
sep1 = sns.lineplot(x=september['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=september, color='red')
sep1.set_xticks(september['Tanggal'].dt.day)
sep1.legend(['Total Kasus', 'Sembuh', 'Meninggal'])
plt.title('Kasus Covid-19 September 2020')
sep1.set_xlabel('Tanggal')
sep1.set_ylabel('Total Kasus')
plt.text(4, 288000, int(september['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 276000, int(september['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 264000, int(september['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()


dfgrowthokt = df[coleamonth][6:8]
print(dfgrowthokt)

okt1 = sns.lineplot(x=oktober['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=oktober)
okt1 = sns.lineplot(x=oktober['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=oktober, color='green')
okt1 = sns.lineplot(x=oktober['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=oktober, color='red')
okt1.set_xticks(oktober['Tanggal'].dt.day)
okt1.legend(['Total Kasus', 'Sembuh', 'Meninggal'])
plt.title('Kasus Covid-19 Oktober 2020')
okt1.set_xlabel('Tanggal')
okt1.set_ylabel('Total Kasus')
plt.text(4, 411000, int(oktober['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 394500, int(oktober['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 377000, int(oktober['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()