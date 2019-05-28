from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("recycled_set")
model_trainer.trainModel(num_objects=3, num_experiments=10, enhance_data=True, batch_size=20, show_network_summary=True)
#3 classes, 10 epoch, batch size 16 to cater to GPU memory
#https://towardsdatascience.com/train-image-recognition-ai-with-5-lines-of-code-8ed0bdd8d9ba