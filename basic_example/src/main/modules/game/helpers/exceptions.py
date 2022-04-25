
class Error(Exception):
	pass

class PlayerError(Error):
	pass

class TeamError(Error):
	pass

class GameError(Error):
	pass


class NotFound(Exception):
	pass

class PlayerNotFound(NotFound):
	pass

class TeamNotFound(NotFound):
	pass

class GameNotFound(NotFound):
	pass