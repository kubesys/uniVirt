

class BadRequest(Exception):
    def __init__(self, message):
        self.reason = 400
        self.message = message

class Forbidden(Exception):
    def __init__(self, message):
        self.reason = 403
        self.message = message
        
class NotFound(Exception):
    def __init__(self, message):
        self.reason = 404
        self.message = message
        
class InternalServerError(Exception):
    def __init__(self, message):
        self.reason = 500
        self.message = message
        
class ConditionException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

class ExecuteException(Exception):
    def __init__(self, reason, message):
        self.reason = reason
        self.message = message