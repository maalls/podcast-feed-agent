from podcastfy.client import generate_podcast

custom_config = {
    "output_language": 'French'
    
}

audio_file = generate_podcast(urls=[
    "https://dwh.lequipe.fr/api/edito/rss?path=/Cyclisme/",
],
    llm_model_name="gpt-4o-mini",
    api_key_label="OPENAI_API_KEY",
    conversation_config=custom_config,)
