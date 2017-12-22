export STREAMER_PATH=$HOME/mjpg-streamer-code-182/mjpg-streamer
export LD_LIBRARY_PATH=$STREAMER_PATH

raspistill --nopreview -w 640 -h 480 -q 5 -bm -o /home/pi/Pictures/pic.jpg -tl 500 -t 9999999 -th 0:0:0 | $STREAMER_PATH/mjpg_streamer -i "$STREAMER_PATH/input_file.so -f /home/pi/Pictures -n pic.jpg" -o "$STREAMER_PATH/output_http.so -w $STREAMER_PATH/www"

