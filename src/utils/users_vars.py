user_vars = {
    "yo": "salut"
}

def is_user_var(var_name):
    return var_name in user_vars

def get_users_vars(var_name):
    return str(user_vars[var_name])

