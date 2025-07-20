from figo_score_calculator import calculate_score

if __name__ == "__main__":
    result = calculate_score("data/EU_FIGO_IIGO_Relations.csv")
    print(result.head())
