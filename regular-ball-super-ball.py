class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
    
    def returning(self):
        return self.ball_type
        
