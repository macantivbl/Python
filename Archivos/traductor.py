from translate import Translator
from_lang = 'es'
translator = Translator(to_lang="ja")
try:
    with open('ArchivoTraducir.txt', mode='r') as Mi_archivo:
        texto = Mi_archivo.read()
        translator = translator.translate(texto)
        print(translator)
except FileNotFoundError as e:
    print('verifica tus archivos')


