import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sensor_data.csv")

print(df)

print(df.head(3))

# 温度の統計分析
print("温度の平均:", df["temperature"].mean())
print("温度の最大:", df["temperature"].max())
print("温度の最小:", df["temperature"].min())

#湿度の統計分析
print("湿度の平均:", df["humidity"].mean())
print("湿度の最大:", df["humidity"].max())
print("湿度の最小:",df["humidity"].min())

# 温度の折れ線グラフ
plt.plot(df["time"], df["temperature"])

# グラフのタイトル
plt.title("Temperature Graph")

# 横軸と縦軸の名前
plt.xlabel("Time")
plt.ylabel("Temperature (C)")

# グラフを画像として保存
plt.savefig("temperature.png")

# グラフを表示
plt.show()




# 分析結果を表にまとめる
result_df = pd.DataFrame({
    "item": ["temperature", "humidity"],
    "mean": [df["temperature"].mean(), df["humidity"].mean()],
    "max": [df["temperature"].max(), df["humidity"].max()],
    "min": [df["temperature"].min(), df["humidity"].min()]
})

# 分析結果を表示
print(result_df)

# CSVファイルとして保存
result_df.to_csv("summary.csv", index=False)
