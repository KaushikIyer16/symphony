from chaos.search import SearchAgent

config = {
  "openai_api_key": "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",
  "google_api_key": "AIzaSyDcLZdN5Z_BUK9mOj-fuj4WWAbqYGgquz0",
  "google_cse_id": "b76747d94c23b42fe"
}
search = SearchAgent(google_api_key=config["google_api_key"], google_cse_id=config["google_cse_id"], openai_api_key=config["openai_api_key"])

def get_registry():
  return {
    "text-completion": search,
    "web-search": search,
    "scraping": search,
    "linkedin": search
  }