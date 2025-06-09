from fastapi.responses import JSONResponse

def register_view(jwt):
	if jwt:
		month = 5
		max_age = (((60*60)*24)*(30*month))
		response = JSONResponse(status_code=200, content={"success":True,"message":"вы регистрировались"})
		response.set_cookie(key="jwt", value=jwt, max_age=max_age)
		return response
	else:
		return JSONResponse(status_code=400, content={"success":False,"message":"email уже существует"})

def login_view(jwt):
	if jwt:
		month = 5
		max_age = (((60*60)*24)*(30*month))
		response = JSONResponse(status_code=200, content={"success":True,"message":"вы успешно вошли"})
		response.set_cookie(key="jwt", value=jwt, max_age=max_age)
		return response
	else:
		return JSONResponse(status_code=400, content={"success":False,"message":"email или пароль не правильный"})