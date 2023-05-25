# practicum
Psychosis in teens via gesture analysis

## Visual Features 
1. **Time_in_seconds**: float
It represents the time in seconds corresponding to the current frame number divided by the frames per second (fps)

2. **Frame**: int 
It represents the current frame number being processed.

3. **Total_movement_per_second**: float 
It measures the cumulative total movement detected in the current frame compared to previous frame within 1 second. The keypoints tracked are LEFT_WRIST, RIGHT_WRIST, LEFT_ANKLE, RIGHT_ANKLE

4. **Pose_openness**: float
It calculates the openness of a pose based on the landmarks of the holistic model. The landmark used here are LEFT_SHOULDER, RIGHT_SHOULDER, LEFT_HIP, RIGHT_HIP, LEFT_WRIST, RIGHT_WRIST. The landmark coordinate value are multiplied by image_w and image_h is to scale the coordinates from normalized values (ranging from 0 to 1) to the corresponding pixel coordinates in the image. / openness of main body

5. **Leaning**: str [‘Backward’, ‘Forward’]
It determines the leaning direction of the person based on the position of the nose relative to the hips.

6. **Head_horizontal**: str [‘Left’, ‘Right’, ‘Still’]
Calculation: It determines the horizontal direction of the head movement based on the change in the position of the nose between consecutive frames.

7. **Head_vertical**: str [‘Up’, ‘Down’, ‘Still’]
It determines the vertical direction of the head movement based on the change in the position of the nose between consecutive frames.

8. **left_arm_angle** & **right_arm_angle**: float
It determines the angle of the left arm and right arm based on the landmarks of the holistic model. For calculating the angle, WRIST-ELBOW-SHOULDER coordinates for left and right arms are used.

9. **left_arm_v_movement** & **right_arm_v_movement**: str [‘Up’, ‘Down’]
It determines vertical movement(‘UP’ or ‘DOWN’) of left and right arms based on the left_arm_angle and right_arm_angle.

10. **left_arm_h_movement** & **right_arm_h_movement**: str [‘Forward’, ‘Calculating’]
It determines horizontal movement(‘FORWARD’) of left and right arms based on the position of WRIST relative to the ELBOW.

11. **left_hand_orientation** & **right_hand_orientation**: str [‘Right’, ‘Left’, ‘Up’, ‘Down’]
It determines the orientation of the hand(‘Right’, ‘Left’, ‘Up’, ‘Down’) based on the landmarks in the left and right hands. Landmarks used are WRIST and MIDDLE_FINGER_MCP and the calculation is done by determining the slope of the line connecting these landmarks.

12. **left_hand_state** & **right_hand_state**: str [‘Closed’, ‘Open’]
It determines whether a hand is ‘CLOSED’ or ‘OPEN’ based on the euclidean distance between THUMB_TIP and INDEX_TIP landmarks. 

## Acoustic Features
1. **Avg_pitch**: float
It calculates the average pitch of the 10 seconds audio segment using the piptrack function from the librosa library.

2. **Avg_intensity**: float
It calculates the average intensity of the 10 seconds audio segment using the piptrack function from the librosa library.

3. **Transcription**: string 
It transcribes the 10 seconds audio segment using the Google Speech Recognition service through the recognize_google method from the speech_recognition library.

## Cross-modality Features
**Contradiction** between expected gestures and actual gestures

This code aims to identify and output the rows where there are contradictions between the expected gestures based on words in the transcript and the actual recorded gestures. The contradictions are detected by comparing the values in the dataframe with the expected values specified in the word_gesture_map dictionary.

Steps undertook:
- Split the transcript into individual words and store them in the words variable.
- Iterate over each word in the words list.
- If the word is present in the word_gesture_map dictionary:
  - Get the expected gestures associated with the word.
  - Iterate over each gesture and expected value pair.
  - Compare the expected value with the actual value in the row for the corresponding gesture.
- If a contradiction is found (the values don't match), print the word, the actual value, and the expected value, and return the row.
