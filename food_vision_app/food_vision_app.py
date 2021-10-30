# Logan Clark 10/29/2021
# App for running a Food Vision model
# Built with streamlit

# input = (224, 224, 3)

import streamlit as st
import numpy as np
import cv2 as cv


def main():
    readme_text = st.markdown(get_file_content_as_string("readme.md"))

    # Download model maybe

    # Sidebar Options
    st.sidebar.title("Sidebar")
    app_mode = st.sidebar.selectbox("Choose the mode",
                ["Show Instructions", "Input an Image", "Run the Model"])
    
    if app_mode == "Show Instructions":
        st.siderbar.success('Instructions')
    elif app_mode == "Input an Image":
        readme_text.empty()
        # input_image()
    elif app_mode == "Run the Model":
        readme_text.empty()
        # run_the_model()



# def download_file(file_path, url):
#     # # Don't download the file twice. (If possible, verify the download using the file length.)
#     # if os.path.exists(file_path):
#     #     if "size" not in EXTERNAL_DEPENDENCIES[file_path]:
#     #         return
#     #     elif os.path.getsize(file_path) == EXTERNAL_DEPENDENCIES[file_path]["size"]:
#     #         return

#     # These are handles to two visual elements to animate.
#     weights_warning, progress_bar = None, None
#     try:
#         weights_warning = st.warning("Downloading %s..." % file_path)
#         progress_bar = st.progress(0)
#         with open(file_path, "wb") as output_file:
#             with urllib.request.urlopen(url) as response:
#                 length = int(response.info()["Content-Length"])
#                 counter = 0.0
#                 MEGABYTES = 2.0 ** 20.0
#                 while True:
#                     data = response.read(8192)
#                     if not data:
#                         break
#                     counter += len(data)
#                     output_file.write(data)

#                     # We perform animation by overwriting the elements.
#                     weights_warning.warning("Downloading %s... (%6.2f/%6.2f MB)" %
#                         (file_path, counter / MEGABYTES, length / MEGABYTES))
#                     progress_bar.progress(min(counter / length, 1.0))

#     # Finally, we remove these visual elements by calling .empty().
#     finally:
#         if weights_warning is not None:
#             weights_warning.empty()
#         if progress_bar is not None:
#             progress_bar.empty()





# net = cv.dnn.readNet('model_weights.pb')


# inp = np.random.standard_normal([1, 3, 224, 224]).astype(np.float32)
# net.setInput(inp)
# out = net.forward()
# print(out.shape)






@st.cache(show_spinner=False)
def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/coganllark/TensorFlow_Cert_Projects/master/food_vision_app/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")

if __name__ == "__main__":
    main()




