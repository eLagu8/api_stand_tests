import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)
#
# def get_logs():
#     return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)
#
# response = get_logs()
# print(response.status_code)
# #print(response.headers)
#
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH,)

# response = get_users_table()
# print(response.status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
# print(response.status_code)
# print(response.json())

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,headers=data.headers)
response = post_products_kits(data.product_ids)
# print(response.status_code)
# print(response.json())