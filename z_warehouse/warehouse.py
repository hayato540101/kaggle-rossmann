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

'''特徴量'''
# 時系列特徴量作成
2015-09-17
data['year'] = data.Date.apply(lambda x: x.split('-')[0])
data['year'] = data['year'].astype(float)
data['month'] = data.Date.apply(lambda x: x.split('-')[1])
data['month'] = data['month'].astype(float)
data['day'] = data.Date.apply(lambda x: x.split('-')[2])
data['day'] = data['day'].astype(float)

'''所感'''

- メモリ削減はいいけど、int8,int16あたりにしているとどっかで列操作するときに上限・下限を超えて数値がバグってしまうことが考慮しなければならない。