# Module foutcodes

list = [
'ERR000: Module makesshcon : Er is een time-out opgetreden in de SSH-verbinding.',
'ERR001: Module ftpsettings : De gevraagde ftpsetting is niet gevonden.',
'ERR002',
'ERR003: Module makesshcon : De SSH connectie is opgezet.',
'ERR004: Module makesshcon : Het opzetten van de SSH connectie is mislukt.',
'ERR005: Module connections: Er is een niet-gedefiniëerd device opgevraagd.',
'ERR006',
'ERR007',
'ERR008',
'ERR009',
'ERR010: Module makesshcon : Het commando om de files te uploaden is uitgevoerd.',
'ERR011: De files zijn succesvol geback-upped.'
]

def foutcode(code):
    return list[code]
