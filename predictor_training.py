import pandas as pd
import tensorflow

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import datetime

df = pd.read_csv('manual_data_random.csv')

X = pd.get_dummies(df.drop(['id', 'winner'], axis=1))
y = df['winner']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)

# print(y_train.head())

model = Sequential()
model.add(Dense(units=32, activation='relu', input_dim=len(X_train.columns)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

#print(model.summary())
#config = model.get_config()
#print(config["layers"][0]["config"]["batch_input_shape"])
#exit()

model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tensorflow.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# command for tensorboard
# python -m tensorboard.main --logdir logs/fit

model.fit(X_train, y_train, epochs=100, batch_size=32, callbacks=[tensorboard_callback], shuffle = True, validation_split = 0.2)


y_hat = model.predict(X_test)
y_hat = [0 if val < 0.5 else 1 for val in y_hat]

print("Accuracy is:")
print(accuracy_score(y_test, y_hat))

# print(y_hat)

# model.save('tfmodel')
# del model
# model = load_model('tfmodel')