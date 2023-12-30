import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error, r2_score

# データの取得
usd_jpy = yf.download('USDJPY=X', start='2015-01-01', end='2023-12-01')
data = usd_jpy.filter(['Close'])
dataset = data.values
training_data_len = int(np.ceil(len(dataset) * .8))

# データのスケーリング
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

# トレーニングデータセットの作成
train_data = scaled_data[0:int(training_data_len), :]
x_train, y_train = [], []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])
    
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# LSTMモデルの構築
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# モデルのコンパイルと訓練
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, batch_size=1, epochs=1)

# テストデータセットの作成
test_data = scaled_data[training_data_len - 60: , :]
x_test, y_test = [], dataset[training_data_len:, :]
for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# 価格予測値の取得
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# RMSE値の計算
rmse = np.sqrt(np.mean(((predictions - y_test) ** 2)))
print(f'RMSE: {rmse}')

# 予測精度の追加評価指標を計算
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f'mae: {mae}')
print(f'r: {r2}')

# 未来1年間の予測を格納するリスト
future_predictions = []

# 最後の観測日を取得
last_date = data.index[-1]

# 1年後までの予測を行うためのデータを準備
last_60_days = scaled_data[-600:]
current_batch = last_60_days.reshape((1, last_60_days.shape[0], 1))

# 1年後までの営業日のリストを生成（約252営業日）
future_dates = pd.date_range(start=last_date, periods=252)

# 1年間の予測を行う
for i in range(252):
    # 現在のバッチから予測を行う
    current_pred = model.predict(current_batch)[0]
    
    # 予測結果を保存
    future_predictions.append(current_pred)
    
    # バッチを更新（最古のデータを削除し、新しい予測値を追加）
    current_batch = np.append(current_batch[:,1:,:],[[current_pred]],axis=1)

# スケーラーを使用して元のスケールに戻す
future_predictions = scaler.inverse_transform(future_predictions)

# 予測結果をDataFrameに格納
future_df = pd.DataFrame(future_predictions, index=future_dates, columns=['Prediction'])

# 予測結果の表示
print(future_df)

# グラフのプロット
plt.figure(figsize=(10,6))
plt.plot(future_df['Prediction'])
plt.title('USD/JPY Exchange Rate Prediction for the Next Year')
plt.xlabel('Date')
plt.ylabel('Predicted Exchange Rate')
plt.show()

# データのプロット
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions

plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD (JPY)', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()