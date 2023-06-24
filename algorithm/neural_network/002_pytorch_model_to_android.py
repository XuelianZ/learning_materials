# -*- coding: utf-8 -*-
"""
Created on Sat May 13 23:03:22 2023
 pytorch 模型转换为安卓可调用的模型
@author: Admin
"""

import torch
import torchvision
from torch.utils.mobile_optimizer import optimize_for_mobile

model = torchvision.models.mobilenet_v2(pretrained=True)
model.eval()
example = torch.rand(1, 3, 224, 224)
traced_script_module = torch.jit.trace(model, example)
traced_script_module_optimized = optimize_for_mobile(traced_script_module)
traced_script_module_optimized._save_for_lite_interpreter("android_mobilenetv2_model.pt")