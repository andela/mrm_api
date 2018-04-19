from flask import current_app, request
import jwt

class Authentication():
  """ Authenicate token 
    :methods
        verify
        decode_token
        is_admin
  """

  def verify(self, token):
    """ verify token
      :params token
      :return: func|string
    """
    if token:
      return self.decode_token(token)
    return 'Please Provied a valid token!'

  def decode_token(self, auth_token):
    """ Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    secret_key = current_app.config['SECRET_KEY']
    
    try:
      payload = jwt.decode(auth_token, 'me')
      return payload
    except jwt.ExpiredSignatureError:
      return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
      return 'Invalid token. Please Provied a valid token!'

  def is_admin(self, token):
    value = self.verify(token)

    if type(value) is dict:
      if value['role'] == 'Admin':
        return True
    else:
      return value
    return 'Your can are not authroized to accesst this route.', 401
  
  def auth_required(self, fn):
    """ Protects endpoint
       :params: function
       :return: function
    """
    def wrapper(*args, **kwargs):
        """ Wrapper function
          takes all the arguments that comes with the incoming function
          makes sure that the end point has a token
          :returns: func|string
        """
        token = request.headers.get('token')
        validate_token = self.is_admin(token)
        if validate_token == True:
            return fn(*args, **kwargs)
        return validate_token
    return wrapper

Auth = Authentication()