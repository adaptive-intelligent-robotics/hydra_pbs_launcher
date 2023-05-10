# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from hydra.core.config_store import ConfigStore


@dataclass
class BaseQueueConf:
    """Configuration shared by all executors"""

    submitit_folder: str = "${hydra.sweep.dir}/.submitit/%j"

    # maximum time for the job in minutes
    timeout_min: int = 60
    # number of cpus to use for each task
    cpus_per_task: Optional[int] = None
    # number of gpus to use on each node
    gpus_per_node: Optional[int] = None
    # number of tasks to spawn on each node
    tasks_per_node: int = 1
    # memory to reserve for the job on each node (in GB)
    mem_gb: Optional[int] = None
    # number of nodes to use for the job
    nodes: int = 1
    # name of the job
    name: str = "${hydra.job.name}"
    # redirect stderr to stdout
    stderr_to_stdout: bool = False

@dataclass
class LocalQueueConf(BaseQueueConf):
    _target_: str = (
        "hydra_plugins.hydra_pbs_launcher.submitit_launcher.LocalLauncher"
    )


@dataclass
class PbsQueueConf:
    _target_: str = (
        "hydra_plugins.hydra_pbs_launcher.submitit_launcher.PbsLauncher"
    )
    submitit_folder: str = "${hydra.sweep.dir}/.submitit/%j"

    # maximum time for the job in minutes
    walltime: str = "00:20:00"
    # number of cpus to use for each task
    ncpus: Optional[int] = None
    # number of gpus to use on each node
    ngpus: Optional[int] = None
    # memory to reserve for the job on each node (in GB)
    mem_gb: Optional[int] = None
    # number of nodes to use for the job
    nodes: Optional[int] = None
    # name of the job
    name: str = "${hydra.job.name}"
    # number of replications
    replications: Optional[int] = None


    
# finally, register three different choices:
ConfigStore.instance().store(
    group="hydra/launcher",
    name="submitit_local",
    node=LocalQueueConf(),
    provider="submitit_launcher",
)

ConfigStore.instance().store(
    group="hydra/launcher",
    name="submitit_pbs",
    node=PbsQueueConf(),
    provider="submitit_launcher",
)
