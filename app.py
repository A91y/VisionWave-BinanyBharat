import streamlit as st
import cv2
import torch
import numpy as np
import chime
model = torch.hub.load('ultralytics/yolov5', 'custom', path='last2.pt')
outcome = 15  # awake


def main():
    st.set_page_config(page_title="Streamlit WebCam App")
    st.title("Webcam Display Steamlit App")
    st.caption("Powered by OpenCV, Streamlit")
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    stop_button_pressed = st.button("Stop")
    while cap.isOpened() and not stop_button_pressed:
        ret, frame = cap.read()
        results = model(frame)
        try:
            outcome = results.pred[0][0][-1]  # 16: drowsy, 15: awake
        except:
            pass
        if not ret:
            st.write("Video Capture Ended")
            break
        frame = np.squeeze(results.render())
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")
        try:
            if outcome == 16:
                chime.play_wav('sound.wav')
                st.rerun()
        except:
            pass
        if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
