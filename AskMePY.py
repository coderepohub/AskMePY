import wolframalpha
import wikipedia

app_id = "YOUR_WOLFRAMALPHA_API_KEY"
client = wolframalpha.Client(app_id)

def start_Wolframalpha_Query(q):
    res = client.query(input_data)
    result = next(res.results).text
    print(result,"\n")

def start_Wikipedia_Query(q):
    wikisummary = wikipedia.summary(q)
    print(wikisummary , "\n")

while True:
        try:
            input_data = input("Query : ")
            start_Wolframalpha_Query(input_data)
        except:
            start_Wikipedia_Query(input_data)

