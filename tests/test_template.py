# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest

#with pytest.raises(Exception):
#	player.selectHandAction(0,allowedActions)

#monkeypatch.setattr(builtins,"input",lambda _: "p")
