import unreal
import os

# Config
alembic_directory = "C:/path/to/alembic/files"
ue_destination_path = "/Game/MyGame/Models"  # "/Game/" represents the "Content" folder


def main():
    # Get the Asset Tools instance
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

    # Get all Alembic files in the directory
    alembic_files = [file for file in os.listdir(alembic_directory) if file.endswith('.abc')]

    # Yes you need to apply these settings every loop
    for alembic_file in alembic_files:

        # Define import options for Alembic files
        import_options = unreal.AbcImportSettings()
        import_options.import_type = unreal.AlembicImportType.SKELETAL
        import_options.normal_generation_settings.recompute_normals = True
        import_options.material_settings.find_materials = True
        import_options.conversion_settings.rotation = unreal.Vector(x=90, y=0, z=90)
        import_options.conversion_settings.scale = unreal.Vector(x=100, y=-100, z=100)
        import_options.conversion_settings.flip_v = True
        import_options.sampling_settings.skip_empty = True
        import_options.sampling_settings.sampling_type = unreal.AlembicSamplingType.PER_FRAME
        import_options.sampling_settings.frame_start = 0
        import_options.sampling_settings.frame_end = 100
        import_options.sampling_settings.frame_steps = 1
        import_options.sampling_settings.time_steps = 1
        import_options.compression_settings.base_calculation_type = unreal.BaseCalculationType.PERCENTAGE_BASED
        import_options.compression_settings.percentage_of_total_bases = 100
        import_options.compression_settings.bake_matrix_animation = True
        import_options.compression_settings.max_number_of_bases = 999

        # Import all Alembic files
        full_path = os.path.join(alembic_directory, alembic_file)
        import_alembic_file(full_path, ue_destination_path, asset_tools, import_options)


def import_alembic_file(filepath, destination, asset_tools, import_options):
    task = unreal.AssetImportTask()
    task.filename = filepath
    task.destination_path = destination
    task.replace_existing = True
    task.save = True
    task.automated = True
    task.options = import_options
    
    asset_tools.import_asset_tasks([task])


if __name__ == '__main__':
    main()