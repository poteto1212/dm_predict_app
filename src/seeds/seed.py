from datasets.users.users_seed import User_seed
from datasets.admins.admins_seed import Admin_seed

User_seed.insert_test_user()
Admin_seed.insert_test_admin(user_id=1)