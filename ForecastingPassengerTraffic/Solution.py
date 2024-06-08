from statsmodels.tsa.ar_model import AutoReg as AR

N = int(input())

data = []
for i in range(N):
    data.append(int(input().split()[1]))

model = AR(data, lags=1)
fitted_model = model.fit()
pred = fitted_model.predict()[:12]

for i in pred:
    print(i, end ='\n')
