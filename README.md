# practicum
Psychosis in teens via gesture analysis
**Visual Features**
For the following visual features, calculation is done for every frame, only write the values into csv when the time in seconds is an integer. 
Main package used: mediapipe
Mediapipe works in two steps, identify the pre-defined landmarks and track the landmark movement. 
All the value returned by mediapipe is normalized. 
For example, in the case of hand tracking, once the hand is detected in the frame, and the landmarks are localized, MediaPipe returns the landmarks as normalized coordinates relative to the size of the detected hand. In this case, the value is relatively robust even when the camera angle changed from video to video. 
Let’s say the hand move 1 cm in the real world, once video captured the movement 1m forward of the hand, another video captured the video 10m forward of the hand, mediapipe is able to give similar values of the movement in these two videos. 

Time_in_seconds: float
It represents the time in seconds corresponding to the current frame number divided by the frames per second (fps)

Frame: int 
It represents the current frame number being processed.

Total_movement_per_second: float 
It measures the cumulative total movement detected in the current frame compared to previous frame within 1 second. The keypoints tracked are LEFT_WRIST, RIGHT_WRIST, LEFT_ANKLE, RIGHT_ANKLE

Pose_openness: float
It calculates the openness of a pose based on the landmarks of the holistic model. The landmark used here are LEFT_SHOULDER, RIGHT_SHOULDER, LEFT_HIP, RIGHT_HIP, LEFT_WRIST, RIGHT_WRIST. The landmark coordinate value are multiplied by image_w and image_h is to scale the coordinates from normalized values (ranging from 0 to 1) to the corresponding pixel coordinates in the image. / openness of main body

Leaning: str [‘Backward’, ‘Forward’]
It determines the leaning direction of the person based on the position of the nose relative to the hips.

Head_horizontal: str [‘Left’, ‘Right’, ‘Still’]
Calculation: It determines the horizontal direction of the head movement based on the change in the position of the nose between consecutive frames.

Head_vertical: str [‘Up’, ‘Down’, ‘Still’]
It determines the vertical direction of the head movement based on the change in the position of the nose between consecutive frames.

left_arm_angle & right_arm_angle: float
It determines the angle of the left arm and right arm based on the landmarks of the holistic model. For calculating the angle, WRIST-ELBOW-SHOULDER coordinates for left and right arms are used.

left_arm_v_movement & right_arm_v_movement: str [‘Up’, ‘Down’]
It determines vertical movement(‘UP’ or ‘DOWN’) of left and right arms based on the left_arm_angle and right_arm_angle.

left_arm_h_movement & right_arm_h_movement: str [‘Forward’, ‘Calculating’]
It determines horizontal movement(‘FORWARD’) of left and right arms based on the position of WRIST relative to the ELBOW.

left_hand_orientation & right_hand_orientation: str [‘Right’, ‘Left’, ‘Up’, ‘Down’]
It determines the orientation of the hand(‘Right’, ‘Left’, ‘Up’, ‘Down’) based on the landmarks in the left and right hands. Landmarks used are WRIST and MIDDLE_FINGER_MCP and the calculation is done by determining the slope of the line connecting these landmarks.

left_hand_state & right_hand_state: str [‘Closed’, ‘Open’]
It determines whether a hand is ‘CLOSED’ or ‘OPEN’ based on the euclidean distance between THUMB_TIP and INDEX_TIP landmarks. 

**Acoustic Features**
The code process the audio of a video in 10-seconds intervals. 
Why 10 seconds? 
Longer audio segments provide more context for speech recognition algorithms, allowing them to analyze a larger chunk of audio and potentially improve accuracy.

Avg_pitch: float
It calculates the average pitch of the 10 seconds audio segment using the piptrack function from the librosa library.

Avg_intensity: float
It calculates the average intensity of the 10 seconds audio segment using the piptrack function from the librosa library.

Transcription: string 
It transcribes the 10 seconds audio segment using the Google Speech Recognition service through the recognize_google method from the speech_recognition library.

**Cross-modality Features**
Contradiction between expected gestures and actual gestures
This code aims to identify and output the rows where there are contradictions between the expected gestures based on words in the transcript and the actual recorded gestures. The contradictions are detected by comparing the values in the dataframe with the expected values specified in the word_gesture_map dictionary.
The code will check for exact match of the expected gesture’s name in the transcript. This isn’t perfect, for example, when a person say ‘right now’, the code will also search for gestures associated with ‘RIGHT’

Steps undertook:
Split the transcript into individual words and store them in the words variable.
Iterate over each word in the words list.
If the word is present in the word_gesture_map dictionary:
Get the expected gestures associated with the word.
Iterate over each gesture and expected value pair.
Compare the expected value with the actual value in the row for the corresponding gesture.
If a contradiction is found (the values don't match), print the word, the actual value, and the expected value, and return the row.
