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


UserRepository.create_user(1234,567,"first_name_user_test")


