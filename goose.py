# https://api.github.com
import requests, sys

base_URL = 'https://api.github.com'
username = sys.argv[1]
pull_requests = "/repos/{owner}/{repo}/pulls/{pull_number}/reviews"
user_repos = f"/users/{username}/repos"
response = requests.get(f"{base_URL}{user_repos}")
data = response.json()

def get_language(data_obj):
    return data_obj["language"]


fave_languages = list(map(get_language, data))

def calculate_fave_language(langs):
    max_count = 0
    fave_language = ""
    extra_languages = []
    language_count = dict((x, langs.count(x)) for x in set(langs))

    for language, count in language_count.items():
      print(f"incrementing language {language}")
      if count > max_count:
        fave_language = language
        max_count = count
      elif count == max_count:
        extra_languages.append(language)

    return fave_language


def text_to_display(language):
  if language != "None":
    print(f"Your favourite language is {language}")

calculate_fave_language(fave_languages)


