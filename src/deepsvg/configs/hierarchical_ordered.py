from deepsvg.configs.default_icons import ExperimentConfig
from deepsvg.logger import get_logger
from deepsvg.model.config import Hierarchical

LOGGER = get_logger(__name__)


class ModelConfig(Hierarchical):
    def __init__(self):
        super().__init__()

        self.label_condition = False
        self.use_vae = False


class ExperimentConfig(ExperimentConfig):
    def __init__(self, num_gpus=1):
        super().__init__(num_gpus=num_gpus)

        self.model_cfg = ModelConfig()
        self.model_args = self.model_cfg.get_model_args()

        self.filter_category = None

        self.learning_rate = 1e-3 * num_gpus
        self.batch_size = 128 * num_gpus

        self.val_every = 2000
