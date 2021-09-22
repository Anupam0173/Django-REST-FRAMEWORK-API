# Django-REST-FRAMEWORK-API

DJANGO REST FRAMEWORK
1)api view 2)api viewset

model will come in place of models.

normally by serializer and deseralizer
by @api_view() decorator
apiview   //class based view

Genericapiview and mixins
basic authentication and token authentication
viewsets
Genericviewsets  it is same as genericapiview
Modelviewsets     


--------------------------authentication------------------------------
in **basic authentication**:
inside the authorization tab we have to select **basic authentication** and provide the username and password.

in **token authentication** inside the header we have to specify authoriztion and it's token value.
authorization   token <token_value>     //in token authentication

in **jwt authentication** we have to specify the authorization and it's Bearer value.
authorization    Bearer <token_access_value>

api/token/      //is used for accessing the token.
reference -->https://www.geeksforgeeks.org/jwt-authentication-with-django-rest-framework/
