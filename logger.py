import logging

def setup_logger():
    logger = logging.getLogger("main")
    logger.setLevel(logging.DEBUG)

    # Создаем консольный обработчик
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    #Задаем формат логов
    formatter = logging.Formatter("%(acstime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)

    # Добавляем обработчик к люггеру
    logger.addHandler(ch)

    return logger

logger = setup_logger()


