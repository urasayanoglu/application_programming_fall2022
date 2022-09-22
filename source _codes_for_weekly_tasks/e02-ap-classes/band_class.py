
class Band:
    """A basic attempt to model a band."""

    def __init__(self, name=str, genre=str, local_awards=0, global_awards=0,):
        """Initialize band name and music genre attributes."""
        self.band_name = name
        self.music_genre = genre
        self.home_awards = local_awards
        self.international_awards = global_awards
        self.members_positions = {} 

    def describe_band(self):
        """Describe the band name and its music genre."""
        print(f"The band's name is {self.band_name.title()} and its genre is {self.music_genre.lower()}.")

    def band_members(self, name, position):
        """Introduce band members with their positions."""
        self.members_positions[name] = position

    def describe_members(self):
        """Describe the Band members with their positions."""
        for member, position in self.members_positions.items():
            print(f"{member} is in the role of {position} in the band {self.band_name}")

    def band_slogan(self, slogan=str):
        """Announce the slogan that the band is famous for."""
        print(f"{slogan.capitalize()} is the most famous slogan for the band {self.band_name.title()}.")

    def is_active(self, band_active=True):
        """Announce status of the band."""
        if band_active:
            print(f"The {self.band_name.title()} is active.")
        else:
            print(f"The {self.band_name.title()} is not active at the moment.")

    def set_home_awards(self,home_awards_number=int):
        """Set the number of awards that the band got locally."""
        self.home_awards += home_awards_number

    def set_international_awards(self, international_awards_number=int):
        """Set the number of awards that the band got internationally."""
        self.international_awards += international_awards_number

my_favorite_group = Band("Stratovarius", "Speed-Metal")
print(my_favorite_group.band_name)
print(my_favorite_group.music_genre)
my_favorite_group.describe_band()
my_favorite_group.is_active()


festival_band1 = Band("Judas Priest", "Heavy-Metal")
festival_band2 = Band("Rammstein", "Industrial-Metal")
festival_band3 = Band("W.A.S.P", "Heavy-Metal")
festival_band1.band_members("Ian Hill", "Bass")
festival_band1.band_members("Rob Halfords", "Vocals")
festival_band1.describe_members()

festival_band1.describe_band()
festival_band2.describe_band()
festival_band3.describe_band()

god_of_rock = Band("ACϟDC", "Hard Rock")
print(f"The band {god_of_rock.band_name.upper()} won {god_of_rock.home_awards} amount of local awards and {god_of_rock.international_awards} amount of global awards.")
another_god_of_rock = Band("Deep Purple", "Hard Rock", 0, 2)
print(f"The band {another_god_of_rock.band_name.title()} won {another_god_of_rock.home_awards} amount of local awards and {another_god_of_rock.international_awards} amount of global awards.")

god_of_rock.set_home_awards(5)
print(f"The band {god_of_rock.band_name.upper()} won {god_of_rock.home_awards} amount of local awards and {god_of_rock.international_awards} amount of global awards.")

another_god_of_rock.set_international_awards(6)
print(f"The band {another_god_of_rock.band_name.title()} won {another_god_of_rock.home_awards} amount of local awards and {another_god_of_rock.international_awards} amount of global awards.")

class RockBand(Band):
    """A basic attempt to model a rock band."""

    def __init__(self, name, genre, local_awards=0, global_awards=0):
        """Represent aspects of a band , specific to rock bands."""
        super().__init__(name, genre, local_awards=0, global_awards=0)
        self.rock_concert_movements = {
            1: "The Basic Head Bob", 
            2: "The One-Armed Fist Pump", 
            3: "The Up and Down Jumping Motion",
            4: "The Behind the Head Leg Stretch", 
            6: "Two Armed Upward Thrust with Yell",
            8: "The Black Out", 
            10: "Getting a Closer Look at the Audience", 
            15: "Bringing a Guest Vocalist Onstage",
            23: "Getting the Audience to Sing Along", 
            27: "Saying Hello to the People in the Cheap Seats", 
            28: "Getting an Audience Member Onstage to Dance", 
            32: "The Mosh Pit (Skitzo)",
            37: "The 'Waiting-around-for-the-show-to-start' Motion", 
            48: "Introducing the Band",
            63: "Bringing out Venus Hum", 
            69: "Circle Pit (TinMan)", 
            78: "The Fake Ending", 
            91: "Enjoying the T-Shirt You Bought at The Complex Rock Tour", 
            616: "Slam Dancing (TinMan)"}

    def display_concert_movements(self):
        """Display the rock concert movements."""
        for key, value in self.rock_concert_movements.items():
            print(f"Number {key} rock concert movement is {value}.")

    def band_slogan(self):
        print(f"Long live Rock 'N Roll!")


stairway_to_heawen = RockBand("Led Zeppeling", "Hard Rock")
stairway_to_heawen.display_concert_movements()
print(stairway_to_heawen.band_name)


class Choir(Band):
    """A basic attempt to model a Choir"""

    def __init__(self, name, genre="choral", local_awards=0, global_awards=0):
        """Represent aspects of a band , specific to a choir."""
        super().__init__(name, genre, local_awards=0, global_awards=0)

    def describe_band(self):
        """Describe the band name and its music genre."""
        print(f"The choir's name is {self.band_name.title()} and its genre is {self.music_genre}.")

    def band_members(self, name, voice_part):
        """Introduce choir members with their positions."""
        self.members_positions[name] = voice_part

    def describe_members(self):
        """Describe the choir members with the parts they sing in the choir."""
        for member, voice in self.members_positions.items():
            print(f"{member} sings in {voice} part in the band {self.band_name.title()}.")

    
loimaa_choir = Choir("Metsämaan kappelikuoro")
loimaa_choir.band_members("Kaija Huhtanen", "Soprano")
loimaa_choir.band_members("Marjukka Lehtola", "Alto")
loimaa_choir.describe_members()