# PyASF
Python library for further integration with ASF's IPC interface with data validation (Pydantic)

Python >= 3.12

### WARNING
> Work in progress! Tested with EN ASF ("CurrentCulture": "en")

### Plugins
| Name                      | Status      | Url                                               |
|:--------------------------|:------------|:--------------------------------------------------|
| `ASFEnhance`              | In progress | https://github.com/chr233/ASFEnhance              |
| `ASFTradeExtension `      | In progress | https://github.com/chr233/ASFTradeExtension       |
| `ASFAchievementManagerEx` | In progress | https://github.com/chr233/ASFAchievementManagerEx |
| `CS2Interface`            | In progress | https://github.com/Citrinate/CS2Interface         |



### Installation
```bash
pip install git+https://github.com/OliverTrust/pyasf
```

### Usage/Examples
Commands ASF level and balance
```python
from pyasf import API
from pyasf.asf import Command

ipc = "http://127.0.0.1:1242"
login = "GabeNewell"

api = API(ipc)
command = Command(api, login)

level = command.level()
print(level) # int 27
balance = command.balance()
print(balance) # obj amount=2.78 token=<Token.RUB: 'RUB'>
```

Commands ASFEnhance purchase game
```python
from pyasf import API
from pyasf.asf_enhance import Command

ipc = "http://127.0.0.1:1242"
login = "GabeNewell"

api = API(ipc)
command = Command(api, login)

command.addcart("s/645485") # bool True
command.purchase() # bool True
```

IPC CS2Interface get player profile
```python
from pyasf import API
from pyasf.cs2interface import IPC

ipc = "http://127.0.0.1:1242"
login = "GabeNewell"

api = API(ipc)
interface = IPC(api, login)

interface.start() # start cs2 game coordinator
profile = interface.playerprofile(76561199059082632)
print(profile)  # obj account_profiles=[AccountProfile(account_id=1098816904, ongoingmatch=None, global_stats=None, ranking=None, commendation=None, medals=Medals(display_items_defidx=[4906, 996], featured_display_item_defidx=4906), my_current_event=None, my_current_event_teams=[], my_current_team=None, my_current_event_stages=[], activity=None, player_level=18, player_cur_xp=327680155, rankings=[Ranking(account_id=1098816904, rank_id=2, wins=39, rank_type_id=7, per_map_rank=[])])]
```