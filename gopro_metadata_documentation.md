# GoPro metadata documentation

The `gpmf_to_json.py` script converts a `.mp4` file into a `.json` file containing embedded GoPro sensor metadata. Each key in the resulting JSON corresponds to a specific sensor or data stream, and is associated with:

* a list of **timestamps** (`timestamps_s`) in seconds (frequency varies per sensor),
* a list of **values** (`data`) measured at each timestamp.

Below is a description of the main keys found in the metadata:

## `img_timestamps_s`

List of timestamps (in seconds) corresponding to each video frame.

## `ACCL`: acceleration

Contains 3 components: acceleration along the $x$, $y$, and $z$ axes. Unit: $\mathrm{m.s^{-1}}$.

## `GYRO`: gyroscope metadata

Contains 3 components: angular velocity around $x$, $y$, and $z$ axes tracking roll, pitch and yaw. Unit: $\mathrm{rad.s^{-1}}$.

## `GPS5` are GPS values

Contains 5 components:

* Latitude in degrees
* Longitude in degrees
* Altitude in meters
* 2D speed (horizontal) in $\mathrm{m.s^{-1}}$
* 3D speed (total) in $\mathrm{m.s^{-1}}$

## `GRAV` is the gravity vector value

Contains 3 components representing the gravity vector along the 3 axes in $g$ unit. It indicates the direction of gravity relative to the camera orientation. It is useful for understanding tilt or inclination.

## `MAGN`: magnetometer metadata

Contains 3 components: magnetic field in $x$, $y$, and $z$. The unit is in $μT$ (microteslas). It is used to estimate compass heading and thus camera orientation.

## `CORI` is the camera orientation

It is a quaternion (4 components) describing the camera axis positions over time. Unit: degrees.

## `IORI` is the stabilized image orientation

It is also a quaternion describing the orientation of the image after being stabilized by GoPro algorithms (e.g., HyperSmooth). Thus values are often floats close to integers. It represents how the video frame was adjusted for stabilization.

**Note**: lengths of `timestamps_s` and `data` differ between sensors due to different sampling rates (Hz).
