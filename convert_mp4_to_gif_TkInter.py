import tkinter as tk
import moviepy.editor as mp
from tkinter import filedialog

# Define function to convert MP4 to GIF
def convert_video_to_gif():
    # Prompt user to select input video file
    input_file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    
    # Prompt user to select output GIF file path and name
    output_file_path = filedialog.asksaveasfilename(defaultextension=".gif")
    
    # Convert MP4 to GIF using MoviePy
    video = mp.VideoFileClip(input_file_path)
    video.write_gif(output_file_path)
    
    # Show success message to user
    success_label = tk.Label(root, text="Video converted to GIF successfully!", padx=21,pady=11,font="lucida 14 bold")
    success_label.pack()

# Create main window and button to trigger conversion
root = tk.Tk()
root.title("MP4 to GIF Converter")

convert_button = tk.Button(root, text="Convert MP4 to GIF. Specify the path to the file location", padx=21,pady=11,font="lucida 14 bold",bg="orange",command=convert_video_to_gif)
convert_button.pack()

root.mainloop()


