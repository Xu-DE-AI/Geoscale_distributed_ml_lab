import numpy as np,torch
from torch import nn
def main():
 import onnxruntime as ort
 m=nn.Sequential(nn.Linear(8,16),nn.ReLU(),nn.Linear(16,2)).eval(); x=torch.randn(4,8); torch.onnx.export(m,x,'model.onnx',input_names=['input'],output_names=['output'],opset_version=17); s=ort.InferenceSession('model.onnx'); print(s.run(['output'],{'input':x.numpy().astype(np.float32)})[0])
if __name__=='__main__': main()
