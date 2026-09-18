import requests
import plotly.express as px

# Make an API call and check the response
print(
    "Hi, I am going to show the popular repos in guthub based on the language you select."
)
print(
    "Please give an input of a language that you want to visualize (Python/Javascript/Ruby)"
)
VALID_LANGUAGES = {"python", "javascript", "ruby"}
while True:
    language = input("Enter the language (Python/Javascript/Ruby): ").strip().lower()
    if language in VALID_LANGUAGES:
        break
    print(
        f"'{language}' is not recognized. Please choose from Python, Javascript, or Ruby.\n"
    )

url = "https://api.github.com/search/repositories"
url += f"?q=language:{language}+sort:stars+stars:>1000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code:{r.status_code}")
if r.status_code != 200:
    print(f"Failed to fetch data: {r.json().get('message', 'Unknown error')}")
    exit()

# convert the response object to a dictionary
response_dict = r.json()

# Explore info about repos
repo_dicts = response_dict.get("items", [])
print(f"Repositories returned: {len(repo_dicts)}")

if not repo_dicts:
    print(f"No repositories found for '{language}'.")
    exit()

print(response_dict.keys())

print(f"Total repositories:{response_dict['total_count']}")
print(f"Complete Results:{not response_dict['incomplete_results']}")


print("\nSelected Information about first repository:")
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict["stargazers_count"])

    # Build hover text
    owner = repo_dict["owner"]["login"]
    description = repo_dict.get("description") or "No description provided."
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)


# Make visualization
title = f"Most-Starred {language.title()} Projects on Github"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)

fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
fig.show()
