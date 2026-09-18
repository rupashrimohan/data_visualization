import requests
from operator import itemgetter
import plotly.express as px

# Make an API call and check the response
# We want to create a dictionary of key value pair that contains information about the submissions. like (Title,Discussion link and comments)

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code : {r.status_code}")
if r.status_code != 200:
    print(f"Failed to fetch data: {r.json().get('message', 'Unknown error')}")
    exit()
# process information
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make an API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    # print(f"id: {submission_id}\t status: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict.get("descendants", 0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

comments, submission_links, hover_texts = [], [], []
for sub_dict in submission_dicts:
    comments.append(sub_dict["comments"])
    title_link = f"<a href='{sub_dict["hn_link"]}'>{sub_dict["title"]}</a>"
    submission_links.append(title_link)
    hover_texts.append(
        f"<b>{sub_dict["title"]}</b><br />Comments: {sub_dict['comments']}"
    )


# for sub_dict in submission_dicts:
#     print(f"\nTitle: {submission_dict['title']}")
#     print(f"Discussion link:{submission_dict['hn_link']}")
#     print(f"Comments: {submission_dict['comments']}")

# Create the bar chart
title = "Most Active Discussions Currently Happening on Hacker News"
label = {"x": "Submission Title", "y": "No of Comments"}
fig = px.bar(
    x=submission_links, y=comments, labels=label, title=title, hover_name=hover_texts
)
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=18,
    yaxis_title_font_size=18,
    margin=dict(b=250),
)
fig.update_traces(
    marker_color="rgb(152, 63, 228)",
    marker_opacity=0.7,
    hovertemplate="%{hovertext}<extra></extra>",
)
fig.show()
