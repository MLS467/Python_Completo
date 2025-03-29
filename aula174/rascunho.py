import os
import shutil

HOME = os.path.expanduser('~')
CAMINHO_ORIGINAL = os.path.join(HOME, 'Desktop', 'TESTE')
NOVA_PASTA = os.path.join(HOME, 'Desktop', 'NOVA_PASTA2')

# os.makedirs(NOVA_PASTA, exist_ok=True)
# os.unlink(NOVA_PASTA)
# shutil.rmtree(NOVA_PASTA, ignore_errors=True)


# shutil.copytree(CAMINHO_ORIGINAL, NOVA_PASTA)

shutil.move(NOVA_PASTA+'BATATA BATATA', NOVA_PASTA + ' BATATA')
