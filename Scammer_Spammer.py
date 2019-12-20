#Import Libraries
import names, requests, random, string, os, urllib3

#Add proxies here. Need both HTTP and HTTPS.
proxies = {
    'http': 'http://49.51.68.122:1080',
    'https': 'http://49.51.68.122:1080',
}

#Create the session and set the proxies.
s = requests.Session()
#Uncomment below if you need to use proxies.
#s.proxies = proxies

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

#Replace with Scammer URL (Should end in .PHP)
url = 'https://scvr-signinaccountprotection.nsupdate.info/action/post_signin.php'

while True:
    #Generate random first/last name
    first = names.get_first_name().lower()
    last = names.get_last_name().lower()

    #Generate 3 random numbers
    rando = ''.join(random.choice(string.digits))
    rando2 = ''.join(random.choice(string.digits))
    rando3 = ''.join(random.choice(string.digits))

    #Chooses email format
    emailformat = random.choice([1,2,3,4,5,6,7,8,9,10,11])
    if emailformat == 1:        
        name = first + last + rando + rando2 + rando3
    if emailformat == 2:
        name = first + '_' + last + rando + rando2 + rando3
    if emailformat == 3:
        name = first + '-' + last + rando + rando2
    if emailformat == 4:
        name = last + first + rando + rando2 + rando3
    if emailformat == 5:
        name = first + rando + rando2 + last
    if emailformat == 6:
        name = last + rando + rando2 + rando3 + first
    if emailformat == 7:
        name = last + '-' + first + '-' + rando + rando2 + rando3 
    if emailformat == 8:
        name = first + last
    if emailformat == 9:
        name = last + first
    if emailformat == 10:
        name = first + rando + rando2 + rando3
    if emailformat == 11:
        name = first + '_' + last


    #Chooses email provider
    pickprov = random.choice([1,1,2,3,4,5,6,7,8,9])
    if pickprov == 1:
        username = name.lower() + '@yahoo.com'
    if pickprov == 2:
        username = name.lower() + '@gmail.com'
    if pickprov == 3:
        username = name.lower() + '@gmx.com'
    if pickprov == 4:
        username = name.lower() + '@icloud.com'
    if pickprov == 5:
        username = name.lower() + '@mail.com'
    if pickprov == 6:
        username = name.lower() + '@gmx.us'
    if pickprov == 7:
        username = name.lower() + '@outlook.com'
    if pickprov == 8:
        username = name.lower() + '@aol.com'
    if pickprov == 9:
        username = name.lower() + '@comcast.net'

    #Chooses randomly generated password between 8-16 characters long
    password = ''.join(random.choice(chars) for i in range(random.choice([8,9,10,11,12,13,14,15,16])))

    #Chooses screen resolution
    randomresolution = random.choice([1,2,3,4])
    if randomresolution == 1:
        #720P
        resolution = '1280 x 720'
        windowreso = '1213 x 612'
    if randomresolution == 2:
        #1080P
        resolution = '1920 x 1080'
        windowreso = '1853 x 972'
    if randomresolution == 3:
        #1366 x 768
        resolution = '1366 x 768'
        windowreso = '1299 x 660'
    if randomresolution == 4:
        #1440 x 900
        resolution = '1440 x 900'
        windowreso = '1373 x 792'
    idk = '-6'

    #Disables HTTPS warning
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    #Make post request
    #Replace parameters as needed.
    s.post(url, allow_redirects=False, verify=False, data={
        '913f9c49dcb544e2087cee284f4a00b7': resolution,
        '8e3f1bbb73f0f6c952fcf873332eae9f': windowreso,
        'b2c6cc48f97ccd71b16d31d88fc177a6': idk,
		'0c83f57c786a0b4a39efab23731c7ebc': username,
		'5f4dcc3b5aa765d61d8327deb882cf99': password
	})

    #prints output
    print()
    print("Sending username: " + username + " and Password: " + password )
    print("Resolutions: " + resolution + " and " + windowreso)
    print("To: " + url)