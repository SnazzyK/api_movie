from faker import Faker

#
#
# from utils.api_utils import ApiUtils
#
# fake = Faker()
#
# AUTH_URL = "https://auth.dev-cinescope.store"
# MOVIE_URL = "https://api.dev-cinescope.store"
#
#
# DELETE_ENDPOINT = "/user/"
# CREATE_MOVIE_ENDPOINT = "/movies"
#
# email_admin = "test-admin@mail.com"
# password_admin = "KcLMmxkJMjBD1"
# password_user = fake.password()
#
# user_auth_api_utils = ApiUtils(AUTH_URL)
# auth_helper = AuthorizationHelper(user_auth_api_utils)
# response = auth_helper.post_register(json={"email":fake.email(),
#                                            "fullName":f"{fake.first_name()} {fake.last_name()}",
#                                            "password":password_user,
#                                            "passwordRepeat":password_user})
# #
#
#
#
#
#
# # response = user_auth_api_utils.post(REGISTER_ENDPOINT, json={"email": fake.email(),
# #                                                              "fullName": f"{fake.first_name()} {fake.last_name()}",
# #                                                              "password": password_user,
# #                                                              "passwordRepeat": password_user})
# #
# # print(response.status_code)
# # email_user = response.json()["email"]
# #
# # response_login_user = user_auth_api_utils.post(LOGIN_ENDPOINT, json={"email": email_user,
# #                                                                      "password": password_user})
# #
# # print(response_login_user.status_code)
# # print(response_login_user.json())
# # id_user = response_login_user.json()["user"]["id"]
# # access_token = response_login_user.json()["accessToken"]
# #
# #
# # admin_auth_api_utils = ApiUtils(AUTH_URL)
# #
# # response_login_admin = admin_auth_api_utils.post(LOGIN_ENDPOINT, json={"email": email_admin,
# #                                                                        "password": password_admin})
# # access_token_admin = response_login_admin.json()["accessToken"]
# #
# #
# # admin_movie_api_utils = ApiUtils(MOVIE_URL, headers={"Authorization": f"Bearer {access_token_admin}"})
# # id_admin = response_login_admin.json()["user"]["id"]
# #
# #
# # response_movie_admin = admin_movie_api_utils.post(CREATE_MOVIE_ENDPOINT, json={"name": fake.name(),
# #                                                                                "price": random.randint(1, 100),
# #                                                                                "description": fake.text(),
# #                                                                                "location": random.choice(
# #                                                                                    ["SPB", "MSK"]),
# #                                                                                "published": True,
# #                                                                                "genreId": 1})
#
#
