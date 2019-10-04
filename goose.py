# https://api.github.com
import requests, sys
from backend.paths import test

base_URL = 'https://api.github.com'
username = sys.argv[1]
pull_requests = "/repos/{owner}/{repo}/pulls/{pull_number}/reviews"
user_repos = f"/users/{username}/repos"
rate_limit = "/rate_limit"

print(test)

def make_request(url, path):
  return requests.get(f"{url}{path}")

response = make_request(base_URL, rate_limit)

data = response.json()
error = response.json()
print(data)

def get_language(data_obj):
    if error:
      print(error["message"])
      sys.exit()
    else:
      return data_obj["language"]


fave_languages = list(map(get_language, data))

def calculate_fave_language(langs):
    max_count = 0
    fave_language = ""
    extra_languages = []
    language_count = dict((x, langs.count(x)) for x in set(langs))

    for language, count in language_count.items():
      if count > max_count:
        fave_language = language
        max_count = count
      elif count == max_count:
        extra_languages.append(language)

    return fave_language


def text_to_display(language):
  if language != None:
    print(f"Your favorite language is {language}")
  elif language == None:
    print("You either have a lot of repositories with READMEs or are empty. Go write code!")
  else:
    print("Sorry, our systems are currently not working; we apologise that you are unable to find your favourite language.")

calculate_fave_language(fave_languages)

text_to_display(calculate_fave_language(fave_languages))

