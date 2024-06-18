import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Inner actions data
data = {
    "DOP Code": ["DOP01", "DOP01", "DOP01", "DOP01", "DOP01", "DOP01",
                 "DOP02", "DOP02", "DOP02", "DOP02", "DOP02",
                 "DOP03", "DOP03", "DOP03", "DOP03", "DOP03", "DOP03",
                 "DOP04", "DOP04", "DOP04", "DOP04", "DOP04", "DOP04", "DOP04",
                 "DOP05", "DOP05", "DOP05", "DOP05", "DOP05", "DOP05",
                 "DOP06", "DOP06", "DOP06", "DOP06",
                 "DOP07", "DOP07", "DOP07", "DOP07",
                 "DOP08", "DOP08", "DOP08", "DOP08",
                 "DOP09", "DOP09", "DOP09", "DOP09",
                 "DOP10", "DOP10", "DOP10", "DOP10",
                 "DOP11", "DOP11", "DOP11", "DOP11", "DOP11",
                 "DOP12", "DOP12", "DOP12", "DOP12", "DOP12", "DOP12"],
    "DOP Description": [
        "Balance the ground land-use of the city considered as a whole ecosystem consisting of both natural and socio-economics components. SDG Target 11.7, 11a, 11b",
        "Balance the ground land-use of the city considered as a whole ecosystem consisting of both natural and socio-economics components. SDG Target 11.7, 11a, 11b",
        "Balance the ground land-use of the city considered as a whole ecosystem consisting of both natural and socio-economics components. SDG Target 11.7, 11a, 11b",
        "Balance the ground land-use of the city considered as a whole ecosystem consisting of both natural and socio-economics components. SDG Target 11.7, 11a, 11b",
        "Balance the ground land-use of the city considered as a whole ecosystem consisting of both natural and socio-economics components. SDG Target 11.7, 11a, 11b",
        "Balance the ground land-use of the city considered as a whole ecosystem consisting of both natural and socio-economics components. SDG Target 11.7, 11a, 11b",
        "Implement Permeability to facilitate Urban Flow. SDG Target 11.7, 11a, 11b",
        "Implement Permeability to facilitate Urban Flow. SDG Target 11.7, 11a, 11b",
        "Implement Permeability to facilitate Urban Flow. SDG Target 11.7, 11a, 11b",
        "Implement Permeability to facilitate Urban Flow. SDG Target 11.7, 11a, 11b",
        "Implement Permeability to facilitate Urban Flow. SDG Target 11.7, 11a, 11b",
        "Balance the distribution of key types of uses and foster multifunctional spaces SDG Target 11.",
        "Balance the distribution of key types of uses and foster multifunctional spaces SDG Target 11.",
        "Balance the distribution of key types of uses and foster multifunctional spaces SDG Target 11.",
        "Balance the distribution of key types of uses and foster multifunctional spaces SDG Target 11.",
        "Balance the distribution of key types of uses and foster multifunctional spaces SDG Target 11.",
        "Balance the distribution of key types of uses and foster multifunctional spaces SDG Target 11.",
        "Make biodiversity an important part of urban life. SDG Target 11.7; 11a",
        "Make biodiversity an important part of urban life. SDG Target 11.7; 11a",
        "Make biodiversity an important part of urban life. SDG Target 11.7; 11a",
        "Make biodiversity an important part of urban life. SDG Target 11.7; 11a",
        "Make biodiversity an important part of urban life. SDG Target 11.7; 11a",
        "Make biodiversity an important part of urban life. SDG Target 11.7; 11a",
        "Make biodiversity an important part of urban life. SDG Target 11.7; 11a",
        "Create connected open space system, activate urban metabolism. SDG Target 11.7; 11a",
        "Create connected open space system, activate urban metabolism. SDG Target 11.7; 11a",
        "Create connected open space system, activate urban metabolism. SDG Target 11.7; 11a",
        "Create connected open space system, activate urban metabolism. SDG Target 11.7; 11a",
        "Create connected open space system, activate urban metabolism. SDG Target 11.7; 11a",
        "Create connected open space system, activate urban metabolism. SDG Target 11.7; 11a",
        "Promote Walkability, cycling and reinforce their integration with public transportation SDG Target 11.",
        "Promote Walkability, cycling and reinforce their integration with public transportation SDG Target 11.",
        "Promote Walkability, cycling and reinforce their integration with public transportation SDG Target 11.",
        "Promote Walkability, cycling and reinforce their integration with public transportation SDG Target 11.",
        "Balancing the public transportation potential. SDG target 11.2",
        "Balancing the public transportation potential. SDG target 11.2",
        "Balancing the public transportation potential. SDG target 11.2",
        "Balancing the public transportation potential. SDG target 11.2",
        "Change from multi-modality to inter-modality concept. SDG Target 11.2",
        "Change from multi-modality to inter-modality concept. SDG Target 11.2",
        "Change from multi-modality to inter-modality concept. SDG Target 11.2",
        "Change from multi-modality to inter-modality concept. SDG Target 11.2",
        "Fostering local energy production; building as component of a community energy system. SDG Target 11b",
        "Fostering local energy production; building as component of a community energy system. SDG Target 11b",
        "Fostering local energy production; building as component of a community energy system. SDG Target 11b",
        "Fostering local energy production; building as component of a community energy system. SDG Target 11b",
        "Linking the city to its food. Toward a new balance between city, agriculture, and food system. SDG Targets 2.1; 2.3; 2.4; 2b; 2c",
        "Linking the city to its food. Toward a new balance between city, agriculture, and food system. SDG Targets 2.1; 2.3; 2.4; 2b; 2c",
        "Linking the city to its food. Toward a new balance between city, agriculture, and food system. SDG Targets 2.1; 2.3; 2.4; 2b; 2c",
        "Linking the city to its food. Toward a new balance between city, agriculture, and food system. SDG Targets 2.1; 2.3; 2.4; 2b; 2c",
        "Prevent the negative impact of waste, facilitating the transition from a Linear to an urban circularity model. SDG target 11.6",
        "Prevent the negative impact of waste, facilitating the transition from a Linear to an urban circularity model. SDG target 11.6",
        "Prevent the negative impact of waste, facilitating the transition from a Linear to an urban circularity model. SDG target 11.6",
        "Prevent the negative impact of waste, facilitating the transition from a Linear to an urban circularity model. SDG target 11.6",
        "Prevent the negative impact of waste, facilitating the transition from a Linear to an urban circularity model. SDG target 11.6",
        "Implement an Integrated Urban Water Management (IUWM). SDG Targets 2.1; 2.3; 2.4; 2b; 2c",
        "Implement an Integrated Urban Water Management (IUWM). SDG Targets 2.1; 2.3; 2.4; 2b; 2c",
        "Implement an Integrated Urban Water Management (IUWM). SDG Targets 2.1; 2.3; 2.4; 2b; 2c",
        "Implement an Integrated Urban Water Management (IUWM). SDG Targets 2.1; 2.3; 2.4; 2b; 2c",
        "Implement an Integrated Urban Water Management (IUWM). SDG Targets 2.1; 2.3; 2.4; 2b; 2c",
        "Implement an Integrated Urban Water Management (IUWM). SDG Targets 2.1; 2.3; 2.4; 2b; 2c"
    ],
    "Action Code": ["Action 1.1", "Action 1.2", "Action 1.3", "Action 1.4", "Action 1.5", "Action 1.6",
                    "Action 2.1", "Action 2.2", "Action 2.3", "Action 2.4", "Action 2.5",
                    "Action 3.1", "Action 3.2", "Action 3.3", "Action 3.4", "Action 3.5", "Action 3.6",
                    "Action 4.1", "Action 4.2", "Action 4.3", "Action 4.4", "Action 4.5", "Action 4.6", "Action 4.7",
                    "Action 5.1", "Action 5.2", "Action 5.3", "Action 5.4", "Action 5.5", "Action 5.6",
                    "Action 6.1", "Action 6.2", "Action 6.3", "Action 6.4",
                    "Action 7.1", "Action 7.2", "Action 7.3", "Action 7.4",
                    "Action 8.1", "Action 8.2", "Action 8.3", "Action 8.4",
                    "Action 9.1", "Action 9.2", "Action 9.3", "Action 9.4",
                    "Action 10.1", "Action 10.2", "Action 10.3", "Action 10.4",
                    "Action 11.1", "Action 11.2", "Action 11.3", "Action 11.4", "Action 11.5",
                    "Action 12.1", "Action 12.2", "Action 12.3", "Action 12.4", "Action 12.5", "Action 12.6"],
    "Action Description": [
        "Adopt an urban containment and compact, mixed-use development in urban areas to reduces land consumption and promotes efficient resource utilization.",
        "Implement a peri-urban agricultural land protection strategy.",
        "Develop green infrastructure such as parks, green roofs, and wetlands to provide ecosystem services.",
        "Reduce urban land cover and soil sealing by promoting vegetation growth and permeable paving systems that allow water infiltration, instead of runoff into stormwater systems.",
        "Implement green open spaces like community gardens, urban farms, and pocket parks to reduce soil sealing, mitigate urban heat islands, absorb stormwater, provide wildlife habitats, and offer recreational opportunities for urban residents.",
        "Prioritize infill development on vacant or underutilized urban land promotes sustainable and liveable development, efficient urban infrastructure utilization, and reduces environmental impacts linked to urban sprawl.",
        "Design a connected network of streets providing multiple access points.",
        "Design Pedestrian-friendly streets: Incorporating the pedestrian and cycling paths with open spaces and greenery.",
        "Integrate ride-sharing platforms into a bicycle-oriented urban strategy to increase transportation options and decrease single-occupancy vehicles.",
        "Apply filtered permeability principles to create pedestrian, cyclist, and public transportation-friendly urban environments by restricting motor vehicle movement.",
        "Implement eye-levelled greenery lines as an effective way to improve urban permeability by creating more inviting and attractive urban environments for pedestrians, cyclists, and other users of public space.",
        "Improve proximity to work/activity from sprawl to proximity.",
        "Prioritize compact, mixed-use, and walkable development patterns.",
        "Improve pedestrian accessibility/walkability.",
        "Encourages multi-functional buildings.",
        "Improve influential factors that contribute to the comfort of public space; make the space inviting, attractive and provide social satisfaction.",
        "Prioritize integration combining residential, commercial, and office space around public transportation hubs.",
        "Enhance ecological restoration in cities by restoring degraded and underutilized land to improve local ecosystem health and wildlife habitat.",
        "Design and preserve of Habitat corridors (Urban integrated Green Spaces)",
        "Increase and promote creation of green infrastructures in built environment.",
        "Activate the vegetation and food products emphasizes the importance of incorporating vegetation and food production into the design of urban spaces.",
        "Incorporate and enhance nature-based Solutions (NBS) and their management into urban planning areas.",
        "Integrate both green and non-green infrastructures in a holistic landscape approach.",
        "Measuring and monitoring biodiversity.",
        "Create a connected, continuous, and integrated system of urban open green spaces.",
        "Include in green network system active play spaces, playgrounds, water features, informal sports and game spaces, and recreation spaces.",
        "Develop a green infrastructure strategy that identifies priority areas for new green infrastructure.",
        "Design a connected network that integrates green infrastructure, such as green roofs, green walls, bioswales, rain gardens, and nature-based solutions, with the urban built environment.",
        "Design open spaces connected with green corridors and integrate green infrastructure with the urban built environment and provide ecosystem services.",
        "Adopt an overall strategy to support the development of peri-urban agriculture.",
        "Improve the spatial quality and attractiveness of streets by revitalizing public areas, making them quieter, increasing recreational areas, and promoting new uses.",
        "Creating dedicated bike lanes and pedestrian-friendly streets, prioritizing non-motorized traffic.",
        "Encourage mixed-use development by designing neighborhoods with amenities and services within a walking or cycling distance.",
        "Develop complete streets that accommodate all modes of transportation, including cars, bikes, pedestrians, and public transportation.",
        "Enhancing transit connectivity through transport hubs.",
        "Combine use of bicycles and transit services as a distinct transport mode.",
        "Activate a joint land use-transit model for integrating land use and transit planning.",
        "Adopt Travel Demand Management (TDM) strategy.",
        "Develop Implement a connected, systems approach to support inter-modality: This includes building bike lanes, pedestrian walkways, transit lanes, and dedicated parking areas for bike and car-sharing.",
        "Mitigate the effect of the environmental impact of transportation systems integrating different modes of transportation.",
        "Implement car-free zone integrated with congestion pricing to discourage single-occupancy vehicle use and promote carpooling or alternative modes of transportation. Provide real-time transportation information.",
        "Create transportation hubs where different modes of transportation can be easily accessed and interchanged, making it easier for users to switch between modes.",
        "Promote the diffusion of the Nearly Zero-Energy standard and beyond, towards the Positive Energy Building (PEB) model.",
        "Apply local power generation and integration of renewable energy systems in buildings.",
        "Local energy communities to improve resource management and energy performance.",
        "Encourage the use of microgrids, which allow buildings to generate, store, and distribute their own energy within a community.",
        "Provide fresh and affordable variety of food from pre-urban agriculture in a walkable distance.",
        "Activate circular life cycles from natural resources till bio wastes.",
        "Design spaces capable to host multifunctional production technologies.",
        "Design public/semipublic spaces for the community to cultivate food together.",
        "Develop services, actions, and tools that help decrease solid waste generation on the site, specifically by reducing single-use and non-recyclable plastics and surplus food, and by fostering goods repairability and recyclability.",
        "Design physical spaces for separated waste collection within buildings to manage waste effectively, reduce treating organic waste via dehydrators, composting, and on-site anaerobic digestion, on-site gardens and vegetable patches for on-site consumption.",
        "Adopt a smart waste management system: Smart waste management systems can help neighborhoods optimize waste collection and reduce waste generation by providing data on waste generation and collection.",
        "Implement a community recycling program: Neighborhoods can implement community recycling programs to help residents recycle properly and reduce contamination.",
        "Reducing material flow and embodied energy in construction and everyday consumption.",
        "Using wetland as a post treatment.",
        "Use of a green wall for treating grey water and reusing especially for the place with lack of space.",
        "Using Natural Filtration units.",
        "Adopt Greywater Treatment with Membrane Bioreactor Technology.",
        "Implement measures to treat wastewater and use it for non-potable purposes such as irrigation, landscaping, and industrial processes.",
        "Implement measures such as green roofs, permeable pavements, and rainwater harvesting to manage stormwater and prevent flooding."
    ]
}

# Create DataFrame
df_inner = pd.DataFrame(data)

# Interlinkage (outer actions) data
interlinkage = {
    "Action 1.1": ["Action 7.1", "Action 6.5", "Action 6.3", "Action 4.1", "Action 3.4", "Action 3.2", "Action 3.1"],
    "Action 1.2": ["Action 10.1", "Action 5.6", "Action 4.7", "Action 4.5", "Action 4.4", "Action 4.3"],
    "Action 1.3": ["Action 2.5", "Action 3.3", "Action 4.1", "Action 4.2", "Action 4.5", "Action 4.6", "Action 4.7",
                   "Action 5.5", "Action 6.1"],
    "Action 1.4": ["Action 12.3", "Action 12.5", "Action 12.6"],
    "Action 1.5": ["Action 2.5", "Action 3.3", "Action 4.5", "Action 4.6", "Action 5.1", "Action 5.4", "Action 5.5"],
    "Action 1.6": ["Action 3.2", "Action 6.3", "Action 12.6"],
    "Action 2.1": ["Action 3.1", "Action 3.3", "Action 3.5", "Action 5.3", "Action 6.1", "Action 6.5", "Action 7.1",
                   "Action 8.1"],
    "Action 2.2": ["Action 3.1", "Action 3.3", "Action 3.5", "Action 5.3", "Action 6.1", "Action 6.2", "Action 8.3"],
    "Action 2.3": ["Action 3.5", "Action 6.3", "Action 7.2", "Action 8.2", "Action 8.3"],
    "Action 2.4": ["Action 3.3", "Action 3.5", "Action 6.1", "Action 6.2", "Action 6.4", "Action 6.6", "Action 8.3"],
    "Action 2.5": ["Action 1.3", "Action 1.5", "Action 3.2", "Action 3.3", "Action 3.5", "Action 4.3", "Action 4.6",
                   "Action 6.1", "Action 6.2"],
    "Action 3.1": ["Action 1.1", "Action 2.1", "Action 2.2", "Action 7.2", "Action 6.3"],
    "Action 3.2": ["Action 2.5", "Action 1.6", "Action 1.1", "Action 5.2", "Action 6.2", "Action 6.3"],
    "Action 3.3": ["Action 1.3", "Action 1.5", "Action 2.1", "Action 2.2", "Action 2.4", "Action 2.5", "Action 4.4",
                   "Action 5.1", "Action 5.2", "Action 5.4", "Action 6.1", "Action 6.2", "Action 6.3"],
    "Action 3.4": ["Action 1.1", "Action 10.4", "Action 10.3", "Action 6.2"],
    "Action 3.5": ["Action 2.1", "Action 2.2", "Action 2.3", "Action 2.4", "Action 2.5", "Action 5.1", "Action 5.2",
                   "Action 5.3", "Action 5.4", "Action 5.5", "Action 5.6", "Action 6.1", "Action 6.2", "Action 10.4"],
    "Action 3.6": ["Action 6.3", "Action 8.4"],
    "Action 4.1": ["Action 1.3", "Action 1.1", "Action 12.2", "Action 12.1", "Action 7.1", "Action 5.4", "Action 5.1"],
    "Action 4.2": ["Action 5.1", "Action 5.2", "Action 5.3", "Action 6.3", "Action 12.1", "Action 12.2", "Action 1.3"],
    "Action 4.3": ["Action 5.2", "Action 6.1", "Action 9.1", "Action 12.1", "Action 1.2", "Action 2.5"],
    "Action 4.4": ["Action 5.2", "Action 5.6", "Action 10.1", "Action 10.4", "Action 12.1", "Action 12.6", "Action 1.2",
                   "Action 3.3"],
    "Action 4.5": ["Action 10.4", "Action 12.1", "Action 1.2", "Action 1.3", "Action 1.5"],
    "Action 4.6": ["Action 5.4", "Action 6.1", "Action 10.4", "Action 12.1", "Action 1.3", "Action 1.5", "Action 2.5"],
    "Action 4.7": ["Action 1.2", "Action 1.3"],
    "Action 5.1": ["Action 6.1", "Action 6.4", "Action 6.5", "Action 7.2", "Action 1.5", "Action 3.3", "Action 3.5",
                   "Action 4.1", "Action 4.2"],
    "Action 5.2": ["Action 6.3", "Action 4.4", "Action 4.3", "Action 4.2", "Action 3.5", "Action 3.3", "Action 3.2"],
    "Action 5.3": ["Action 6.1", "Action 6.3", "Action 6.4", "Action 9.1", "Action 2.1", "Action 2.2", "Action 3.5",
                   "Action 4.2"],
    "Action 5.4": ["Action 4.6", "Action 4.1", "Action 3.5", "Action 3.3", "Action 1.5", "Action 9.3", "Action 6.6"],
    "Action 5.5": ["Action 6.1", "Action 1.3", "Action 1.5", "Action 3.5"],
    "Action 6.1": ["Action 7.2", "Action 8.3", "Action 1.3", "Action 2.1", "Action 2.2", "Action 2.4", "Action 2.5",
                   "Action 3.3", "Action 3.5", "Action 4.3", "Action 4.6", "Action 5.1", "Action 5.3", "Action 5.5"],
    "Action 6.2": ["Action 3.5", "Action 3.4", "Action 3.3", "Action 3.2", "Action 2.5", "Action 2.4", "Action 2.2",
                   "Action 7.1", "Action 7.2", "Action 7.3", "Action 8.1", "Action 8.2", "Action 8.4"],
    "Action 6.3": ["Action 1.1", "Action 1.6", "Action 2.3", "Action 3.1", "Action 3.2", "Action 3.3", "Action 3.6",
                   "Action 4.2", "Action 5.2", "Action 5.3"],
    "Action 6.4": ["Action 5.3", "Action 5.1", "Action 2.4", "Action 8.4", "Action 8.2", "Action 8.1"],
    "Action 6.5": ["Action 5.1", "Action 2.1", "Action 1.1"],
    "Action 6.6": ["Action 5.4", "Action 2.4", "Action 8.4"],
    "Action 7.1": ["Action 6.2", "Action 4.1", "Action 2.1", "Action 1.1", "Action 8.2", "Action 8.1"],
    "Action 7.2": ["Action 6.2", "Action 6.1", "Action 5.1", "Action 3.1", "Action 2.3", "Action 9.1", "Action 8.2",
                   "Action 8.1"],
    "Action 7.3": ["Action 6.2", "Action 8.1"],
    "Action 7.4": ["Action 8.1"],
    "Action 8.1": ["Action 2.1", "Action 6.2", "Action 6.4", "Action 7.1", "Action 7.2", "Action 7.3", "Action 7.4"],
    "Action 8.2": ["Action 2.3", "Action 6.2", "Action 6.4", "Action 7.1", "Action 7.2"],
    "Action 8.3": ["Action 6.1", "Action 2.4", "Action 2.3", "Action 2.2"],
    "Action 8.4": ["Action 6.6", "Action 6.4", "Action 6.2", "Action 3.6"],
    "Action 9.1": ["Action 7.2", "Action 5.3", "Action 4.3"],
    "Action 9.2": ["Action 11.2"],
    "Action 9.3": ["Action 5.4", "Action 11.4", "Action 12.4"],
    "Action 9.4": ["Action 10.3", "Action 5.6"],
    "Action 10.1": ["Action 4.4", "Action 1.2", "Action 12.3", "Action 12.2", "Action 12.1"],
    "Action 10.2": ["Action 11.1", "Action 11.2", "Action 11.3", "Action 12.4", "Action 12.5"],
    "Action 10.3": ["Action 9.4", "Action 11.4", "Action 12.5", "Action 3.4"],
    "Action 10.4": ["Action 4.6", "Action 4.5", "Action 4.4", "Action 3.5", "Action 3.4"],
    "Action 11.1": ["Action 10.2", "Action 12.1"],
    "Action 11.2": ["Action 9.2", "Action 10.2", "Action 12.3"],
    "Action 11.3": ["Action 10.2", "Action 12.2"],
    "Action 11.4": ["Action 9.3", "Action 10.3", "Action 12.2"],
    "Action 11.5": ["Action 12.2"],
    "Action 12.1": ["Action 10.1", "Action 11.1", "Action 4.6", "Action 4.5", "Action 4.4", "Action 4.3", "Action 4.2",
                    "Action 4.1"],
    "Action 12.2": ["Action 10.1", "Action 11.3", "Action 11.4", "Action 11.5", "Action 4.2", "Action 4.1"],
    "Action 12.3": ["Action 10.1", "Action 11.2", "Action 1.4"],
    "Action 12.4": ["Action 9.3", "Action 10.2"],
    "Action 12.5": ["Action 10.2", "Action 10.3", "Action 1.4", "Action 1.5"],
    "Action 12.6": ["Action 4.4", "Action 1.6", "Action 1.4"]
}

# Convert interlinkage to DataFrame
df_outer = pd.DataFrame.from_dict(interlinkage, orient='index')
df_outer = df_outer.reset_index().melt(id_vars=['index'], var_name='Outer Link', value_name='Linked Action').dropna()
df_outer.columns = ['Action Code', 'Outer Link', 'Linked Action']

# Merge inner and outer dataframes
df_merged = df_inner.merge(df_outer, on='Action Code', how='left')

# Streamlit application
st.title("DOP Actions Interactive Viewer")

selected_dops = st.multiselect(
    "Select DOPs",
    options=df_inner["DOP Code"].unique(),
    format_func=lambda x: x
)

if selected_dops:
    st.header("Inner Actions")
    for dop in selected_dops:
        st.subheader(dop)
        actions = df_inner[df_inner["DOP Code"] == dop]
        for _, action in actions.iterrows():
            st.write(f"{action['Action Code']}: {action['Action Description']}")

    st.header("Outer Actions")
    outer_action_counts = {}
    for dop in selected_dops:
        actions = df_inner[df_inner["DOP Code"] == dop]
        for action_code in actions["Action Code"]:
            linked_actions = df_outer[df_outer["Action Code"] == action_code]["Linked Action"]
            for linked_action in linked_actions:
                if linked_action not in outer_action_counts:
                    outer_action_counts[linked_action] = 0
                outer_action_counts[linked_action] += 1

    sorted_outer_actions = sorted(outer_action_counts.items(), key=lambda item: item[1], reverse=True)

    # Prepare data for heatmap
    heatmap_data = pd.DataFrame(list(outer_action_counts.items()), columns=['Action', 'Frequency'])
    heatmap_data = heatmap_data.sort_values(by='Frequency', ascending=False).set_index('Action')

    # Customizable color palette
    cmap_option = st.selectbox('Select Color Map', options=plt.colormaps(), index=plt.colormaps().index('viridis'))

    # Create heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_data, annot=True, cmap=cmap_option, cbar_kws={'label': 'Frequency'})
    plt.title('Frequency of Outer Actions Based on Selected DOPs')
    st.pyplot(plt)
