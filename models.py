import pickle


def load_model(model_path="classifier_model/email_classifier.pkl"):
    with open(model_path, "rb") as file:
        return pickle.load(file)


def predict_category(email_text, model):
    return model.predict([email_text])[0]
