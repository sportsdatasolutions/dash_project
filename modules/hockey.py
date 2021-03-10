import requests
import pandas as pd

def scrape_rankings(gender):
    response = requests.get(f"https://fih-rankings-live.herokuapp.com/api/rankings/{gender}").json()
    wr = response[0]['countries']
    wr_df = pd.DataFrame(wr)
    wr_df = wr_df[['rank','gender','code','name','points','last_updated_at','last_match','first_match']]
    return wr_df
