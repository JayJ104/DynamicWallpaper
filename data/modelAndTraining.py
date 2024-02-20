import tensorflow as tf
from PIL import Image
print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train, x_test
#batch size: 1 since we have like no data lol
model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(2, 3, activation='relu', input_shape=(640, 640, 3), padding='same'),
  #2 filters of a 3x3 kernel, image height, image width, 3 color channels (rgb)
  tf.keras.layers.Conv2D(2, 3, activation='relu', padding='same'), #2 filters of a 3x3 kernel
  tf.keras.layers.GlobalAveragePooling2D(keepdims = True),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Conv2D(2, 3, activation='relu', padding='same'), #2 filters of a 3x3 kernel
  tf.keras.layers.Conv2D(2, 3, activation='relu', padding='same'), #2 filters of a 3x3 kernel
  tf.keras.layers.GlobalAveragePooling1D(keepdims = True),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(8) #what structure is fully connected layer?
])

predictions = model(x_train[:1]).numpy()
print(predictions)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test,  y_test, verbose=2)

