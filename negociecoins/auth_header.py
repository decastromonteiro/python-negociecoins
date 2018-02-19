import base64, hashlib, hmac, random, time,urllib.parse

'''               
@param id ID da API gerada pelo usuário na NegocieCoins.
@param key Chave da API gerada pelo usuário na NegocieCoins.
@param url URL da API da NegocieCoins.
@param method Método utilizado na conexão com a API, pode ser GET, POST ou DELETE.
@param body Corpo de envio da requisição, nos métodos GET e DELETE ele é nulo.
@return AMXHeader Cabeçalho no formato desejado para se autenticar na API da NegocieCoins.         
'''


def amx_authorization_header(id, key, url, method, body):
    encoded_url = urllib.parse.quote_plus(url).lower()
    method = method.upper()
    ##==================Tratando o content=====================================
    m = hashlib.md5()
    m.update(body.encode('utf-8'))
    content = '' if body == None else base64.b64encode(m.digest())
    ##=========================================================================
    timestamp = str(int(time.time()))
    nonce = str(random.randint(0, 100000000))
    data = ''.join([id, method, encoded_url, timestamp, nonce, str(content)]).encode()
    secret = base64.b64decode(key)
    signature = str(base64.b64encode(hmac.new(secret, msg=data, digestmod=hashlib.sha256).digest()))
    ##===================Cabeçalho no formato AMX==============================
    header = 'amx %s' % ':'.join([id, signature, nonce, timestamp])

    return header
