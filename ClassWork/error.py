class Error(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built!"
    
def check_material(amount_material, limit_value):
    if amount_material > limit_value:
        return "nought material"
    else: 
        raise Error(amount_material)
        
matterials = 123
check_material(matterials, 300)