# nanに対する処理結果検証
a = np.array([0,1,2,3,4,5,6,7,8,9,10,np.nan])
np.clip(a, 1, 8)
np.log1p(a)


日本の祝日フラグを立てられるらしい。今回はロシアなのでどうするかな、、、
jpholiday
https://upura.hatenablog.com/entry/2018/12/21/070000
うのみにせず処理後のチェックは必要。

# .ipynb->.py
jupyter nbconvert --to python xxxx.ipynb