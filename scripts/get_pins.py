from pinscrape import pinscrape

def scrape_and_pins(search_term: str, destination_folder: str):

    details = pinscrape.scraper.scrape(search_term, destination_folder, {}, 10, 15)
    
    if details["isDownloaded"]:
        print("\nDownloading completed !!")
        print(f"\nTotal urls found: {len(details['extracted_urls'])}")
        print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")
        print(details)
    else:
        print("\nNothing to download !!")
