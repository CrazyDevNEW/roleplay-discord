class Player():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.member = kwargs.get("member")
 
