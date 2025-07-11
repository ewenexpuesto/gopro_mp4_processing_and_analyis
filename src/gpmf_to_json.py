from py_gpmf_parser.gopro_telemetry_extractor import GoProTelemetryExtractor
import os

def extract_data_from_mp4(input_paths: list, output_paths: list) -> None:
    for filepath, output_path in zip(input_paths, output_paths):
        print(f"\nProcessing file: {filepath}")
        try:
            # Instanciation de l’extracteur
            extractor = GoProTelemetryExtractor(filepath)
            extractor.open_source()

            # Extraction des données GPS
            gps, gps_t = extractor.extract_data("GPS5")
            print("Premiers points GPS :")
            for i in range(min(5, len(gps))):
                print(gps[i], "à", gps_t[i])

            # Créer le dossier de sortie s'il n'existe pas
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            # Exporter vers le chemin de sortie donné
            extractor.extract_data_to_json(output_path,
                                           ["ACCL", "GYRO", "GPS5", "GRAV", "MAGN", "CORI", "IORI"])
            print("Exported to:", output_path)

            extractor.close_source()
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

input_paths = [
    "data1/GH010025.MP4",
    "data1/GH020025.MP4",
    "data2/GH010024.MP4",
    "data2/GH020024.MP4",
    "data2/GH030024.MP4",
#    "data/video1.mp4",
#    "data/video2.mp4"
]

output_paths = [
    "json/GH010025.MP4.json",
    "json/GH020025.MP4.json",
    "json/GH010024.MP4.json",
    "json/GH020024.MP4.json",
    "json/GH030024.MP4.json",
#    "json/video1.json",
#    "json/video2.json"
]

extract_data_from_mp4(input_paths, output_paths)
# Doesn't work with video files that have been concatenated, as they don't have the GPMF metadata.