from flask import Session
from functools import wraps


def check_logged_in(func):
  @wraps (func)
  def wrapper(*args, **kwargs):
    if 'logged_in' in Session:
      return func(*args, **kwargs)
    return 'You are NOT logged in'
  return wrapper