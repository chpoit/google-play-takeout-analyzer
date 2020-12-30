from loader.config_loader import load_config 
from loader.takeout_loader import load_takeout 


if __name__ == "__main__":
    config = load_config()
    takeout = load_takeout(config["takeout-path"])

    takeout.print()