import tkinter as tk

import pygame

import os


class MusicPlayer:

    def __init__(self, master):

        self.master = master

        self.master.title("Music Player")

        self.playlist = []

        pygame.mixer.init()

        self.createthewidgets()

    def createthewidgets(self):

        self.playlist_box = tk.Listbox(self.master, width=50)

        self.playlist_box.pack(padx=10, pady=10)


        self.button_frame = tk.Frame(self.master)

        self.button_frame.pack(pady=10)


        self.add_button = tk.Button(self.button_frame, text="Add Song", command=self.addthesong)

        self.add_button.pack(side=tk.LEFT, padx=5)


        self.remove_button = tk.Button(self.button_frame, text="Remove Song", command=self.removethesong)

        self.remove_button.pack(side=tk.LEFT, padx=5)


        self.play_button = tk.Button(self.button_frame, text="Play", command=self.playthemusic)

        self.play_button.pack(side=tk.LEFT, padx=5)



        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stopthemusic)

        self.stop_button.pack(side=tk.LEFT, padx=5)



    def addthesong(self):

        song = tk.filedialog.askopenfilename(initialdir="/", title="Select Song", filetypes=(("Audio Files", "*.mp3"),))

        if song:

            self.playlist.append(song)

            self.playlist_box.insert(tk.END, os.path.basename(song))

    def playthemusic(self):

        selected_song = self.playlist_box.curselection()

        if selected_song:

            index = selected_song[0]

            song = self.playlist[index]

            pygame.mixer.music.load(song)

            pygame.mixer.music.play()


    def stopthemusic(self):

        pygame.mixer.music.stop()

    def removethesong(self):

        selected_song = self.playlist_box.curselection()

        if selected_song:

            index = selected_song[0]

            self.playlist.pop(index)

            self.playlist_box.delete(index)

root = tk.Tk()

music_player = MusicPlayer(root)

root.mainloop()
