from re import compile

from telegram import Chat

LANGUAGES = ('українська', 'English', 'русский')
CHAT_TYPES = (Chat.PRIVATE, Chat.GROUP, Chat.SUPERGROUP)
ORDINARY_ROLE, ADMIN_ROLE, LEADER_ROLE = 0, 1, 2

DATABASE = '../../memory.db'
INITIAL_ROLE, INITIAL_FAMILIARITY = ORDINARY_ROLE, '000000000000000'
KPI_ID = 100

THRESHOLD_DATE = (8, 31)  # August 31, the last day before the next EDU year starts
NOTIFICATION_TIME = (7, 30)  # 07:30 AM, when notifications are sent
ECAMPUS_URL, ECAMPUS_THREADS, ECAMPUS_WAIT = 'https://ecampus.kpi.ua/login', 5, 10

EDU_YEAR_PATTERN = compile(r'(\d)+.+?(\d)+')
DATE_PATTERN = compile(r'(\d{1,2})\.(\d{1,2})(,? (\d{1,2}):(\d{1,2}))?')

MAX_GROUP_NAME_LENGTH = 15
MIN_GROUPMATES_FOR_LC, MAX_EDU_YEARS = 1, 6
MAX_ADMINS_STUDENTS_RATIO = .5
