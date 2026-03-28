import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel


model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_frame_embedding(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model.get_image_features(**inputs)

    # --- FIX START ---
    # Check if 'outputs' is a special object or a direct tensor
    if hasattr(outputs, "pooler_output"):
        emb = outputs.pooler_output
    elif hasattr(outputs, "last_hidden_state"):
        emb = outputs.last_hidden_state
    else:
        emb = outputs
    # --- FIX END ---

    # Now you can safely call .norm() on the tensor
    emb = emb / emb.norm(dim=-1, keepdim=True)
    print("USING CORRECT EMBEDDING SERVICE")

    #return emb[0].cpu().numpy()
    return emb.cpu().numpy() 
