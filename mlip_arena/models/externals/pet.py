from __future__ import annotations

import yaml
from pathlib import Path

from ase.calculators.calculator import all_changes
from upet.calculator import UPETCalculator

from mlip_arena.models.utils import get_freer_device



with open(Path(__file__).parents[1] / "registry.yaml", encoding="utf-8") as f:
    REGISTRY = yaml.safe_load(f)


class PET_OAM_XL(UPETCalculator):
    def __init__(
        self,
        checkpoint=REGISTRY["PET(OAM)"]["checkpoint"],
        device: str | None = None,
        **kwargs,
    ):
        self.device = device or str(get_freer_device())
        super().__init__(model="pet-oam-xl", version="1.0.0", device=self.device)
    
    
    def calculate(
        self, atoms=None, properties=['energy', 'forces', 'stress'], system_changes=all_changes
    ):
        super().calculate(atoms, properties, system_changes)
