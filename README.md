# cycleaudio v0.1

#### Description
Quick project I tossed together last night to analyze my deskcycle out of curiosity. The plug for the spedometer timer etc looked just like a 3.5 audio jack. I plugged it into an extender cable and into my sound card. At first I messed around with using my cycle output to an audio file (wav) format. I noticed in the playback a disctinct click when the cycle would turn over one time. I analyzed the frequency in Audacity to see the clear disctinction between the cycle rotations.

Using python I generate a numpy graph of the audio output to a png file that is rendered in an html file that has a js function that constantly updates the page. I studied the output signals frequency and determined a decent value to denote when a rotation has occured **32000** or **-32000**. I noticed I could record the frequency instance 2 times within my time span, so I divide the actual value by 2 and print even modulous to get an accurate number of cycles.



```
python3 matlab_visualizer.py
```
![Alt text](./docs/cycleaudio.png?raw=true "cycleaudio v0.1")
### Built With
* [Python](https://www.python.org/) - Python 3.5 +
* [Pyaudio](https://people.csail.mit.edu/hubert/pyaudio/)
* [Numpy](http://www.numpy.org/)
* [Pylab](https://scipy.github.io/old-wiki/pages/PyLab)

### Todo
-   Get the distance 1 rotation is equivalent to to calculate distance traveled in a session
-   Get the frequency of rotations over time to determine speed once distance is known.
-   Timer and # rotations on HTML
-   Session recording to CSV
-   Graphing of sessions overtime

### Authors
* **Justin Chase** - [JustinChase](https://github.com/jujum4n)
    - Idea 
    - Implementation

### License
This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments
* Thanks to anyone who's examples were used
* Inspiration
* water

### Ubuntu install
To install PyAudio you will need to install the portaudio19-dev package. You can do this by running the following command:
`sudo apt install portaudio19-dev`
