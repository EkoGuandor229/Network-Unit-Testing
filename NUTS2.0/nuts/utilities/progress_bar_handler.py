from colorama import Fore
from tqdm import tqdm


class ProgressBarHandler:

    def __init__(self):
        self.pbar = None

    def initiate_progress_bar(self, bar_size, description):
        self.pbar = tqdm(total=bar_size,
                         bar_format="%s {l_bar}{bar}{r_bar} %s" % (Fore.CYAN, Fore.RESET),
                         ncols=100)
        self.pbar.set_description_str(description)

    def update_progress_bar(self, progress):
        self.pbar.update(progress)

    def clear_progress_bar(self):
        self.pbar.close()
