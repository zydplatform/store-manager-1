
from app.models import  attendants

class Attendants:

    def __init__(self, id_number, attendant_name, attendant_username, attendant_password):
        self.id_number = id_number
        self.attendant_name = attendant_name
        self.attendant_username = attendant_username
        self.attendant_password = attendant_password

    def add_store_attendant(self):
        attendant = {
            "attendant_id" : attendants[-1]["attendant_id"]+1,
            "id_number" : self.id_number,
            "attendant_name" : self.attendant_name,
            "attendant_username" : self.attendant_username,
            "attendant_password" : self.attendant_password
        }

        if attendant in attendants or [
                                    attendant for attendant in attendants
                                    if attendant["id_number"] ==  self.id_number
                                    and attendant["attendant_name"] ==  self.attendant_name
                                    and attendant["attendant_username"] == self.attendant_username
                                    and attendant["attendant_password"] ==  self.attendant_password
                                ]:
            return False

        else:
            attendants.append(attendant)
            return True
    
    def update_store_attendant(self, attendant):
        if len(attendant) == 0:
            return False
        else:
            if attendant[0]["id_number"] != self.id_number:
                attendant[0]["id_number"] = self.id_number

            if attendant[0]["attendant_name"] != self.attendant_name:
                attendant[0]["attendant_name"] = self.attendant_name

            if attendant[0]["attendant_username"] != self.attendant_username:
                attendant[0]["attendant_username"] = self.attendant_username

            if attendant[0]["attendant_password"] != self.attendant_password:
                attendant[0]["attendant_password"] = self.attendant_password

            return True

