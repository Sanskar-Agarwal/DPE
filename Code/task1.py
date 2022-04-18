import json
import pandas as pd
def task1():
    with open('/course/data/a1/engagements/HealthStory.json') as json_file:
        engagement_json= json.load(json_file)
    with open('/course/data/a1/reviews/HealthStory.json') as json_file:
        reviews_json= json.load(json_file)
    df rows=[]
    
    
    

    with open('task1.json', 'w') as fp:
        json.dump(engagement_json, fp)    


        
    return
