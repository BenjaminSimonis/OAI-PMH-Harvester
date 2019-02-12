import platform


class AppConstants:

    def __init__(self):
        if platform.system() is "Windows":
            self._SLASH = "\\"
        else:
            self._SLASH = "/"

        # Edit the next two lines for your system!
        self._DOWNLOAD_PATH = ""
        self._OAI_URL = ""

    def SLASH(self):
        return self._SLASH

    def DOWNLOADPATH(self):
        return self._DOWNLOAD_PATH

    def OAI_URL(self):
        return self._OAI_URL


def get_constants():
    return AppConstants()
