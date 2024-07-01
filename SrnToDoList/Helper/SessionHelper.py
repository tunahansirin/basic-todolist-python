import uuid

# SessionHelper sınıfı, oturum işlemleri için yardımcı sınıftır.
class SessionHelper:
    def __init__(self):
        self.activeSessions = {}

    # CreateSession metodu, oturum oluşturur ve oturum kimliğini döndürür.
    def CreateSession(self, username):
        sessionId = str(uuid.uuid4())
        self.activeSessions[sessionId] = username
        return sessionId

    # GetSessionById metodu, oturum kimliğine göre oturumu döndürür.
    def GetSessionById(self, sessionId):
        return self.activeSessions.get(sessionId, None)

    # DeleteSession metodu, oturum kimliğine göre oturumu siler.
    def DeleteSession(self, sessionId):
        if sessionId in self.activeSessions:
            del self.activeSessions[sessionId]