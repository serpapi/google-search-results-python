from niquests import AsyncSession

DEFAULT_HTTP_CLIENT = AsyncSession(
    pool_maxsize=100,
)
