import argparse
from ultralytics import YOLO


def main():
    # Create parser
    parser = argparse.ArgumentParser(description="Run YOLO world with command line arguments")

    # Add arguments
    parser.add_argument('--model', type=str, help='Model name', default='yolov8l-world.pt')
    parser.add_argument('--prompt_list', type=str, help='Comma-separated list of prompts', required=True)
    parser.add_argument('--source', type=str, help='Source file', required=True)
    parser.add_argument('--conf', type=float, help='Confidence threshold', default=0.07)

    # Parse arguments
    args = parser.parse_args()

    # Split the prompt_list string into a list by commas
    prompt_list = [item.strip() for item in args.prompt_list.split(',')]

    # Load model
    model = YOLO(args.model)

    # Set classes based on prompt list
    model.set_classes(prompt_list)

    # Predict
    model.predict(
        source=args.source,
        show=True,
        save=True,
        conf=args.conf,
        show_conf=False,
        agnostic_nms=True
    )


if __name__ == "__main__":
    main()
