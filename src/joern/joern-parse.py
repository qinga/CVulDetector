from argparse import ArgumentParser
from os import system
from os.path import join
from typing import cast
from omegaconf import OmegaConf, DictConfig


def configure_arg_parser() -> ArgumentParser:
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-c",
                            "--config",
                            help="Path to YAML configuration file",
                            default="configs/dwk.yaml",
                            type=str)
    return arg_parser


if __name__ == "__main__":
    __arg_parser = configure_arg_parser()
    __args = __arg_parser.parse_args()
    config = cast(DictConfig, OmegaConf.load(__args.config))
    joern = config.joern_path
    root = join(config.data_folder, config.dataset.name)
    source_path = join(root, "source-code")
    out_path = join(root, "csv")
    # joern/joern-parse data\\CWE119\\csv data\\CWE119\\source-code
    # str = f"{joern} {out_path} {source_path}"
    system(f"{joern} {out_path} {source_path}")

    # import pickle
    # f_list = [[1, 2, 'yes'], [1, 3, 'no']]
    #
    # fw = open('G:\\Grade2Master\\VulProjects\\DeepWukong-master\\data\\CWE119\\XFG\\6\\ptr\\a.xfg.pkl', 'wb')
    # pickle.dump(f_list, fw, -1)
    # fw.close()

    # fr = open('G:\\Grade2Master\\VulProjects\\DeepWukong-master\\data\\CWE119\\XFG\\6\\call\\10.xfg.pkl', 'rb')
    # data = pickle.load(fr)
    # print(data)
    # fr.close()
    # import networkx as nx
    # xfg = nx.read_gpickle('G:\\Grade2Master\\VulProjects\\DeepWukong-master\\data\\CWE119\\XFG\\6\\call\\11.xfg.pkl')
    # print(xfg)
