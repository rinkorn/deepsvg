from deepsvg.configs.default_icons import ExperimentConfig


class ExperimentConfig(ExperimentConfig):
    def __init__(self, num_gpus=1):
        super().__init__(num_gpus=num_gpus)

        # Dataset
        self.data_dir = "./dataset/fonts_tensor/"
        self.meta_filepath = "./dataset/fonts_meta.csv"
