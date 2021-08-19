from Blessings import SaiBaba, AagasaVeeran
from Invitation import Invite
from HappilyEverAfter import Bride, Groom, Wedding

def invitation():
    '''
    ===================
    MARRIAGE INVITATION
    ===================
    '''
    wedding_invitation = str(SaiBaba()) + str(AagasaVeeran())
    
    wedding_invitation += Invite().message 
    
    wedding_invitation += "\n" + Bride().name + "," + Bride().qualification \
                            + "\n" + Bride().occupation + "\n"
    wedding_invitation += "\nWeds\n"
    wedding_invitation += "\n" + Groom().name + "," + Groom().qualification \
                            + "\n" + Groom().occupation + "\n"
    
    wedding_invitation += Wedding().reception
    wedding_invitation += Wedding().wedding
    
    wedding_invitation += Invite().compliment 

    return wedding_invitation

if __name__ == "__main__":
    print(invitation.__doc__)
    print(invitation())