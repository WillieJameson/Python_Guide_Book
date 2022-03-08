import requests
def gen_from_urls(urls: tuple) -> tuple:
  for resp in (requests.get(url) for url in urls):
    yield len(resp.content), resp.status_code, resp.url

"""The listcomp waits for all of its data to be produced before feeding any data
to the waiting for loop, whereas the generator releases data as soon as it becomes available. This means the for loop that uses the generator is much more responsive, as opposed to the listcomp (which makes you wait)."""

""" The yield keyword was added to Python to support the creation of generator functions, and you can use it anywhere a return is used."""

""""If you spot comprehension code surrounded by parentheses, you're looking at a generator (which can be turned into a function that itself uses yield to generate data as needed)."""