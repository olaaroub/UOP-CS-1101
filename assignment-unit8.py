def invert_server_roles(input_file, output_file):
    """
    Reads a file mapping Server -> Roles, inverts it to Role -> Servers,
    and writes the result to an output file.
    """
    server_dict = {}
    inverted_dict = {}

    try:
        # STEP 1: READ FROM FILE
        # Use 'with' context manager to safely open the file
        with open(input_file, 'r') as file_in:
            for line in file_in:
                # Clean whitespace and skip empty lines
                line = line.strip()
                if not line:
                    continue

                # Parse the line: "web-01: Frontend, API"
                # split(':', 1) ensures we only split on the first colon
                parts = line.split(':', 1)

                if len(parts) == 2:
                    server = parts[0].strip()
                    # The value might be a list of roles "Frontend, API"
                    # We split by comma to handle multiple roles
                    roles_str = parts[1].strip()
                    roles_list = [r.strip() for r in roles_str.split(',')]

                    server_dict[server] = roles_list

        # STEP 2: INVERT THE DICTIONARY
        # Logic: Iterate through the original dict and flip keys/values
        for server, roles in server_dict.items():
            for role in roles:
                if role not in inverted_dict:
                    inverted_dict[role] = [server]
                else:
                    inverted_dict[role].append(server)

        # STEP 3: WRITE TO OUTPUT FILE
        with open(output_file, 'w') as file_out:
            for role, servers in inverted_dict.items():
                # Join the list of servers into a comma-separated string
                servers_str = ", ".join(servers)
                file_out.write(f"{role}: {servers_str}\n")

        print(f"Success! Processed {len(server_dict)} servers.")
        print(f"Output written to '{output_file}'.")

    # STEP 4: EXCEPTION HANDLING
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to write to '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Main Execution ---
invert_server_roles("server_config.txt", "roles_inventory.txt")