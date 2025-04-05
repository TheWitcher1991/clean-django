from django.conf import settings

from clean_django.shared.kernel.types import LoggerResource


class Logger:

    def __init__(self):
        pass

    def logger(self, resource_type: LoggerResource = LoggerResource.kernel, **kwargs):
        raise NotImplementedError

    def _log(self, level: str, message: str, resource_type: LoggerResource, **kwargs):
        level = level.upper()

        log = self.logger(resource_type=resource_type)

        if level == "TRACE":
            log.trace(message)
        elif level == "DEBUG":
            log.debug(message)
        elif level == "INFO":
            log.info(message)
        elif level == "WARN":
            log.warn(message)
        elif level == "ERROR":
            log.error(message)
        elif level == "FATAL":
            log.fatal(message)

    def info(self, message, resource_type: LoggerResource, **kwargs):
        self._log("INFO", message, resource_type=resource_type, **kwargs)

    def warning(self, message, resource_type: LoggerResource, **kwargs):
        self._log("WARNING", message, resource_type=resource_type, **kwargs)

    def error(self, message, resource_type: LoggerResource, **kwargs):
        self._log("ERROR", message, resource_type=resource_type, **kwargs)

    def debug(self, message, resource_type: LoggerResource, **kwargs):
        if settings.DEBUG:
            print(f"DEBUG: {message} {kwargs}")
        else:
            self._log("DEBUG", message, resource_type=resource_type, **kwargs)

    def critical(self, message, resource_type: LoggerResource, **kwargs):
        self._log("CRITICAL", message, resource_type=resource_type, **kwargs)
