from fastapi.responses import JSONResponse

def add_cookie(response, jwt):
	month = 5
	max_age = (((60*60)*24)*(30*month))
	response.set_cookie(key="jwt", value=jwt, max_age=max_age)
	return response


def register_view(jwt):
	if jwt:
		response = JSONResponse(status_code=200, content={"success":True,"message":"вы регистрировались"})
		return add_cookie(response,jwt)
	else:
		return JSONResponse(status_code=400, content={"success":False,"message":"email уже существует"})

def login_view(jwt):
	if jwt:
		response = JSONResponse(status_code=200, content={"success":True,"message":"вы успешно вошли"})
		return add_cookie(response,jwt)
	else:
		return JSONResponse(status_code=400, content={"success":False,"message":"email или пароль не правильный"})

def taskAdd_view(jwt):
	if jwt:
		return JSONResponse(status_code=200, content={"success":True,"message":jwt})
	else:
		return not_user()

def get_tasks_view(tasks):
	if type(tasks) == list:
		return JSONResponse(status_code=200, content={"success":True,"message":tasks})
	else:
		return not_user()

def not_user():
	return JSONResponse(status_code=400, content={"success":False,"message":"вы не пользватель"})

def updateTasks(is_True:bool):
	if is_True:
		return JSONResponse(status_code=200, content={"success":True,"message":True})
	else:
		return JSONResponse(status_code=400, content={"success":False,"message":"Не обнавился."})

def not_filter():
	return JSONResponse(status_code=400, content={"success":False,"message":"Фильтр не прваильный"})