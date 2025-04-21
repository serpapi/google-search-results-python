from niquests import Session

DEFAULT_HTTP_CLIENT = Session(
    pool_maxsize=100,
)
