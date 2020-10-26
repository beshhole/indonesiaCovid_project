import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 12)

# dataset taken from https://bnpb-inacovid19.hub.arcgis.com/datasets/statistik-perkembangan-covid19-indonesia-new/data?orderBy=Tanggal&orderByAsc=false
data = pd.read_csv('E:/.../Statistik_Perkembangan_COVID19_Indonesia_New.csv')

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

# MARET

margrowth = maret['Jumlah_Kasus_Kumulatif'].iloc[-1]

# mar = sns.lineplot(x=maret['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=maret)
# mar.set_xticks(maret['Tanggal'].dt.day)
# plt.title('Covid19 Case March')
# plt.text(1, 1500, 'Total case = ' + str(maret['Jumlah_Kasus_Kumulatif'].iloc[-1]))
# plt.text(1, 1400, f'Case growth = {margrowth}')
# plt.xlabel('Date')
# plt.ylabel('Total Case')
# plt.show()

marrecgrowth = (maret['Jumlah_Pasien_Sembuh'].iloc[-1]) - (maret['Jumlah_Pasien_Sembuh'].iloc[0])
marrecperc = (maret['Jumlah_Pasien_Sembuh'].iloc[-1] / maret['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100

# marrec = sns.lineplot(x=maret['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=maret)
# marrec.set_xticks(maret['Tanggal'].dt.day)
# plt.title('Covid19 Recovered March')
# plt.text(1, 80, 'Total recovered = ' + str(maret['Jumlah_Pasien_Sembuh'].iloc[-1]))
# plt.text(1, 76, f'Recovered growth = {marrecgrowth}')
# plt.text(1, 72, 'Recovered % = ' + '%.02f' % marrecperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Recovered')
# plt.show()

mardeagrowth = (maret['Jumlah_Pasien_Meninggal'].iloc[-1]) - (maret['Jumlah_Pasien_Meninggal'].iloc[0])
mardeaperc = (maret['Jumlah_Pasien_Meninggal'].iloc[-1] / maret['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
#
# mardea = sns.lineplot(x=maret['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=maret)
# mardea.set_xticks(maret['Tanggal'].dt.day)
# plt.title('Covid19 Death March')
# plt.text(1, 135, 'Total Death = ' + str(maret['Jumlah_Pasien_Meninggal'].iloc[-1]))
# plt.text(1, 127, f'Death growth = {mardeagrowth}')
# plt.text(1, 119, 'Death % = ' + '%.02f' % mardeaperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Death')
# plt.show()

# APRIL

aprgrowth = (april['Jumlah_Kasus_Kumulatif'].iloc[-1]) - (maret['Jumlah_Kasus_Kumulatif'].iloc[-1])

# apr = sns.lineplot(x=april['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=april)
# apr.set_xticks(april['Tanggal'].dt.day)
# plt.title('Covid19 Case April')
# plt.text(1, 10000, 'Total Case = ' + str(april['Jumlah_Kasus_Kumulatif'].iloc[-1]))
# plt.text(1, 9500, f'Case growth = {aprgrowth}')
# plt.xlabel('Date')
# plt.ylabel('Total Case')
# plt.show()

aprrecgrowth = (april['Jumlah_Pasien_Sembuh'].iloc[-1]) - (maret['Jumlah_Pasien_Sembuh'].iloc[-1])
aprrecperc = (aprrecgrowth / aprgrowth) * 100

# aprrec = sns.lineplot(x=april['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=april)
# aprrec.set_xticks(april['Tanggal'].dt.day)
# plt.title('Covid19 Recovered April')
# plt.text(1, 1500, 'Total recovered = ' + str(april['Jumlah_Pasien_Sembuh'].iloc[-1]))
# plt.text(1, 1420, f'Recovered growth = {aprrecgrowth}')
# plt.text(1, 1340, 'Recovered % = ' + '%.02f' % aprrecperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Recovered')
# plt.show()

aprdeagrowth = (april['Jumlah_Pasien_Meninggal'].iloc[-1]) - (maret['Jumlah_Pasien_Meninggal'].iloc[-1])
aprdeaperc = (aprdeagrowth / aprgrowth) * 100

# aprdea = sns.lineplot(x=april['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=april)
# aprdea.set_xticks(april['Tanggal'].dt.day)
# plt.title('Covid19 Death April')
# plt.text(1, 780, 'Total death = ' + str(april['Jumlah_Pasien_Meninggal'].iloc[-1]))
# plt.text(1, 750, f'Death growth = {aprdeagrowth}')
# plt.text(1, 720, 'Death % = ' + '%.02f' % aprdeaperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Death')
# plt.show()

# MEI

meigrowth = (mei['Jumlah_Kasus_Kumulatif'].iloc[-1]) - (april['Jumlah_Kasus_Kumulatif'].iloc[-1])
#
# mei1 = sns.lineplot(x=mei['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=mei)
# mei1.set_xticks(mei['Tanggal'].dt.day)
# plt.title('Covid19 Case May')
# plt.text(1, 26000, 'Total case = ' + str(mei['Jumlah_Kasus_Kumulatif'].iloc[-1]))
# plt.text(1, 25000, f'Case growth = {meigrowth}')
# plt.xlabel('Date')
# plt.ylabel('Total Case')
# plt.show()
#
meirecgrowth = (mei['Jumlah_Pasien_Sembuh'].iloc[-1]) - (april['Jumlah_Pasien_Sembuh'].iloc[-1])
meirecperc = (meirecgrowth / meigrowth) * 100
#
# meirec = sns.lineplot(x=mei['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=mei)
# meirec.set_xticks(mei['Tanggal'].dt.day)
# plt.title('Covid19 Recovered May')
# plt.text(1, 7000, 'Total recovered = ' + str(mei['Jumlah_Pasien_Sembuh'].iloc[-1]))
# plt.text(1, 6700, f'Recovered growth = {meirecgrowth}')
# plt.text(1, 6400, 'Recovered % = ' + '%.02f' % meirecperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Recovered')
# plt.show()
#
meideagrowth = (mei['Jumlah_Pasien_Meninggal'].iloc[-1]) - (april['Jumlah_Pasien_Meninggal'].iloc[-1])
meideaperc = (meideagrowth / meigrowth) * 100
#
# meidea = sns.lineplot(x=mei['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=mei)
# meidea.set_xticks(mei['Tanggal'].dt.day)
# plt.title('Covid19 Death May')
# plt.text(1, 1600, 'Total death =' + str(mei['Jumlah_Pasien_Meninggal'].iloc[-1]))
# plt.text(1, 1550, f'Death growth = {meideagrowth}')
# plt.text(1, 1500, 'Death percentage = ' + '%.02f' % meideaperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Death')
# plt.show()

# JUNI

jungrowth = (juni['Jumlah_Kasus_Kumulatif'].iloc[-1]) - (mei['Jumlah_Kasus_Kumulatif'].iloc[-1])
#
# jun = sns.lineplot(x=juni['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=juni)
# jun.set_xticks(juni['Tanggal'].dt.day)
# plt.title('Covid19 Case June')
# plt.text(1, 55000, 'Total case = ' + str(juni['Jumlah_Kasus_Kumulatif'].iloc[-1]))
# plt.text(1, 53500, f'Case growth = {jungrowth}')
# plt.xlabel('Date')
# plt.ylabel('Total Case')
# plt.show()
#
junrecgrowth = (juni['Jumlah_Pasien_Sembuh'].iloc[-1]) - (mei['Jumlah_Pasien_Sembuh'].iloc[-1])
junrecperc = (junrecgrowth / jungrowth) * 100

# junrec = sns.lineplot(x=juni['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=juni)
# junrec.set_xticks(juni['Tanggal'].dt.day)
# plt.title('Covid19 Recovered June')
# plt.text(1, 24000, 'Total recovered = ' + str(juni['Jumlah_Pasien_Sembuh'].iloc[-1]))
# plt.text(1, 23000, f'Recovered growth = {junrecgrowth}')
# plt.text(1, 22000, 'Recovered % = ' + '%.02f' % junrecperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Recovered')
# plt.show()
#
jundeagrowth = (juni['Jumlah_Pasien_Meninggal'].iloc[-1]) - (mei['Jumlah_Pasien_Meninggal'].iloc[-1])
jundeaperc = (jundeagrowth / jungrowth) * 100

# jundea = sns.lineplot(x=juni['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=juni)
# jundea.set_xticks(juni['Tanggal'].dt.day)
# plt.title('Covid19 Death June')
# plt.text(1, 2800, 'Total death = ' + str(juni['Jumlah_Pasien_Meninggal'].iloc[-1]))
# plt.text(1, 2750, f'Death growth = {jundeagrowth}')
# plt.text(1, 2700, 'Death % = ' + '%.02f' % jundeaperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Death')
# plt.show()

# JULI

julgrowth = (juli['Jumlah_Kasus_Kumulatif'].iloc[-1]) - (juni['Jumlah_Kasus_Kumulatif'].iloc[-1])
#
# jul = sns.lineplot(x=juli['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=juli)
# jul.set_xticks(juli['Tanggal'].dt.day)
# plt.title('Covid19 Case July')
# plt.text(1, 108000, 'total kasus = ' + str(juli['Jumlah_Kasus_Kumulatif'].iloc[-1]))
# plt.text(1, 105000, f'growth = {julgrowth}')
# plt.xlabel('Date')
# plt.ylabel('Total Case')
# plt.show()
#
julrecgrowth = (juli['Jumlah_Pasien_Sembuh'].iloc[-1]) - (juni['Jumlah_Pasien_Sembuh'].iloc[-1])
julrecperc = (julrecgrowth / julgrowth) * 100
#
# julrec = sns.lineplot(x=juli['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=juli)
# julrec.set_xticks(juli['Tanggal'].dt.day)
# plt.title('Covid19 Recovered July')
# plt.text(1, 63000, f'growth = {julrecgrowth}')
# plt.text(1, 65000, 'recovery percentage = ' + '%.02f' % julrecperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Recovered')
# plt.show()
#
juldeagrowth = (juli['Jumlah_Pasien_Meninggal'].iloc[-1]) - (juni['Jumlah_Pasien_Meninggal'].iloc[-1])
juldeaperc = (juldeagrowth / julgrowth) * 100
#
# juldea = sns.lineplot(x=juli['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=juli)
# juldea.set_xticks(juli['Tanggal'].dt.day)
# plt.title('Covid19 Death July')
# plt.text(1, 4900, f'growth = {juldeagrowth}')
# plt.text(1, 5000, 'death percentage = ' + '%.02f' % juldeaperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Death')
# plt.show()

# AGUSTUS

agugrowth = (agustus['Jumlah_Kasus_Kumulatif'].iloc[-1]) - (juli['Jumlah_Kasus_Kumulatif'].iloc[-1])
#
# agu = sns.lineplot(x=agustus['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=agustus)
# agu.set_xticks(agustus['Tanggal'].dt.day)
# plt.title('Covid19 Case August')
# plt.text(1, 171000, 'total kasus = ' + str(agustus['Jumlah_Kasus_Kumulatif'].iloc[-1]))
# plt.text(1, 168000, f'growth = {agugrowth}')
# plt.xlabel('Date')
# plt.ylabel('Total Case')
# plt.show()
#
agurecgrowth = (agustus['Jumlah_Pasien_Sembuh'].iloc[-1]) - (juli['Jumlah_Pasien_Sembuh'].iloc[-1])
agurecperc = (agurecgrowth / agugrowth) * 100
#
# agurec = sns.lineplot(x=agustus['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=agustus)
# agurec.set_xticks(agustus['Tanggal'].dt.day)
# plt.title('Covid19 Recovered August')
# plt.text(1, 119000, f'growth = {agurecgrowth}')
# plt.text(1, 122000, 'recovery percentage = ' + '%.02f' % agurecperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Recovered')
# plt.show()
#
agudeagrowth = (agustus['Jumlah_Pasien_Meninggal'].iloc[-1]) - (juli['Jumlah_Pasien_Meninggal'].iloc[-1])
agudeaperc = (agudeagrowth / agugrowth) * 100
#
# agudea = sns.lineplot(x=agustus['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=agustus)
# agudea.set_xticks(agustus['Tanggal'].dt.day)
# plt.title('Covid19 Death August')
# plt.text(1, 7100, f'growth = {agudeagrowth}')
# plt.text(1, 7300, 'death percentage = ' + '%.02f' % agudeaperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Death')
# plt.show()

# SEPTEMBER

sepgrowth = (september['Jumlah_Kasus_Kumulatif'].iloc[-1]) - (agustus['Jumlah_Kasus_Kumulatif'].iloc[-1])
#
# sep = sns.lineplot(x=september['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=september)
# sep.set_xticks(september['Tanggal'].dt.day)
# plt.title('Covid19 Case September')
# plt.text(1, 281000, 'total kasus = ' + str(september['Jumlah_Kasus_Kumulatif'].iloc[-1]))
# plt.text(1, 276000, f'growth = {sepgrowth}')
# plt.xlabel('Date')
# plt.ylabel('Total Case')
# plt.show()
#
seprecgrowth = (september['Jumlah_Pasien_Sembuh'].iloc[-1]) - (agustus['Jumlah_Pasien_Sembuh'].iloc[-1])
seprecperc = (seprecgrowth / sepgrowth) * 100
#
# seprec = sns.lineplot(x=september['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=september)
# seprec.set_xticks(september['Tanggal'].dt.day)
# plt.title('Covid19 Recovered September')
# plt.text(1, 205500, f'growth = {seprecgrowth}')
# plt.text(1, 210000, 'recovery percentage = ' + '%.02f' % seprecperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Recovered')
# plt.show()
#
sepdeagrowth = (september['Jumlah_Pasien_Meninggal'].iloc[-1]) - (agustus['Jumlah_Pasien_Meninggal'].iloc[-1])
sepdeaperc = (sepdeagrowth / sepgrowth) * 100
#
# sepdea = sns.lineplot(x=september['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=september)
# sepdea.set_xticks(september['Tanggal'].dt.day)
# plt.title('Covid19 Death September')
# plt.text(1, 10400, f'growth = {sepdeagrowth}')
# plt.text(1, 10600, 'death percentage = ' + '%.02f' % sepdeaperc + r'%')
# plt.xlabel('Date')
# plt.ylabel('Total Death')
# plt.show()

print(data.tail())
print(data.head())
print(data.info())

dfmonths = ['March', 'April', 'May', 'June', 'July', 'August', 'September']
df1 = pd.DataFrame({'Month': dfmonths}).reset_index(drop=True)

dfkumulatif = data['Jumlah_Kasus_Kumulatif'].groupby(data['Tanggal'].dt.month).tail(1)[:7]
dfgrowth = [margrowth, aprgrowth, meigrowth, jungrowth, julgrowth, agugrowth, sepgrowth]
df2 = pd.DataFrame({'Total Case': dfkumulatif, 'Case Growth': dfgrowth}).reset_index(drop=True)
df12 = pd.concat([df1, df2], axis=1)
# print(df12)

marrec = (maret['Jumlah_Pasien_Sembuh'].iloc[-1] / maret['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
aprrec = (april['Jumlah_Pasien_Sembuh'].iloc[-1] / april['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
meirec = (mei['Jumlah_Pasien_Sembuh'].iloc[-1] / mei['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
junrec = (juni['Jumlah_Pasien_Sembuh'].iloc[-1] / juni['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
julrec = (juli['Jumlah_Pasien_Sembuh'].iloc[-1] / juli['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
agurec = (agustus['Jumlah_Pasien_Sembuh'].iloc[-1] / agustus['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
seprec = (september['Jumlah_Pasien_Sembuh'].iloc[-1] / september['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100

dfrec = data['Jumlah_Pasien_Sembuh'].groupby(data['Tanggal'].dt.month).tail(1)[:7]
dfrecgrowthperc = ['%.01f'%marrec+r'%', '%.01f'%aprrec+r'%', '%.01f'%meirec+r'%', '%.01f'%junrec+r'%', '%.01f'%julrec+r'%', '%.01f'%agurec+r'%', '%.01f'%seprec+r'%']
dfrecgrowth = [marrecgrowth, aprrecgrowth, meirecgrowth, junrecgrowth, julrecgrowth, agurecgrowth, seprecgrowth]
df3 = pd.DataFrame({'Total Recovered': dfrec, 'Recovered Growth': dfrecgrowth, r'Recovered %': dfrecgrowthperc}).reset_index(drop=True)
df13 = pd.concat([df1, df3], axis=1)
# print(df13)

mardea = (maret['Jumlah_Pasien_Meninggal'].iloc[-1] / maret['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
aprdea = (april['Jumlah_Pasien_Meninggal'].iloc[-1] / april['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
meidea = (mei['Jumlah_Pasien_Meninggal'].iloc[-1] / mei['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
jundea = (juni['Jumlah_Pasien_Meninggal'].iloc[-1] / juni['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
juldea = (juli['Jumlah_Pasien_Meninggal'].iloc[-1] / juli['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
agudea = (agustus['Jumlah_Pasien_Meninggal'].iloc[-1] / agustus['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100
sepdea = (september['Jumlah_Pasien_Meninggal'].iloc[-1] / september['Jumlah_Kasus_Kumulatif'].iloc[-1]) * 100

dfdea = data['Jumlah_Pasien_Meninggal'].groupby(data['Tanggal'].dt.month).tail(1)[:7]
dfdeagrowthperc = ['%.01f'%mardea+r'%', '%.01f'%aprdea+r'%', '%.01f'%meidea+r'%', '%.01f'%jundea+r'%', '%.01f'%juldea+r'%', '%.01f'%agudea+r'%', '%.01f'%sepdea+r'%']
dfdeagrowth = [mardeagrowth, aprdeagrowth, meideagrowth, jundeagrowth, juldeagrowth, agudeagrowth, sepdeagrowth]
df4 = pd.DataFrame({'Total Death': dfdea, 'Death Growth': dfdeagrowth, r'Death %': dfdeagrowthperc}).reset_index(drop=True)
df14 = pd.concat([df1, df4], axis=1)
# print(df14)

df = pd.concat([df1, df2, df3, df4], axis=1)
df.set_index('Month', inplace=True)
print(df)
#
ax = sns.lineplot(x='Month', y='Total Case', data=df)
ax = sns.lineplot(x='Month', y='Total Recovered', data=df, color='green')
ax = sns.lineplot(x='Month', y='Total Death', data=df, color='red')
ax.legend(['Total Case', 'Recovered', 'Death'])
plt.title('Indonesia Covid-19 Case')
plt.text(0.6, 288000, str(september['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(0.6, 276000, str(september['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(0.6, 264000, str(september['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()

# ax1 = sns.lineplot(x='Month', y='Recovered %', data=df)
# ax1 = sns.lineplot(x='Month', y='Death %', data=df)
# ax1.legend(['Recovered %', 'Death %'])
# ax1.set_ylim(0,100)
# plt.show()

maret1 = sns.lineplot(x=maret['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=maret)
maret1 = sns.lineplot(x=maret['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=maret, color='green')
maret1 = sns.lineplot(x=maret['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=maret, color='red')
maret1.set_xticks(maret['Tanggal'].dt.day)
maret1.legend(['Total Case', 'Recovered', 'Death'])
plt.title('Covid-19 Case March')
maret1.set_xlabel('Date')
maret1.set_ylabel('Total Case')
plt.text(5, 1530, str(maret['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(5, 1465, str(maret['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(5, 1400, str(maret['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()

april1 = sns.lineplot(x=april['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=april)
april1 = sns.lineplot(x=april['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=april, color='green')
april1 = sns.lineplot(x=april['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=april, color='red')
april1.set_xticks(april['Tanggal'].dt.day)
april1.legend(['Total Case', 'Recovered', 'Death'])
plt.title('Covid-19 Case April')
april1.set_xlabel('Date')
april1.set_ylabel('Total Case')
plt.text(4, 10150, str(april['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 9700, str(april['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 9250, str(april['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()

mei1 = sns.lineplot(x=mei['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=mei)
mei1 = sns.lineplot(x=mei['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=mei, color='green')
mei1 = sns.lineplot(x=mei['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=mei, color='red')
mei1.set_xticks(mei['Tanggal'].dt.day)
mei1.legend(['Total Case', 'Recovered', 'Death'])
plt.title('Covid-19 Case May')
mei1.set_xlabel('Date')
mei1.set_ylabel('Total Case')
plt.text(4, 26550, str(mei['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 25450, str(mei['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 24350, str(mei['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()

juni1 = sns.lineplot(x=juni['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=juni)
juni1 = sns.lineplot(x=juni['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=juni, color='green')
juni1 = sns.lineplot(x=juni['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=juni, color='red')
juni1.set_xticks(juni['Tanggal'].dt.day)
juni1.legend(['Total Case', 'Recovered', 'Death'])
plt.title('Covid-19 Case June')
juni1.set_xlabel('Date')
juni1.set_ylabel('Total Case')
plt.text(4, 56500, str(juni['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 54250, str(juni['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 51750, str(juni['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()

juli1 = sns.lineplot(x=juli['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=juli)
juli1 = sns.lineplot(x=juli['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=juli, color='green')
juli1 = sns.lineplot(x=juli['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=juli, color='red')
juli1.set_xticks(juli['Tanggal'].dt.day)
juli1.legend(['Total Case', 'Recovered', 'Death'])
plt.title('Covid-19 Case July')
juli1.set_xlabel('Date')
juli1.set_ylabel('Total Case')
plt.text(4, 109000, str(juli['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 104000, str(juli['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 99000, str(juli['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()

agus1 = sns.lineplot(x=agustus['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=agustus)
agus1 = sns.lineplot(x=agustus['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=agustus, color='green')
agus1 = sns.lineplot(x=agustus['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=agustus, color='red')
agus1.set_xticks(agustus['Tanggal'].dt.day)
agus1.legend(['Total Case', 'Recovered', 'Death'])
plt.title('Covid-19 Case August')
agus1.set_xlabel('Date')
agus1.set_ylabel('Total Case')
plt.text(4, 175500, str(agustus['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 168000, str(agustus['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 160500, str(agustus['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()

sep1 = sns.lineplot(x=september['Tanggal'].dt.day, y='Jumlah_Kasus_Kumulatif', data=september)
sep1 = sns.lineplot(x=september['Tanggal'].dt.day, y='Jumlah_Pasien_Sembuh', data=september, color='green')
sep1 = sns.lineplot(x=september['Tanggal'].dt.day, y='Jumlah_Pasien_Meninggal', data=september, color='red')
sep1.set_xticks(september['Tanggal'].dt.day)
sep1.legend(['Total Case', 'Recovered', 'Death'])
plt.title('Covid-19 Case September')
sep1.set_xlabel('Date')
sep1.set_ylabel('Total Case')
plt.text(4, 288000, str(september['Jumlah_Kasus_Kumulatif'].iloc[-1]))
plt.text(4, 276000, str(september['Jumlah_Pasien_Sembuh'].iloc[-1]))
plt.text(4, 264000, str(september['Jumlah_Pasien_Meninggal'].iloc[-1]))
plt.show()
