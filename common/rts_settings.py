from common.settings_subclass import SettingsSubclass


class RTSConfigurationLayout(SettingsSubclass):
    """Settings for the RTS configuration layout"""

    def __init__(self):
        """Constructor"""
        self.font_size_limits: list = [6, 25]  # limits for the font size selection choice
        # list of scaling values [%]
        self.scaling_list: list = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 175, 200, 225, 250, 275, 300]
        self.build_order_search_size: list = [160, 30]  # size of the search bar for the build order
        self.build_order_selection_vertical_spacing: int = 3  # vertical spacing between two build order suggestions
        self.selected_build_order_color: list = [230, 159, 0]  # color for selected build order
        self.hovering_build_order_color: list = [204, 102, 0]  # color for build order hovered by mouse
        self.bo_list_max_count: int = 10  # maximum count of valid build orders in the selection list
        self.bo_list_fuzz_search: bool = True  # True to use fuzzy search, False for splitting words search
        self.bo_list_fuzz_score_cutoff: int = 50  # score cutoff parameter for the fuzzy search


class RTSConfigurationUsernameLayout(RTSConfigurationLayout):
    """Settings for the AoE2 configuration layout (with username)"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.search_spacing: int = 10  # space between the searching bars
        self.username_search_size: list = [160, 30]  # size of the search bar for the username
        self.selected_username_color: list = [86, 180, 233]  # color for selected username


class RTSBuildOrderLayout(SettingsSubclass):
    """Settings for the RTS build order layout"""

    def __init__(self):
        """Constructor"""
        self.image_height: int = 30  # height of the build order images
        self.resource_spacing: int = 3  # space between the build order resources
        self.bo_next_tab_spacing: int = 30  # horizontal spacing between build order last button and next tab button


class RTSBuildOrderTooltipLayout(SettingsSubclass):
    """Settings for the RTS build order layout (tooltip part)"""

    def __init__(self):
        """Constructor"""
        self.color_default: list = [255, 255, 255]  # default text RGB color for the font
        self.color_background: list = [0, 0, 0]  # background RGB color of the tooltip window
        self.opacity: float = 0.8  # opacity of the tooltip window
        self.vertical_spacing: int = 2  # vertical spacing for the tooltip lines
        self.border_size: int = 5  # border size of the tooltip window
        self.timeout: int = 1500  # time after which the tooltip is removed [ms]


class RTSLayout(SettingsSubclass):
    """Settings for the RTS layout"""

    def __init__(self):
        """Constructor"""
        self.opacity: float = 0.75  # opacity of the window
        self.upper_right_position: list = [1871, 67]  # initial position of the upper right corner
        self.border_size: int = 15  # size of the borders
        self.vertical_spacing: int = 10  # vertical spacing
        self.horizontal_spacing: int = 6  # horizontal spacing
        self.font_police: str = 'Arial'  # font police type
        self.font_size: int = 11  # font size (selected value for 'font_size_limits')
        self.scaling: int = 100  # scaling value [%] (selected value for 'scaling_list')
        self.color_default: list = [255, 255, 255]  # default text RGB color for the font
        self.color_background: list = [30, 30, 30]  # background RGB color
        self.action_button_size: int = 22  # size of the action buttons
        self.action_button_spacing: int = 8  # horizontal spacing between the action buttons
        self.build_order: RTSBuildOrderLayout = RTSBuildOrderLayout()  # build order layout


class RTSImages(SettingsSubclass):
    """Settings for the RTS images"""

    def __init__(self):
        """Constructor"""
        self.game_icon: str = 'icon/salamander_sword_shield.ico'  # game overlay icon
        self.next_panel: str = 'action_button/to_end.png'  # go to the next next_panel
        self.build_order_previous_step: str = 'action_button/previous.png'  # go to previous step in the build order
        self.build_order_next_step: str = 'action_button/next.png'  # go to next step in the build order
        self.quit: str = 'action_button/leave.png'  # quit the overlay
        self.save: str = 'action_button/save.png'  # save the settings
        self.load: str = 'action_button/load.png'  # load the settings
        self.config_hotkeys: str = 'action_button/gears.png'  # configure the hotkeys
        self.write_build_order: str = 'action_button/feather.png'  # write a build order
        self.time: str = 'icon/time.png'  # time for build order


class RTSHotkeysConfigurationLayout(SettingsSubclass):
    """Settings for the panel to configure the RTS hotkeys layout"""

    def __init__(self):
        """Constructor"""
        self.font_police: str = 'Arial'  # font police type
        self.font_size: int = 11  # font size
        self.color_font: list = [255, 255, 255]  # color of the font
        self.color_background: list = [30, 30, 30]  # color of the background
        self.opacity: float = 0.8  # opacity of the window
        self.border_size: int = 10  # size of the borders
        self.edit_width: int = 200  # width for the hotkeys edit fields
        self.edit_height: int = 30  # height for the hotkeys edit fields
        self.button_margin: int = 5  # margin from text to button border
        self.vertical_spacing: int = 10  # vertical spacing between the elements
        self.horizontal_spacing: int = 10  # horizontal spacing between the elements


class RTSHotkeys(SettingsSubclass):
    """Settings for the RTS hotkeys"""

    def __init__(self):
        """Constructor"""
        self.enter: str = 'Return'  # enter selection key
        self.select_next_build_order: str = 'Tab'  # select the next build order
        self.next_panel: str = ''  # cycle through the next panel
        self.show_hide: str = ''  # show/hide the application
        self.build_order_previous_step: str = ''  # go to the previous build order step
        self.build_order_next_step: str = ''  # go to the next build order step

        self.config = RTSHotkeysConfigurationLayout()  # panel to configure the hotkeys


class RTSOverlaySettings(SettingsSubclass):
    """Settings for the RTS overlay"""

    def __init__(self):
        """Constructor"""
        self.hotkeys = RTSHotkeys()  # hotkeys

        self.mouse_call_ms = 20  # interval between 2 calls related to mouse motion [ms]