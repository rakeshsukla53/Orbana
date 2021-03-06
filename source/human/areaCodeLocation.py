
from geopy import geocoders

import collections

from human.models import Phone, State


y = open("output.txt", 'r')

d = {'216': 'Cleveland, OH', '217': 'Chicago, IL', '214': 'Dallas, TX', '215': 'Philadelphia, PA', '212': 'New York, NY', '213': 'Los Angeles, CA', '210': 'San Antonio, TX', '667': 'Baltimore, MD', '763': 'Minneapolis, MN', '760': 'San Diego, CA', '662': 'Southaven, MS', '218': 'Duluth, MN', '219': 'Valparaiso, IN', '769': 'Jackson, MS', '620': 'Hutchinson, KS', '937': 'Dayton, OH', '804': 'Richmond, VA', '779': 'Rockford, IL', '949': 'Santa Ana, CA', '507': 'Rochester, MN', '775': 'Reno, NV', '669': 'San Jose, CA', '980': 'Charlotte, NC', '651': 'Minneapolis, MN', '289': 'Woodbridge, ON', '406': 'Billings, MT', '346': 'Houston, TX', '347': 'Brooklyn, NY', '340': 'Charlotte Amalie, VI', '402': 'Omaha, NE', '401': 'Providence, RI', '343': 'Vankleek Hill, ON', '281': 'Houston, TX', '919': 'Raleigh, NC', '812': 'Evansville, IN', '813': 'Tampa, FL', '814': 'Erie, PA', '571': 'Alexandria, VA', '409': 'Beaumont, TX', '408': 'San Jose, CA', '570': 'Wilkes Barre, PA', '678': 'Atlanta, GA', '719': 'Colorado Springs, CO', '718': 'Brooklyn, NY', '717': 'Lancaster, PA', '716': 'Buffalo, NY', '715': 'Green Bay, WI', '714': 'Long Beach, CA', '670': 'Saipan, NN', '671': 'Santa Rita, GU', '618': 'Belleville, IL', '262': 'Milwaukee, WI', '260': 'Fort Wayne, IN', '267': 'Philadelphia, PA', '661': 'Bakersfield, CA', '269': 'Kalamazoo, MI', '660': 'Otterville, MO', '970': 'Ft Collins, CO', '917': 'Brooklyn, NY', '906': 'Deerton, MI', '701': 'Fargo, ND', '916': 'Sacramento, CA', '954': 'Fort Lauderdale, FL', '765': 'Indianapolis, IN', '619': 'San Diego, CA', '910': 'Fayetteville, NC', '414': 'Milwaukee, WI', '415': 'San Francisco, CA', '416': 'Toronto, ON', '417': 'Springfield, MO', '410': 'Baltimore, MD', '828': 'Asheville, NC', '412': 'Pittsburgh, PA', '413': 'Springfield, MA', '920': 'Milwaukee, WI', '912': 'Savannah, GA', '418': 'Ville Degelis, QC', '419': 'Toledo, OH', '539': 'Tulsa, OK', '586': 'Detroit, MI', '319': 'Cedar Rapids, IA', '318': 'Shreveport, LA', '708': 'Chicago, IL', '709': 'Woody Point, NL', '587': 'Wetaskiwin, AB', '313': 'Detroit, MI', '312': 'Chicago, IL', '706': 'Augusta, GA', '310': 'Los Angeles, CA', '317': 'Indianapolis, IN', '316': 'Wichita, KS', '315': 'Syracuse, NY', '314': 'Saint Louis, MO', '270': 'Bowling Green, KY', '272': 'Lake Ariel, PA', '585': 'Buffalo, NY', '276': 'Martinsville, VA', '703': 'Alexandria, VA', '984': 'Raleigh, NC', '770': 'Atlanta, GA', '832': 'Houston, TX', '647': 'Toronto, ON', '830': 'New Braunfels, TX', '831': 'Salinas, CA', '580': 'Oklahoma City, OK', '762': 'Augusta, GA', '929': 'Brooklyn, NY', '747': 'Los Angeles, CA', '581': 'Vallee Jonction, QC', '713': 'Houston, TX', '612': 'Minneapolis, MN', '985': 'New Orleans, LA', '534': 'Chippewa Falls, WI', '520': 'Phoenix, AZ', '918': 'Tulsa, OK', '442': 'Victorville, CA', '915': 'El Paso, TX', '914': 'Manhattan, NY', '423': 'Chattanooga, TN', '365': 'Tottenham, ON', '425': 'Seattle, WA', '424': 'Los Angeles, CA', '360': 'Seattle, WA', '361': 'Corpus Christi, TX', '308': 'Grand Island, NE', '309': 'Peoria, IL', '440': 'Cleveland, OH', '531': 'Lincoln, NE', '516': 'Springfield Gardens, NY', '512': 'Austin, TX', '443': 'Baltimore, MD', '301': 'Baltimore, MD', '302': 'Wilmington, DE', '303': 'Denver, CO', '304': 'Charleston, WV', '305': 'Miami, FL', '306': 'Yorkton, SK', '307': 'Casper, WY', '240': 'Baltimore, MD', '386': 'Daytona Beach, FL', '773': 'Chicago, IL', '973': 'Newark, NJ', '249': 'Whitefish Falls, ON', '248': 'Detroit, MI', '972': 'Dallas, TX', '847': 'Chicago, IL', '785': 'Topeka, KS', '786': 'Miami, FL', '787': 'Bayamon, PR', '780': 'Zama, AB', '781': 'Boston, MA', '904': 'Jacksonville, FL', '905': 'Woodbridge, ON', '908': 'Newark, NJ', '903': 'Tyler, TX', '772': 'Port Saint Lucie, FL', '601': 'Jackson, MS', '737': 'Austin, TX', '519': 'Zurich, ON', '518': 'Schenectady, NY', '438': 'Saint Genevieve, QC', '646': 'Brooklyn, NY', '437': 'Toronto, ON', '434': 'Lynchburg, VA', '435': 'Park City, UT', '432': 'Midland, TX', '514': 'Saint Genevieve, QC', '430': 'Longview, TX', '385': 'Salt Lake City, UT', '458': 'Eugene, OR', '740': 'Columbus, OH', '579': 'Waterloo, QC', '540': 'Fredericksburg, VA', '339': 'Boston, MA', '626': 'Los Angeles, CA', '843': 'Charleston, SC', '450': 'Yamaska, QC', '334': 'Montgomery, AL', '337': 'Lafayette, LA', '336': 'Greensboro, NC', '331': 'Lemont, IL', '330': 'Akron, OH', '575': 'Las Cruces, NM', '574': 'South Bend, IN', '989': 'Saginaw, MI', '801': 'Salt Lake City, UT', '252': 'Greenville, NC', '253': 'Seattle, WA', '250': 'Zeballos, BC', '251': 'Mobile, AL', '256': 'Huntsville, AL', '913': 'Kansas City, KS', '254': 'Killeen, TX', '407': 'Orlando, FL', '613': 'Yarker, ON', '857': 'Boston, MA', '850': 'Pensacola, FL', '517': 'Lansing, MI', '971': 'Portland, OR', '819': 'Yamachiche, QC', '530': 'Sacramento, CA', '858': 'San Diego, CA', '405': 'Oklahoma City, OK', '979': 'College Station, TX', '978': 'Boston, MA', '731': 'Jackson, TN', '657': 'Long Beach, CA', '404': 'Atlanta, GA', '734': 'Detroit, MI', '508': 'Boston, MA', '509': 'Spokane, WA', '506': 'Youngs Cove Road, NB', '403': 'Youngstown, AB', '504': 'New Orleans, LA', '505': 'Albuquerque, NM', '502': 'Louisville, KY', '503': 'Portland, OR', '501': 'Little Rock, AR', '630': 'Chicago, IL', '631': 'Deer Park, NY', '707': 'Santa Rosa, CA', '469': 'Dallas, TX', '650': 'San Jose, CA', '636': 'Saint Louis, MO', '754': 'Fort Lauderdale, FL', '561': 'West Palm Beach, FL', '562': 'Los Angeles, CA', '563': 'Davenport, IA', '845': 'Poughkeepsie, NY', '567': 'Toledo, OH', '810': 'Flint, MI', '901': 'Memphis, TN', '702': 'Las Vegas, NV', '229': 'Albany, GA', '228': 'Gulfport, MS', '226': 'Wyoming, ON', '225': 'Baton Rouge, LA', '224': 'Chicago, IL', '856': 'Camden, NJ', '931': 'Clarksville, TN', '623': 'Phoenix, AZ', '907': 'Anchorage, AK', '802': 'Shelburne, VT', '704': 'Charlotte, NC', '864': 'Greenville, SC', '860': 'Hartford, CT', '863': 'Kissimmee, FL', '862': 'Newark, NJ', '865': 'Knoxville, TN', '815': 'Chicago, IL', '867': 'Yellowknife, NT', '805': 'Bakersfield, CA', '727': 'Tampa, FL', '724': 'Pittsburgh, PA', '725': 'Las Vegas, NV', '816': 'Kansas City, MO', '720': 'Denver, CO', '947': 'Southfield, MI', '757': 'Virginia Beach, VA', '925': 'Oakland, CA', '817': 'Dallas, TX', '936': 'Conroe, TX', '605': 'Sioux Falls, SD', '604': 'Yale, BC', '607': 'Freeville, NY', '606': 'Sharpsburg, KY', '559': 'Fresno, CA', '603': 'Manchester, NH', '602': 'Phoenix, AZ', '928': 'Phoenix, AZ', '551': 'Newark, NJ', '608': 'Madison, WI', '541': 'Eugene, OR', '239': 'Fort Myers, FL', '234': 'Akron, OH', '712': 'Sioux City, IA', '236': 'Victoria, BC', '848': 'Newark, NJ', '231': 'Muskegon, MI', '732': 'Newark, NJ', '641': 'Beaman, IA', '909': 'Riverside, CA', '878': 'Pittsburgh, PA', '951': 'Riverside, CA', '778': 'Youbou, BC', '952': 'Minneapolis, MN', '872': 'Chicago, IL', '873': 'Woburn, QC', '870': 'Jonesboro, AR', '956': 'Laredo, TX', '323': 'Los Angeles, CA', '320': 'Saint Cloud, MN', '321': 'Orlando, FL', '325': 'Abilene, TX', '938': 'Goodwater, AL', '807': 'Wunumin Lake, ON', '201': 'Newark, NJ', '774': 'Boston, MA', '203': 'New Haven, CT', '202': 'Washington, DC', '205': 'Birmingham, AL', '204': 'Yorkton, MB', '207': 'Portland, ME', '206': 'Seattle, WA', '209': 'Fresno, CA', '208': 'Boise, ID', '610': 'Philadelphia, PA', '616': 'Grand Rapids, MI', '617': 'Boston, MA', '614': 'Columbus, OH', '615': 'Nashville, TN', '939': 'Bayamon, PR', '859': 'Lexington, KY', '510': 'San Jose, CA', '484': 'Philadelphia, PA', '513': 'Cincinnati, OH', '573': 'Columbia, MO', '480': 'Phoenix, AZ', '902': 'Yarmouth, NS', '479': 'Springdale, AR', '818': 'Los Angeles, CA', '705': 'Woodville, ON', '515': 'Des Moines, IA', '609': 'Camden, NJ', '940': 'Denton, TX', '941': 'Sarasota, FL', '470': 'Atlanta, GA', '808': 'Honolulu, HI', '352': 'Gainesville, FL', '351': 'Danvers, MA', '475': 'New Haven, CT', '803': 'Columbia, SC', '684': 'Pago Pago, AS', '478': 'Macon, GA', '431': 'Winnipeg, MB', '681': 'Charleston, WV', '806': 'Lubbock, TX', '639': 'Regina, SK', '682': 'Dallas, TX'}

phoneNumbers = []
g = geocoders.GoogleV3()

for line in y:

    phoneNumbers.append(int(line))

counter = collections.Counter(phoneNumbers)

for i in zip(sorted(counter.keys())[::-1], sorted(counter.values())[::-1]):

    line = str(list(i)[0])
    frequency = list(i)[1]
    key = str(line[0:3]);
    location = d.get(key)
    try:
        if location:
            state_id = location.split(",")[1].strip()
            state  = State.objects.get(state_name = state_id)
            place, (lat, lng) = g.geocode(location)
            print place, lat, lng
            p = Phone(phone_number=int(line), area_code=int(key), frequency=frequency,location=place, latitude= lat,longitude=lng, state=state)
            p.save()
    except Exception as e:
        print e

















