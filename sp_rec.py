from faster_whisper import WhisperModel

def transcriber(audio):
    ## Bebas set model_id ke large-v3 (kalau pc lu kuat), medium, base, atau tiny.
    model_id = 'small'
    save_dir = f'model-{model_id}'

    model = WhisperModel(
        model_id,

        ## Ganti ke device="cuda" dan compute_type="float16" (kalau punya gpu dan mau cepet).
        device="cpu",
        compute_type="int8",
        download_root=save_dir,

        ## Uncomment kode dibawah kalo model udh di download.
        # local_files_only=True
    )

    segment, _ = model.transcribe(
        audio=audio,
        beam_size=5
    )
    for seg in segment:
        yield seg.text