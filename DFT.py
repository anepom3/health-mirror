import numpy as np
import matplotlib.pyplot as plotter

def dft(signal): 
    #plotter.plot(signal)
    frameRate = 30 #30 frames per second
    lengthOfVideo = 30
    fourierTransform = np.fft.rfft(signal) / signal.size
    timePlot = np.arange(0, lengthOfVideo, 1 / frameRate); #used to graph signal
    values = np.arange(int(signal.size/2))
    timePeriod = signal.size / frameRate #makes the domain of the fourierTransform in seconds
    frequencies = values / timePeriod
    positiveFFT = np.abs(fourierTransform[0 : signal.size//2])
    figure, graph = plotter.subplots(2, 1)
    graph[0].set_ylabel("RGB-value")
    graph[0].set_xlabel("Frame")
    graph[0].plot(timePlot, signal)
    graph[1].set_ylabel("RGB value")
    graph[1].set_xlabel("Frequency [1/s]")
    graph[1].stem(frequencies, positiveFFT)
    plotter.grid()
    plotter.show()
    highestPeak(signal, positiveFFT)

def highestPeak(signal, fft):
    frameRate = 30
    fourierFrequencies = np.fft.fftfreq(signal.size)
    frequency = fourierFrequencies[np.argmax(fft)] #gets frequency at the max index value of fft (1 per frame).
    frequencyPerSecond = frequency * frameRate
    print(frequencyPerSecond)
    return frequencyPerSecond

def generateWave():
    beginTime = 0
    endTime = 30 #length of video is 30 seconds.
    signal1Frequency = 0.5
    time = np.arange(beginTime, endTime, 1 / 30) #creates an array of 900 frames.
    amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
    return amplitude1
    

dft(generateWave())
    