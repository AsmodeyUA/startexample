import re

class rrrr:
	def _bound(self, name, default=0):
		dict1 = self._config
		return dict1.get("value",
						 dict1.get(name,
								   default))

d = rrrr()
d._config = {"test":8, "value":5}
print(d._bound("test"))

