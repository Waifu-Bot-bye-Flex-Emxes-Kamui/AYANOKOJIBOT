# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 14691251  # Get this value from my.telegram.org/apps
    API_HASH = "ce7153b02b496253947872656b3ee0d3"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://uctejkqi5g93cu:pff9e446e7c372fdaaf74c73e79b67e3a05773fa79afb629e02d18eb6e370155e@c7t0sffab2p4bc.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d4e72qim2do63q"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002078575375
    MESSAGE_DUMP = -1002078575375

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://mukundsrajput:lFRam73ZwE2D4snZ@cluster0.bmxejth.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "FLEX_Support_Chat"
    SUPPORT_ID = -1002100475470

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "7116566735:AAFOSx0aTLfpWpkM73OYjCypy6tUG4s6VfM"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6584789596
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = ["2010819209", "6584789596", "5702598840"]  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True
    BAN_STICKER = ""

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
