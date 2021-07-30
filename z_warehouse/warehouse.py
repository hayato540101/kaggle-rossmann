# いつもの
import os
os.listdir('../../')


'''EDA&&基本的な前処理'''
# 売り上げが0なのにOpenが1(=Openしているのに売り上げが0)なのはさすがにおかしい、実務だと理由がありそうだが、訓練データに関しては「売上0の時は店が開いていない」と置換してもよいはず
# モデルはOpenの時売り上げが0になるとは限らないと学習してしまう
# train[train['Sales']==0].Open.value_counts()
# 0    172817
# 1        54

# OPENしていない日は流石にすべての売り上げが0になっている
# train[train['Open']==0].Sales.value_counts()

# 以下のコードでSalesが0の時Openを0に置換
# train['Open'] = train['Open'].where(train['Sales']!=0, 0)

# train['Sales']が0の時、Openは通常0と考えられるので、
# Sales!=0を満たさないものつまりSales=0の時のOpenを0に置換する
# 条件式がFalseのものを置換する点がちょっと紛らわしいので注意
train['Open'] = train['Open'].where(train['Sales']!=0, 0)
train[train['Open']==0].Sales.value_counts()


# 休日フラグを立ててみよう
# The day of the week with Monday=0, Sunday=6.
# 5と6を1、それ以外を0としてみる
tmp = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1}
train['non-working day'] = train['DayOfWeek'].map(tmp)
# こういうの確認するときはクエリの方が便利
# train.query("DayOfWeek==5 or DayOfWeek==6")['DayOfWeek'].value_counts()





'''特徴量'''
# 時系列特徴量作成
2015-09-17
data['year'] = data.Date.apply(lambda x: x.split('-')[0])
data['year'] = data['year'].astype(float)
data['month'] = data.Date.apply(lambda x: x.split('-')[1])
data['month'] = data['month'].astype(float)
data['day'] = data.Date.apply(lambda x: x.split('-')[2])
data['day'] = data['day'].astype(float)


train.query("Sales==1")




'''メモリ対策'''
# importするやつ
import sys, os
sys.path.append('../src/') #モジュールが入っているディレクトリのパスを指定
import eda
# 実行コード
import warnings
warnings.simplefilter('ignore')
ntrain_x = eda.reduce_mem_usage(train_x)

# オブジェクトのメモリ使用量確認 
modellist.__sizeof__()

# ndarrayの型確認
a.dtype

# メモ
train.query("Sales==1")

# デバッグ方法2通り
https://qiita.com/Kobayashi2019/items/98e74110d74e4c60f617#rreturn
%debug
import pdb; pdb.set_trace()





'''所感'''

- メモリ削減はいいけど、int8,int16あたりにしているとどっかで列操作するときに上限・下限を超えて数値がバグってしまうことが考慮しなければならない。

# 2021年7月30日以降
- コミットを意味のある単位で分けて、後から見て理解できるように
- 他人の理解を助ける目的でのコミットメッセージを書く

- 最後は関数に落とし込んだほうが作業内容が分けやすく何かと便利


