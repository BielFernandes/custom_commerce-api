class ApplicationController:
    def __init__(self, current_user):
        self.current_user = current_user
        
    @staticmethod
    def get_current_user():
        print('opa')
        return 'user'
