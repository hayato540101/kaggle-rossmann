# nanに対する処理結果検証
a = np.array([0,1,2,3,4,5,6,7,8,9,10,np.nan])
np.clip(a, 1, 8)
np.log1p(a)