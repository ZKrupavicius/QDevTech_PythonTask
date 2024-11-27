def analyze_traffic_lights(filepath):

    traffic_light_occurrences = {'Red': 0, 'Yellow': 0, 'Green': 0}
    light_active_time = {'Red': 0, 'Yellow': 0, 'Green': 0}
    green_light_time = []
    error_lines_count = 0

    with open(filepath, 'r') as file:
        file.readline()

        for line in file:
            parts = line.strip().split(',')
            red, yellow, green = int(parts[0]), int(parts[1]), int(parts[2])
            time_active = int(parts[3])
            clock_time = parts[4]

            if red:
                traffic_light_occurrences['Red'] += 1
                light_active_time['Red'] += time_active
            if yellow:
                traffic_light_occurrences['Yellow'] += 1
                light_active_time['Yellow'] += time_active
            if green:
                traffic_light_occurrences['Green'] += 1
                light_active_time['Green'] += time_active
                green_light_time.append(f"[{clock_time}]")

            active_lights = [red, yellow, green]
            if sum(active_lights) != 1:
                error_lines_count += 1

    return traffic_light_occurrences, light_active_time, green_light_time, error_lines_count


def write_to_file(output_filename, traffic_light_occurrences, light_active_time, green_light_time, error_lines_count):
    with open(output_filename, 'w') as file:
        file.write(f"Occurrences: {traffic_light_occurrences}\n")
        file.write(f"Total Active Time: {light_active_time}\n")
        file.write(f"Green Active Times: {green_light_time}\n")
        file.write(f"Lines with Errors: {error_lines_count}\n")


filepath = 'data.txt'
output_filepath = 'output.txt'
traffic_light_occurrences, light_active_time, green_light_time, error_lines_count = analyze_traffic_lights(filepath)
write_to_file(output_filepath, traffic_light_occurrences, light_active_time, green_light_time, error_lines_count)

