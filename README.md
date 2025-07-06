# Automated-Grocery-Billing-System-Using-Computer-Vision-and-Deep-Learning-Techniques
This project presents a computer vision-based billing system that detects multiple grocery items from an image using **YOLOv8**, counts their occurrences, and automatically generates a bill. The system is trained on the **Freiburg Groceries Dataset** and is deployed using a **Streamlit** interface for real-time usability.

---

## Project Description

Manual grocery billing using barcode scanners is time-consuming and requires human intervention. This project uses object detection to automate item recognition and billing from an uploaded image. The system detects grocery products, calculates quantities, maps them to prices, and generates a final bill using Python and Deep Learning techniques. The project demonstrates practical use of real-time computer vision in a retail setting.

---

## Files in the Repository

| File Name                                                   | Description |
|--------------------------------------------------------------|-------------|
| `EDA_freiburg.ipynb`                                        | Performs exploratory data analysis (EDA) on the Freiburg Groceries Dataset. Includes visualizations of class distribution and object count per image. |
| `Model Training.ipynb`                                      | Trains the YOLOv8 model on 25 grocery categories from the Freiburg dataset. Prepares data, handles formatting, and runs training for 50 epochs. |
| `Model Predictions.ipynb`                                           | Loads the trained YOLOv8 model, performs object detection on input images, and integrates item-wise billing logic using predefined prices. |
| `Automated_billing_system.py`                                | Streamlit application that allows users to upload grocery item images, performs detection, and displays the final bill with item names, quantities, and prices. |
| `Automated Grocery Billing System using Computer Vision and Deep Learning Techniques.pptx` | Final presentation outlining the project methodology, dataset, model performance, billing workflow, and user interface snapshots. |

---

## Dataset

- **Name**: Freiburg Groceries Dataset  
- **Source**: [Freiburg Groceries Dataset GitHub](https://github.com/PhilJd/freiburg_groceries_dataset)  
- **Total Images**: 5,000  
- **Categories**: 25 grocery item types (e.g., milk, cereal, juice, chips, beans)  
- **Format**: Images with corresponding YOLO-formatted annotation files (bounding boxes and class labels)

---

## Exploratory Data Analysis (EDA)

- **Class Distribution**: Visualized using bar plots
  - Common classes: milk, juice, coffee
  - Rare classes: cake, soda, honey
- **Object Count per Image**:
  - Most images contain 1–3 objects
  - Some images have multiple objects, indicating suitable complexity for object detection

---

## Model Summary

- **Model**: YOLOv8 (You Only Look Once, Version 8)
- **Framework**: Ultralytics YOLOv8
- **Training**: 50 epochs on Freiburg Groceries Dataset
- **Loss Achieved**: 0.01
- **Performance**:
  - High accuracy even under occlusion and overlapping
  - Outperforms prior implementations (which achieved ~70% accuracy)

---

## Billing Logic

- YOLOv8 model detects and classifies grocery items in the image
- Each class label is mapped to a predefined unit price
- Quantity is determined by the number of instances per class
- Total price = quantity × unit price
- A final bill is generated showing:
  - Item name
  - Quantity
  - Unit price
  - Total per item and grand total

---

## Streamlit Interface

- Upload an image with grocery items
- System detects and annotates items with bounding boxes
- Bill is displayed in a structured table format
  - Includes item name, quantity, price per item, and total cost
