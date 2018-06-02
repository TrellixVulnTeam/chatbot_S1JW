def import_module(dotted_path):

    import importlib

    module_parts = dotted_path.split('.')
    module_path = '.'.join(module_parts[:-1])
    module = importlib.import_module(module_path)
    return getattr(module, module_parts[-1])


def initialize_class(data, **kwargs):

    if isinstance(data, dict):
        import_path = data.get('import_path')
        data.update(kwargs)
        Class = import_module(import_path)
        return Class(**data)
    else:
        Class = import_module(data)
        return Class(**kwargs)


def validate_adapter_class(validate_class, adapter_class):

    from .adapters import Adapter

    if isinstance(validate_class, dict):
        if 'import_path' not in validate_class:
            raise Adapter.InvalidAdapterTypeException(
                'The dictionary {} must contain a value for "import_path"'.format(
                    str(validate_class)
                )
            )
        validate_class = validate_class.get('import_path')

    if not issubclass(import_module(validate_class), adapter_class):
        raise Adapter.InvalidAdapterTypeException(
            '{} must be a subclass of {}'.format(
                validate_class,
                adapter_class.__name__
            )
        )


def input_function():

    import sys
    
    if sys.version_info[0] < 3:
        user_input = str(raw_input())
        if user_input:
            user_input = user_input.decode('utf-8')
    else:
        user_input = input()
    return user_input


def nltk_download_corpus(resource_path):

    from nltk.data import find
    from nltk import download
    from os.path import split, sep
    from zipfile import BadZipfile

    _, corpus_name = split(resource_path)

    if not resource_path.endswith(sep):
        resource_path = resource_path + sep
    downloaded = False
    try:
        find(resource_path)
    except LookupError:
        download(corpus_name)
        downloaded = True
    except BadZipfile:
        raise BadZipfile(
            'The NLTK corpus file being opened is not a zipfile, '
            'or it has been corrupted and needs to be manually deleted.'
        )
    return downloaded

def remove_stopwords(tokens, language):

    from nltk.corpus import stopwords

    stop_words = stopwords.words(language)
    tokens = set(tokens) - set(stop_words)
    return tokens

def get_response_time(chatbot):

    import time

    start_time = time.time()
    chatbot.get_response('Hello')
    return time.time() - start_time

def print_progress_bar(description, iteration_counter, total_items, progress_bar_length=40):

    import sys

    percent = float(iteration_counter) / total_items
    hashes = '#' * int(round(percent * progress_bar_length))
    spaces = ' ' * (progress_bar_length - len(hashes))
    sys.stdout.write("\r{:20s}: [{}] {}%".format(description, hashes + spaces, int(round(percent * 100))))
    if total_items == iteration_counter:
        print("\r")
    sys.stdout.flush()