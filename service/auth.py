from .JWT import decode_access_token
from models.crud import SessionCRUD

async def is_user(db, jwt:str):
	if jwt == None:
		return False

	session_id = await decode_access_token(jwt)

	sesCrud = SessionCRUD(db)
	ses = await sesCrud.get_by_id(session_id.get("id"))
	if ses:
		return str(ses.user_id)
	else:
		return False