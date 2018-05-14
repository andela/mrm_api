import jwt
from flask import current_app, request, jsonify
from admin_schema import admin_schema
from helpers.database import db_session
from api.user.models import User

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
    return jsonify({ 'message' : 'This endpoint requires you to be authenticated.'}), 401

  def decode_token(self, auth_token):
    """ Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    SECRET_KEY = current_app.config['SECRET_KEY']
    
    try:
      payload = jwt.decode(auth_token, SECRET_KEY)
      return payload
    except jwt.ExpiredSignatureError:
      return jsonify({ 'message':'Signature expired. Please log in again.'}), 401

    except jwt.InvalidTokenError:
      return jsonify({ 'message': 'Invalid token. Please Provied a valid token!'}), 401

  def is_admin(self, token):
    value = self.verify(token)

    if type(value) is dict:

      user_email = value['UserInfo']['email']

      query = '''
      query{
        user(email: "'''+user_email+'''"){
          id
          email
          name
          }
        }
      '''
      result = admin_schema.execute(query, context_value={'session': db_session})

      try:
        
        result_user = list(result.data.items())        
        result_user[0][1]
        email = list(result_user[0][1].items())
        
        if user_email == email[1][1]:
          return True

      except:
        pass
    else:
      return value
    return jsonify({ 'message':'Your can are not authroized to accesst this route.'}), 401
  
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