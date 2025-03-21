import torch
import numpy as np
from PIL import Image
import cv2

class ImageGrayscaleNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),  # ComfyUI handles images as tensors
            },
            "optional": {
                "intensity": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.1
                })
            },
        }

    RETURN_TYPES = ("IMAGE",)  # Output is also an image
    RETURN_NAMES = ("image",)
    FUNCTION = "process"
    CATEGORY = "Image Processing"

    def process(self, image: torch.Tensor, intensity=1.0):
        """
        Convert an image tensor to grayscale.
        """

        # Convert PyTorch tensor to NumPy array (C, H, W) -> (H, W, C)
        image_np = (image[0].cpu().numpy() * 255).astype(np.uint8)
        pil_image = Image.fromarray(image_np)

        print(f"Processing image with intensity: {intensity} # This is just an example")
        
        # Convert to grayscale
        grayscale_image = pil_image.convert("L")

        # Convert back to tensor format expected by ComfyUI
        grayscale_tensor = torch.tensor(np.array(grayscale_image) / 255.0).unsqueeze(0)

        return (grayscale_tensor,)


# Register node in ComfyUI
NODE_CLASS_MAPPINGS = {
    "ImageGrayscaleNode": ImageGrayscaleNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageGrayscaleNode": "Convert to Grayscale"
}

