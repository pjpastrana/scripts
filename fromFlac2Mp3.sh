for file in Once/*
do
    echo $file
    #avconv -i $file -vn -acodec copy $file.aac
    ffmpeg -i "$file" -ab 320k -map_metadata 0 -id3v2_version 3 "$file".mp3
done
