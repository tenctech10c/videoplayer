class Bride:
    def __init__(self):
        self._name = "V. BHADRINATH"
        self._qualification = "B.Tech., M.B.A.,"
        self._occupation = "Software Engineer- BA Continuum Solutions, Chennai"
        
    @property
    def name(self):
        return self._name
    
    @property
    def qualification(self):
        return self._qualification
    
    @property
    def occupation(self):
        return self._occupation

class Groom:
    def __init__(self):
        self._name = "S. Jyothi Rupa"
        self._qualification = "B.E."
        self._occupation = "Product Engineer- UST, Trivandrum, Kerala"
        
    @property
    def name(self):
        return self._name
    
    @property
    def qualification(self):
        return self._qualification
    
    @property
    def occupation(self):
        return self._occupation
    
class Date:
    def __init__(self):
        self._day = "" #Dayname, 00th of Month YYYY
        self._time = "" #0.00 PM Onwards
        self._place = "" 
        
    @property
    def day(self):
        return self._day
        
    @day.setter
    def day(self, day):
        self._day = day
        
    @property
    def time(self):
        return self._time
        
    @time.setter
    def time(self, time):
        self._time = time
        
    @property
    def place(self):
        return self._place
        
    @place.setter
    def place(self, place):
        self._place = place
        
        
class Wedding:
    def __init__(self):
        self._reception = Date()
        self._reception.day = "Dayname, ??th of Month YYYY"
        self._reception.time = "?.?? PM Onwards" 
        self._reception.place = "AAA Marriage Hall,\nYYY Place,\nZZZ"
        self._wedding = Date()
        self._wedding.day = "Dayname, ??th of Month YYYY"
        self._wedding.time = "From ?.?? AM - ?.?? AM"
        self._wedding.place = "AAA Temple, ZZZ"
    
    @property
    def bride(self):
        return self._bride

    @property
    def groom(self):
        return self._groom

    @property
    def reception(self):
        return f"\nOn {self._reception._day} from {self._reception._time},\nat {self._reception._place}\n"

    @property
    def wedding(self):
        return f"\nMarriage: {self._wedding.day}\nTime: {self._wedding.day}\nVenue: {self._wedding.place}\n"
        
    