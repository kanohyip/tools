import util
import pyperclip


try:
    util.kintai()
    util.initTeams()
except Exception as e:
    pyperclip.copy(util.text_startRemoteWork)