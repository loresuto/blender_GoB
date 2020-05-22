# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


"""Addon preferences"""
import bpy
from bpy.types import AddonPreferences


class GoBPreferences(AddonPreferences):
    bl_idname = __package__

    #GLOBAL
    flip_up_axis: bpy.props.BoolProperty(
        name="Invert up axis",
        description="Enable this to invert the up axis on import/export",
        default=False)
    flip_forward_axis: bpy.props.BoolProperty(
        name="Invert forward axis",
        description="Enable this to invert the forward axis on import/export",
        default=False)
    show_button_text: bpy.props.BoolProperty(
        name="Show header buttons text",
        description="Enable this to show the import/export text of the header buttons",
        default=False)        
    performance_profiling: bpy.props.BoolProperty(
        name="[Debug] Process durations",
        description="This is used to identiyfy slow code, note this will slow down your transfer if enabled!",
        default=True)

    # EXPORT
    export_modifiers: bpy.props.EnumProperty(
        name='Modifiers',
        description='How to handle exported object modifiers',
        items=[('APPLY_EXPORT', 'Export and Apply', 'Apply modifiers to object and export them to zbrush'),
               ('ONLY_EXPORT', 'Only Export', 'Export modifiers to zbrush but do not apply them to mesh'),
               ('IGNORE', 'Ignore', 'Do not export modifiers')
               ],
        default='ONLY_EXPORT')

    export_polygroups: bpy.props.EnumProperty(
        name="Polygroups",
        description="Polygroups mode",
        items=[ ('FACE_MAPS', 'from Face Maps', 'Create Polygroups from Face Maps'), 
                ('MATERIALS', 'from Materials', 'Create Polygroups from Materials'),
                ('VERTEX_GROUPS', 'from Vertex Groups', 'Create Polygroups from Vertex Groups'),
                ('NONE', 'None', 'Do not Create Polygroups'),
               ],
        default='NONE')
    # ('FACEMAPS', 'from ** Face Maps', 'Create Polygroups from Face Maps'),


    export_scale_factor: bpy.props.FloatProperty(
        name="** Scale",
        description="export_scale_factor",
        default=1.0,
        min=0,
        soft_max=2,
        step=0.1,
        precision=2,
        subtype='FACTOR')    
    
    export_mask: bpy.props.BoolProperty(
        name="Mask",
        description="Export Maks",
        default=True)


    # IMPORT
    import_material: bpy.props.EnumProperty(
            name="Create material",
            description="choose source for material import",
            items=[('TEXTURES', '** from Textures', 'Create mateial inputs from textures'),        #TODO
                   ('POLYGROUPS', '** from Polygroup', 'Create material inputs from polygroups'),  #TODO
                   ('POLYPAINT', 'from Polypaint', 'Create material inputs from polypaint'),
                   ('NONE', 'None', 'No additional material inputs are created'),
                   ],
            default='POLYPAINT')
            
    import_method: bpy.props.EnumProperty(
            name="Import Button Method",
            description="Manual Mode requires to press the import every time you send a model from zbrush to import it.",
            items=[('MANUAL', 'Manual', 'Manual Mode requires to press the import every time you send a model from zbrush to import it.'),
                   ('AUTOMATIC', 'Automatic', 'Automatic Mode'),
                   ],
            default='AUTOMATIC')

    import_scale_factor: bpy.props.FloatProperty(
        name="** Scale",
        description="import_scale_factor",
        default=1.0, min=0, soft_max=2, step=0.1, precision=2,
        subtype='FACTOR')

    import_polypaint: bpy.props.BoolProperty(
        name="Polypaint to Vertex Color",
        description="Import Polypaint as Vertex Color",
        default=True)
    
    import_polypaint_name: bpy.props.StringProperty(
        name="Vertex Color Name", 
        description="Set name for Vertex Color Layer", 
        default="Col")

    import_polygroups_to_vertexgroups: bpy.props.BoolProperty(
        name="Polygroups to Vertex Groups",
        description="Import Polygroups as Vertex Groups",
        default=True)
       
    import_polygroups_to_facemaps: bpy.props.BoolProperty(
        name="Polygroups to Face Maps",
        description="Import Polygroups as Face Maps",
        default=True)

    apply_facemaps_to_facesets: bpy.props.BoolProperty(
        name="Apply Face Maps to Face Sets",
        description="apply_facemaps_to_facesets",
        default=True)
        
    import_mask: bpy.props.BoolProperty(
        name="Mask to Vertex Group",
        description="Import Mask to Vertex Group",
        default=True)

    import_uv: bpy.props.BoolProperty(
        name="UV Map",
        description="Import Uv Map from Zbrush",
        default=True)
        
    import_uv_name: bpy.props.StringProperty(
        name="UV Map Name", 
        description="Set name for the UV Map", 
        default="UVMap")


        
    imp_tex_diffuse_suffix: bpy.props.StringProperty(
        name="Diffuse Suffix", 
        description="Set Suffix for Diffuse Texture", 
        default="diff")
    imp_tex_displace_suffix: bpy.props.StringProperty(
        name="Displacement Suffix", 
        description="Set Suffix for Displace Texture", 
        default="disp")
    imp_tex_normal_suffix: bpy.props.StringProperty(
        name="Normal Suffix", 
        description="Set Suffix for Normal Texture", 
        default="norm")
    
  
    def draw(self, context):
        #GLOBAL
        layout = self.layout
        layout.use_property_split = True

        layout.prop(self, 'flip_up_axis')
        layout.prop(self, 'flip_forward_axis')
        layout.prop(self, 'show_button_text')        
        layout.prop(self, 'performance_profiling')      
           

        #EXPORT
        col = layout.column()
        box = layout.box()
        box.label(text='Export', icon='EXPORT')  
        #box.prop(self, 'export_scale_factor')      #TODO
        box.prop(self, 'export_modifiers')
        box.prop(self, 'export_polygroups')    
        #box.prop(self, 'export_mask')       #TODO: not yet supported by blender (16.5.2020)


        # IMPORT
        col = layout.column(align=True)
        box = layout.box()
        box.label(text='Import', icon='IMPORT')
        #box.prop(self, 'import_method')            #TODO: disabled: some bugs when switching
        #box.prop(self, 'import_scale_factor')      #TODO
        box.prop(self, 'import_material')         
        
        col = box.column(align=True)            

        #col.prop(self, 'import_mask')
        #col.prop(self, 'import_uv')
        col.prop(self, 'import_polypaint')       
        col.prop(self, 'import_polygroups_to_vertexgroups')
        col.prop(self, 'import_polygroups_to_facemaps')          
        col.prop(self, 'apply_facemaps_to_facesets')


        col = box.column(align=True) 
        col.prop(self, 'imp_tex_diffuse_suffix') 
        col.prop(self, 'imp_tex_displace_suffix') 
        col.prop(self, 'imp_tex_normal_suffix')

        col = box.column(align=True) 
        col.prop(self, 'import_uv_name') 
        col.prop(self, 'import_polypaint_name') 


