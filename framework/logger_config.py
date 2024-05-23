import logging
import colorlog


def setup_logger(logger_name):
    """
        Создает и настраивает логгер с указанным именем для логирования сообщений с различными уровнями важности.

        :param logger_name: Имя логгера.
    """

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # Задаём цвет для логирования
    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        log_colors={
            'DEBUG': 'cyan',  # Отладка: голубой цвет
            'INFO': 'green',  # Информация: зеленый цвет
            'WARNING': 'yellow',  # Предупреждение: желтый цвет
            'ERROR': 'red',  # Ошибка: красный цвет
            'CRITICAL': 'red,bg_white',  # Критическая ошибка: красный текст на белом фоне
        }
    )

    # Добавляем обработчик с цветным
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
