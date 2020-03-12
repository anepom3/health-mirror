# from inputs_outputs import test
from exhibit import video_setup, detect_faces, video_cleanup
test()
cap, faceCascade, out = video_setup()
cap, out = detect_faces(cap, faceCascade, out)
video_cleanup(cap, out)
