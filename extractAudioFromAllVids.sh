for file in mundoNuevo/*
do
    echo $file
    avconv -i $file -vn -acodec copy $file.aac
done
