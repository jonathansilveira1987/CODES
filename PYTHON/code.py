x = int(input('\nDigite um número inteiro: '))
x -= - 1
print(f'\n\033[31m{x}\033[m')

x = x == 0
(x + 1)
x : x + 1
print(f'\n\033[31m{x}\033[m')

import uuid

print('''
UUID = Um namespace de URN de identificador universalmente exclusivo.
Status deste memorando.
Este documento especifica um Protocolo de Rastreamento de Padrões da Internet.
''')

n = uuid.getnode()
print(f'Módulo UUID: \033[32m{n}\033[m')

user_id_1 = uuid.uuid1()
print(f'\nUUID 1: \033[33m{user_id_1}\033[m')

user_id_4 = uuid.uuid4()
print(f'\nUUID 4: \033[32m{user_id_4}\033[m')

dns = uuid.NAMESPACE_DNS
print(f'\nDNS: \033[33m{dns}\033[m')

namespace = uuid.NAMESPACE_URL
print(f'\nNAMESPACE: \033[32m{namespace}\033[m')

oid = uuid.NAMESPACE_OID
print(f'\nOID: \033[33m{oid}\033[m')

x500 = uuid.NAMESPACE_X500
print(f'\nX500: \033[32m{x500}\033[m')

ncs = uuid.RESERVED_NCS
print(f'\nRESERVED NCS: \033[33m{ncs}\033[m')

rfc = uuid.RFC_4122
print(f'\nRFC: \033[32m{rfc}\033[m')

m = uuid.RESERVED_MICROSOFT
print(f'\nRESERVED MICROSOFT: \033[33m{m}\033[m')

future = uuid.RESERVED_FUTURE
print(f'\nRESERVED FUTURE: \033[32m{future}\033[m\n')






























