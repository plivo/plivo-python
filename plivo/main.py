import plivo

client = plivo.RestClient(auth_id="MADCHANDRESH02TANK06", auth_token="OTljNmVmOGVkNGZhNjJlOWIyMWM0ZDI0ZjQwZDdk")

call_params = {
    'role': "Agent",
    'start_mpc_on_enter': True,
    'from_': "+14156667777", # Caller ID for the outbound call
    'to_': "+917708772011", # The destination phone number or endpoint username of the participant that has to be added.
    'start_recording_audio': "http://plivobin.non-prod.plivops.com/api/v1/Vinay_Recording_start.xml",
    'start_recording_audio_method' : "GET",
    'stop_recording_audio' : "http://plivobin.non-prod.plivops.com/api/v1/Vinay_Recording_stop.xml",
    'stop_recording_audio_method' : "GET"
}
#response = client.multi_party_calls.add_participant(friendly_name="MyMPC", **call_params)
#response = client.multi_party_calls.start_play_audio(participant_id=979,friendly_name="MyMPC", url="https://s3.amazonaws.com/plivocloud/music.mp3")
response = client.multi_party_calls.stop_play_audio(participant_id=979,friendly_name="MyMPC")

print(response)