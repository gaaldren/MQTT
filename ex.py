import speedtest
test = speedtest.Speedtest()
download = test.download()
download = (download / 1024)/1024
round(download,2)

print(round(download,2))