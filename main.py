import argparse
from ultralytics import YOLO


def main():
    # Create parser
    parser = argparse.ArgumentParser(description="Run YOLO model with command line arguments")

    # Add arguments
    parser.add_argument('--prompt_list', nargs='+', help='List of prompts', required=True)
    parser.add_argument('--source', type=str, help='Source file', required=True)
    parser.add_argument('--conf', type=float, help='Confidence threshold', default=0.07)

    # Parse arguments
    args = parser.parse_args()

    # Load model
    model = YOLO('yolov8l-world.pt')

    # Set classes based on prompt list
    model.set_classes(args.prompt_list)

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
