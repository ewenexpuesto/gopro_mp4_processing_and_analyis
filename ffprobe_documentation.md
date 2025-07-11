# `ffprobe` documentation

The `ffprobe` command is used to inspect media file structure and metadata like layers. Here the full command is `ffprobe GH010025.MP4`. See below for the [full command output](#full-output).

Original source of the command: [ffprobe documentation](https://ffmpeg.org/ffprobe.html)

## Output analysis

This document provides a structured explanation of the `ffprobe` output for a GoPro video file, based solely on ffprobe documentation.

### Container-level metadata fields

```bash
Metadata:
  major_brand     : mp41
  minor_version   : 538120216
  compatible_brands: mp41
```

These fields come from the beginning of the file called the `ftyp` box found in `.mp4`, `.mov` or `.m4a`:

- `major_brand` is a 4-character code that indicates the specification the file was made for in order to parse and interpret it correctly. `mp41` = MP4 version 1 (ISO/IEC 14496-1).
- `minor_version` is a 32-bit unsigned integer that provides **additional versioning information** about the file format used.
- `compatible_brands` is a list of brands (video players or devices) that can safely interpret the file.

### Creation time, firmware and bitrate

```bash
creation_time   : 2024-07-19T11:03:42.000000Z
  firmware        : H19.03.02.00.00
  Duration: 00:11:47.71, start: 0.000000, bitrate: 45277 kb/s
```

- `creation_time` indicates when the file was generated.
- `firmware` is a device-specific metadata added by the GoPro camera, indicating the software version installed on the device when the video was recorded.span
- `bitrate` is the average total data rate of the file, calculated as `file_size / duration` including video, audio, and data streams. A high bitrate like ~45 Mbps means high video quality.

### Stream #0:0 — Video Stream

```bash
Video: h264 (High) (avc1), yuvj420p(pc, bt709, progressive), 1920x1080, 59.94 fps
```

- `h264` high profile (Advanced Video Coding) is a type of encoding/decoding (codec) of analogical data to numerical.
- `Pixel format` `yuvj420p` is a way to build digital pixel by adding the luminance (dark/bright) with the color perceived by the camera.
- `Resolution`
- `Frame rate`

### Video Metadata

```bash
handler_name    : GoPro AVC
  vendor_id       : [0][0][0][0]
  encoder         : GoPro AVC encoder
  timecode        : 11:03:02:15
```

- `handler_name` is the name of the firmware (see before).
- `vendor_id` is a 4-character code in binary or ASCII identifying the creation (e.g., Apple, GoPro) with  `[0][0][0][0]` meaning it's empty or unspecified.

### Streams

A stream is an individual sequence (like a layer or a key in a dictionnary) of data representing a specific type of media or information inside a multimedia container file.

#### Stream `#0:1` is the audio stream

```bash
Audio: aac (LC), 48000 Hz, stereo, fltp, 189 kb/s
```

`aac` is the codec (Low Complexity).

- Sample rate: 48 kHz.
- Stereo audio.
- Format `fltp` is planar floating point, it means that each color or audio channel is stored in a separate contiguous memory plane (array), rather than together and that the samples (pixel values or audio samples) are stored as floating-point numbers, which can represent a wide dynamic range and fractional values.
- Bitrate.

#### Stream `#0:2` is the timecode

```bash
Data: none (tmcd)
```

- `tmcd`: timecode format (timestamp reference info)

#### Stream `#0:3` is the GoPro metadata (sensor data)

```bash
Data: bin_data (gpmd), 58 kb/s
```

- `gpmd` is the GoPro Metadata format (includes acceleration, GPS, gyro, etc.).
- Bitrate.

#### Stream `#0:4` is another metadata stream

```bash
Data: none (fdsc), 13 kb/s
```

- `fdsc` likely stands for field descriptor, which explains how to parse the `gpmd` binary metadata.
- Bitrate.

**Note** : metadata bitrate values are low because most of the data is in the mp4 pixels.

## Full output

```zsh
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'GH010025.MP4':
  Metadata:
    major_brand     : mp41
    minor_version   : 538120216
    compatible_brands: mp41
    creation_time   : 2024-07-19T11:03:42.000000Z
    firmware        : H19.03.02.00.00
  Duration: 00:11:47.71, start: 0.000000, bitrate: 45277 kb/s
  Stream #0:0[0x1](eng): Video: h264 (High) (avc1 / 0x31637661), yuvj420p(pc, bt709, progressive), 1920x1080 [SAR 1:1 DAR 16:9], 45002 kb/s, 59.94 fps, 59.94 tbr, 60k tbn (default)
    Metadata:
      creation_time   : 2024-07-19T11:03:42.000000Z
      handler_name    : GoPro AVC
      vendor_id       : [0][0][0][0]
      encoder         : GoPro AVC encoder
      timecode        : 11:03:02:15
  Stream #0:1[0x2](eng): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 189 kb/s (default)
    Metadata:
      creation_time   : 2024-07-19T11:03:42.000000Z
      handler_name    : GoPro AAC
      vendor_id       : [0][0][0][0]
      timecode        : 11:03:02:15
  Stream #0:2[0x3](eng): Data: none (tmcd / 0x64636D74) (default)
    Metadata:
      creation_time   : 2024-07-19T11:03:42.000000Z
      handler_name    : GoPro TCD
      timecode        : 11:03:02:15
  Stream #0:3[0x4](eng): Data: bin_data (gpmd / 0x646D7067), 58 kb/s (default)
    Metadata:
      creation_time   : 2024-07-19T11:03:42.000000Z
      handler_name    : GoPro MET
  Stream #0:4[0x5](eng): Data: none (fdsc / 0x63736466), 13 kb/s (default)
    Metadata:
      creation_time   : 2024-07-19T11:03:42.000000Z
      handler_name    : GoPro SOS
```
