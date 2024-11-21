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
