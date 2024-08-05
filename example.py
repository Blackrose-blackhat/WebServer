from main import SlowAPI


slow = SlowAPI()

@slow.get('/users')
def get_users(req,res):
    res.send('musharaf','parwez')