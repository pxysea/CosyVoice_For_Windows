from gradio_client import Client, file

client = Client("http://localhost:8000/")
result = client.predict(
		tts_text="我是通义实验室语音团队全新推出的生成式语音大模型，提供舒适自然的语音合成能力。",
		mode_checkbox_group="预训练音色",
		sft_dropdown="中文男",
		prompt_text="",
		prompt_wav_upload=None,
		prompt_wav_record=None,
		instruct_text="",
		seed=0,
		stream="true",
		speed=1,
		new_dropdown="GreatSpx",
		api_name="/generate_audio"
)
print(result)