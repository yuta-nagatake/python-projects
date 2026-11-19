import csv
from collections import defaultdict

# 商品ごとの売上を保存
sales = defaultdict(lambda: [0, 0])

# CSVファイルを読み込む
with open("sales.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        name = row["商品"]
        quantity = int(row["数量"])
        price = int(row["単価"])

        sales[name][0] += quantity
        sales[name][1] += quantity * price

# 集計結果をCSVに保存
with open("result.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["商品", "数量", "売上"])

    for name, values in sales.items():
        writer.writerow([name, *values])

# 結果を表示
for name, values in sales.items():
    print(f"{name}: {values[0]}個、{values[1]}円")

print("合計売上:", sum(v[1] for v in sales.values()), "円")
print("result.csvを作成しました")
