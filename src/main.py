from inference import predict_currency

def main():
    class_names = ["10 INR", "20 INR", "50 INR", "100 INR", "200 INR", "500 INR", "2000 INR"]
    result = predict_currency("models/currency_model.h5", "D:\\Projects all\\All GITHUB PROJECTS TO UPLOAD\\Z FOLDERS OF ALL THE MAIN TOPICS\\Computer_Vision\\Currency_Note_Recognition\\data\\raw\\500.jpg", class_names)
    print("Predicted currency note:", result)

if __name__ == "__main__":
    main()
