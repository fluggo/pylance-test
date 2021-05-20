import jwt

# This should be an error because payload expects Dict[str, Any]
jwt.encode(payload='subsandwich')
