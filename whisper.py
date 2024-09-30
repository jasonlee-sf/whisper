from datasets import load_dataset, DatasetDict

common_voice = DatasetDict()

#common_voice["train"] = load_dataset("mozilla-foundation/common_voice_11_0", "en", split="train+validation", use_auth_token=True)
common_voice["test"] = load_dataset("mozilla-foundation/common_voice_11_0", "ja", split="test")

print(common_voice)
