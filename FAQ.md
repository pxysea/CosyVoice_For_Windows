## ModuleNotFoundError: No module named 'matcha'

Matcha-TTS is a third_party module. Please check `third_party` directory. If there is no `Matcha-TTS`, execute `git submodule update --init --recursive`.

run `export PYTHONPATH=third_party/Matcha-TTS` if you want to use `from cosyvoice.cli.cosyvoice import CosyVoice` in python script.

## cannot find resource.zip or cannot unzip resource.zip

Please make sure you have git-lfs installed. Execute

```sh
git clone https://www.modelscope.cn/iic/CosyVoice-ttsfrd.git pretrained_models/CosyVoice-ttsfrd
cd pretrained_models/CosyVoice-ttsfrd/
unzip resource.zip -d .
pip install ttsfrd-0.3.6-cp38-cp38-linux_x86_64.whl
```

## 运行 python webui.py 时出现错误

**运行：** python examples\web\webui.py
**报错：** AttributeError: __pydantic_core_schema__

### 解决办法：

**降级 fastapi 版本**
pip uninstall fastapi
pip install fastapi==0.112.4

### torch.OutOfMemoryError 问题

错误信息：

```
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 2.00 GiB of which 1.06 MiB is free. Of the allocated memory 766.53 MiB is allocated by PyTorch, and 51.47 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
```

**分析：** 可能是GPU显存过低，显卡太老

禁用Cuda使用GPU，只使用CPU运算，速度会变慢

禁用CUDA使用GPU 方法

在环境变量中运行：

```shell
set CUDA_VISIBLE_DEVICES=-1
```

python中使用：

```python
os.environ['CUDA_VISIBLE_DEVICES'] = -1
```

**查看是否禁用：**

```python
import torch
print(torch.cuda.is_available())
```

## **pynini 安装**
conda install -c conda-forge pynini==2.1.5

## FutureWarning: You are using torch.load with weights_only=False
**警告信息**
```
\cosyvoice\cli\model.py:57 FutureWarning: You are using torch.load with weights_only=False (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for weights_only will be flipped to True. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via torch.serialization.add_safe_globals. We recommend you start setting weights_only=True for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
```
**中文信息**
```
警告（FutureWarning）：您正在使用 torch.load，且设置了 weights_only=False（当前的默认值），这会隐式地使用默认的 pickle 模块。需要注意的是，pickle 数据可能被构造为恶意形式，从而在反序列化时执行任意代码（详细信息参见：https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models）。在未来的版本中，`weights_only` 的默认值将更改为 True。此更改将限制反序列化过程中可能被执行的功能，除非用户通过 torch.serialization.add_safe_globals 显式允许，否则将不再允许加载任意对象。

我们建议在您无法完全控制加载文件时，将 weights_only 设置为 True。如果遇到与此实验功能相关的问题，请在 GitHub 上提交 issue。
```
## lora.py:393: FutureWarning: `LoRACompatibleLinear` is deprecated
```
Lib\site-packages\diffusers\models\lora.py:393: FutureWarning: `LoRACompatibleLinear` is deprecated and will be removed in version 1.0.0. Use of `LoRACompatibleLinear` is deprecated. Please switch to PEFT backend by installing PEFT: `pip install peft`.
  deprecate("LoRACompatibleLinear", "1.0.0", deprecation_message)
```

**解决办法：**
修改文件：third_party\Matcha-TTS\matcha\models\components\transformer.py

```
        #第一处
        from diffusers.models.lora import LoRACompatibleLinear

        ... 第二处
        # self.proj = LoRACompatibleLinear(in_features, out_features) # fix by siyver
        self.proj = nn.Linear

        ...  第三处
        # project out
        # self.net.append(LoRACompatibleLinear(inner_dim, dim_out))
        self.net.append(nn.Linear(inner_dim, dim_out)) #fix by sivyer
```

## generator object CosyVoice.inference_zero_shot at...
```
<generator object CosyVoice.inference_zero_shot at 0x000001C4A9EE6D40>
!!! Exception during processing !!! 'generator' object is not subscriptable
```
