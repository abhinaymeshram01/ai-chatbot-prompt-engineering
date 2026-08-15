class ConversationMemory:

    def __init__(self, MAX_TURNS=5):
        self.history = []
        self.max_turns = MAX_TURNS
    
    def add_user_message(self, message):
        self.history.append({
            'role':'user',
            'parts':[
                {
                    'text': message
                }
            ]
        })

    def add_assistant_message(self, message):
        self.history.append({
            'role':'model',
            'parts':[
                {
                    'text': message
                }
            ]
        })

    def get_history(self):
        max_messages = self.max_turns * 2
        return self.history[-max_messages:]
    
    def clear(self):
        self.history = []

    def remove_last_message(self):
        if self.history:
            self.history.pop()