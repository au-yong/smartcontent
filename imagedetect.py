from torchvision import models
from torchvision import transforms
from PIL import Image
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

alexnet = models.alexnet(pretrained=True)

class GetImageInfo():
    def __init__(self):
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485,0.456,0.406],
                std=[0.229,0.224,0.225]
            )
        ])

    def info(self,imageUrl):
        img = Image.open(imageUrl)
        img_t = self.transform(img)
        batch_t = torch.unsqueeze(img_t,0)
        alexnet.eval()
        out = alexnet(batch_t)
        with open('data/imagenet_classes.txt') as f:
            classes = [line.strip() for line in f.readlines()]
        _, index = torch.max(out, 1)
        percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
        _, indices = torch.sort(out, descending=True)
        percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
        return classes[index[0]], [classes[idx] for idx in indices[0][:5]]
# [(classes[idx], percentage[idx].item()) for idx in indices[0][:5]]
