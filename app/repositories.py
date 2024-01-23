from database import get_db
from models import User, Subject, Rule


class UserRepository:
    @classmethod
    def create_user(cls, 
                    user_id: int,
                    user_chat_id: int,
                    first_name: str, 
                    last_name: str = "",
                    username: str = "", 
                    ):
        with get_db() as session:
            user = User(user_id=user_id, 
                        user_chat_id=user_chat_id, 
                        user_first_name=first_name, 
                        user_last_name=last_name, 
                        user_username=username
                        ) 
            session.add(user)
            session.commit()


class SubjectRepository:
    @classmethod
    def create_subject(cls,
                       user_id: int,
                       user_chat_id: int,
                       user_first_name: str,
                       user_last_name: str = "",
                       user_username: str = ""
                       ):
        
        with get_db() as session:
            sbj = Subject(user_id=user_id, 
                        user_chat_id=user_chat_id, 
                        user_first_name=user_first_name, 
                        user_last_name=user_last_name, 
                        user_username=user_username
                        ) 
            session.add(sbj)
            session.commit()


