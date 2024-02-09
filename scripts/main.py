from data import *
from get_pins import *

def main():
    df = load_kaggle_data()
    
    query = "SELECT * FROM df ORDER BY genre ASC, popularity DESC"
    filename = "./index.html"

    ordered_df = sql_query(df, query)

    write_to_HTML(ordered_df, filename)
    scrape_and_pins("lover by taylor swift aesthetic", "lover-aesthetic")


if __name__ == "__main__":
    main()