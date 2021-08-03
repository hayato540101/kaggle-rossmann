https://www.kaggle.com/c/rossmann-store-sales/overview

#### 特徴

- 予測対象：店の売り上げ
- 扱うデータの種類 テーブルデータ>時系列
- サイズ
- 指標：RMSPE



#### Score

|       提出ファイル       |       詳細       |       Private Leaderboard       |
| ---------------------- | ---------------------- | ---------------------- |
|  2021-07-30_18-13-47.csv  |  ここからbaseline作成  | 0.56260 |
|  rossmann_best_no_ext_data_scaled  |  13th solution  | 0.10199 |
|  2021-08-03_22-19-57.csv  |  + week and dayofyear  | 0.36472 |
|  2021-08-03_22-24-30.csv  |  except dayofyear  | 0.36853 |
|  2021-08-03_23-04-28.csv  |  make main store information | 0.34656 |


#### 方針
- pre_baselineここからbaseline作成
    - 時系列クロスバリデーション・複数モデルの重み付き平均まではできたはず
- バリデーションの確立
    - これをやらないと、理由が説明できる特徴量以外はどんなに作っても意味がない
    - EDAやdiscussionをみる

- 0803
    - week,dayofyear共にスコア改善に寄与、この二つとも「季節性」や「時期」に関する情報を与えられたのかも
    - storeテーブルのPromo2SinceWeek,Promo2SinceYear,PromoIntervalの情報以外を使用,これは今まで使用していなかった情報なのでスコア改善は理解できる
    - バリデーション手法に試行錯誤の余地がある


#### Kernel /10
<!-- my-15th-solution-features-mainly-using-bigquery -->

#### discussion
https://www.kaggle.com/c/rossmann-store-sales/discussion/18024