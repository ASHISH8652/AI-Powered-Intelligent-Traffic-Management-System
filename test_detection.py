import os
import cv2
from pathlib import Path
from traffic_ai.detection import TrafficInference
from traffic_ai.config.path import ROOT, DATASETS, OUTPUT

# 1. Resolve image path dynamically to ensure an existing image is used
image_dir = DATASETS / "raw" / "DETRAC_Upload" / "images" / "val"

# Target sample or fall back to any available .jpg in val directory
image_path = image_dir / "MVI_39031_img00319.jpg"

if not image_path.exists():
    # Fallback to first available JPG image in val directory
    jpg_files = list(image_dir.glob("*.jpg"))
    if jpg_files:
        image_path = jpg_files[0]
    else:
        raise FileNotFoundError(f"No image files found in directory:\n{image_dir}")

print("=" * 60)
print(f"Testing Vehicle Detection on: {image_path.name}")
print("=" * 60)

# 2. Create inference engine
engine = TrafficInference()

# 3. Detect vehicles
output = engine.detect_image(str(image_path))

if output is None:
    raise ValueError("Detection failed: Engine returned None")

# 4. Save output image to disk
os.makedirs(OUTPUT, exist_ok=True)
save_path = OUTPUT / "test_detection_result.jpg"
cv2.imwrite(str(save_path), output)
print(f"✅ Vehicle Detection Successful!")
print(f"📸 Result saved to: [test_detection_result.jpg](file:///{save_path.as_posix()})")

# 5. Display image (if desktop GUI environment is available)
try:
    cv2.imshow("Vehicle Detection", output)
    print("Press any key in the window to exit...")
    cv2.waitKey(1)
    cv2.destroyAllWindows()
except Exception as e:
    print(f"Note: Display window skipped ({e}). Image saved to outputs.")