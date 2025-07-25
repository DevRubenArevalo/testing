#This fetches data from the Universalis API for FFXIV items
#It retrieves the top 5 sales for each item in the specified list  
import requests
import json
import datetime
import time

def get_item_name(item_id, filename='items.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        item_dict = json.load(f)
    return item_dict.get(str(item_id), "Unknown Item")

# Example usage:
# item_id = "10001"
# item_name = get_item_name(item_id)
# print(f"Item name for ID {item_id}: {item_name}")

# === Mapping dictionaries ===
ITEM_NAMES = {
    "39474": "Corgi",
    "36255": "Ovibos Milk",
    "41758": "Heavens' Eye Materia XI"
}

WORLD_IDS = {
    21: "Ravana",       # Example world IDs
    22: "Bismarck",
    23: "Asura",
    24: "Belias",
    28: "Pandaemonium",
    29: "Shinryu",
    30: "Unicorn",
    31: "Yojimbo",
    32: "Zeromus",
    33: "Twintania",
    34: "Brynhildr",
    35: "Famfrit",
    36: "Lich",
    37: "Mateus",
    39: "Omega",
    40: "Jenova",
    41: "Zalera",
    42: "Zodiark",
    43: "Alexander",
    44: "Anima",
    45: "Carbuncle",
    46: "Fenrir",
    47: "Hades",
    48: "Ixion",
    49: "Kujata",
    50: "Typhon",
    51: "Ultima",
    52: "Valefor",
    53: "Exodus",
    54: "Faerie",
    55: "Lamia",
    56: "Phoenix",
    57: "Siren",
    58: "Garuda",
    59: "Ifrit",
    60: "Ramuh",
    61: "Titan",
    62: "Diabolos",
    63: "Gilgamesh",
    64: "Leviathan",
    65: "Midgardsormr",
    66: "Odin",
    67: "Shiva",
    68: "Atomos",
    69: "Bahamut",
    70: "Chocobo",
    71: "Moogle",
    72: "Tonberry",
    73: "Adamantoise",
    74: "Coeurl",
    75: "Malboro",
    76: "Tiamat",
    77: "Ultros",
    78: "Behemoth",
    79: "Cactuar",
    80: "Cerberus",
    81: "Goblin",
    82: "Mandragora",
    83: "Louisoix",
    85: "Spriggan",
    86: "Sephirot",
    87: "Sophia",
    88: "Zurvan",
    90: "Aegis",
    91: "Balmung",
    92: "Durandal",
    93: "Excalibur",
    94: "Gungnir",
    95: "Hyperion",
    96: "Masamune",
    97: "Ragnarok",
    98: "Ridill",
    99: "Sargatanas",
    400: "Sagittarius",
    401: "Phantom",
    402: "Alpha",
    403: "Raiden",
    404: "Marilith",
    405: "Seraph",
    406: "Halicarnassus",
    407: "Maduin",
    408: "Cuchulainn",
    409: "Kraken",
    410: "Rafflesia",
    411: "Golem",
    3000: "Cloudtest01",
    3001: "Cloudtest02",
    1167: "红玉海",
    1081: "神意之地",
    1042: "拉诺西亚",
    1044: "幻影群岛",
    1060: "萌芽池",
    1173: "宇宙和音",
    1174: "沃仙曦染",
    1175: "晨曦王座",
    1172: "白银乡",
    1076: "白金幻象",
    1171: "神拳痕",
    1170: "潮风亭",
    1113: "旅人栈桥",
    1121: "拂晓之间",
    1166: "龙巢神殿",
    1176: "梦羽宝境",
    1043: "紫水栈桥",
    1169: "延夏",
    1106: "静语庄园",
    1045: "摩杜纳",
    1177: "海猫茶屋",
    1178: "柔风海湾",
    1179: "琥珀原",
    1192: "水晶塔",
    1183: "银泪湖",
    1180: "太阳海岸",
    1186: "伊修加德",
    1201: "红茶川",
    1068: "黄金谷",
    1064: "月牙湾",
    1187: "雪松原",
    2075: "카벙클",
    2076: "초코보",
    2077: "모그리",
    2078: "톤베리",
    2080: "펜리르"
}

url = "https://universalis.app/api/v2/history/North-America/39474,36255,41758?minSalePrice=0&maxSalePrice=2147483647"
r = requests.get(url)
data = r.json()
print(f"Fetching data from Universalis API...")
print(f"Data fetched successfully. Number of items: {len(data['items'])}")
print(f"Today's date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
sales_output = []
for item_id, item_data in data['items'].items():
    item_name = ITEM_NAMES.get(str(item_id), f"Unknown ({item_id})")
    for sale in item_data['entries'][:5]:    # Show the top 5 sales per item
        quantity = sale['quantity']
        pricePerUnit = sale['pricePerUnit']
        worldID = sale['worldID']
        world_name = WORLD_IDS.get(worldID, f"Unknown ({worldID})")
        sales_output.append({
            "world": world_name,
            "item_name": item_name,
            "quantity": quantity,
            "price_per_unit": pricePerUnit
        })
    time.sleep(1/24)  # Sleep  for 1/24th of a second to avoid hitting API rate limits
print(json.dumps(sales_output, ensure_ascii=False, indent=2))