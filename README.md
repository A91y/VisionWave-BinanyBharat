
# VisionWave-BinanyBharat

## Streamlet Drowsiness Detection Model

Welcome to the Streamlet Drowsiness Detection Model! This model is designed to detect drowsiness using the Ultralytics YOLOv5 architecture and is deployed with Streamlet. Upon detecting drowsiness, it triggers an alarm to alert the user.

### Getting Started

#### Prerequisites

Before using the model, ensure you have the following dependencies installed:

- Python 3.6 or higher
- PyTorch (Installation guide: [PyTorch](https://pytorch.org/get-started/locally/))
- Ultralytics YOLOv5 (Repository: [YOLOv5](https://github.com/ultralytics/yolov5))
- Streamlet (Installation guide: [Streamlit Installation](#))

Clone the repository:

```bash
git clone https://github.com/your-username/streamlet-drowsiness-detection.git
cd streamlet-drowsiness-detection
```

Download the COCO classes file:

```bash
wget https://gist.github.com/AruniRC/7b3d50a7655319682b847c0ddcd8c2e8/raw/865c9de1b7e049233221ee2bc0ea7c692c0cbe31/coco_classes.txt
```

Download LabelImg for annotating your custom dataset:

```bash
git clone https://github.com/tzutalin/labelImg.git
cd labelImg
make qt5py3
```

#### Usage

- **Train the Model:**

  Modify the configuration file (yolov5s.yaml) according to your dataset and training preferences. Train the model using:

  ```bash
  python train.py --img-size 640 --batch-size 16 --epochs 50 --data your_data.yaml
  ```

- **Deploy with Streamlet:**

  Run the Streamlet app:

  ```bash
  streamlit run app.py
  ```

  Open your browser and go to http://localhost:8501 to interact with the Drowsiness Detection Model.

### Features

- Custom Dataset: You can use your own dataset for training the model. Follow the guidelines provided in the Ultralytics YOLOv5 repository.

- Alarm System: Upon detecting drowsiness, the model triggers an alarm to alert the user.

### Contributing

If you encounter issues or have suggestions for improvement, please open an issue or submit a pull request.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

This model is built on the YOLOv5 architecture developed by Ultralytics ([Ultralytics GitHub](https://github.com/ultralytics/yolov5)).

Thank you for using the Streamlet Drowsiness Detection Model! If you have any questions or feedback, feel free to reach out.
```
