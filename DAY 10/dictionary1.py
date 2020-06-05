digit={"ten":10,
      "Twenty":20,
      "Thirty":30}

digit.update({"Forty":40})

for key,value in digit.items():
    print(key+"--------"+str(value))