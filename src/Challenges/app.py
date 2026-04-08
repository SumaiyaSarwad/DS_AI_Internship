import streamlit as st

# ---------------- PAGE TITLE ----------------
st.title("🤖 RoboController 1.0")
st.subheader("Menu Driven Smart Navigation System")

# ---------------- ROBOT NAME ----------------
robot_name = st.text_input("Enter Robot Name")

# ---------------- SOURCE SELECTION ----------------
source_place = st.selectbox(
    "Select Source Place",
    ["Main Gate", "Hostel", "Parking", "Block B"]
)

# ---------------- DESTINATION SELECTION ----------------
destination_place = st.selectbox(
    "Select Destination Place",
    ["Library", "Canteen", "Block A", "Auditorium"]
)

# ---------------- AUTO DISTANCE DETECTION ----------------
if source_place == "Main Gate" and destination_place == "Library":
    distance = 120
elif source_place == "Main Gate" and destination_place == "Auditorium":
    distance = 180
elif source_place == "Hostel" and destination_place == "Canteen":
    distance = 300
elif source_place == "Hostel" and destination_place == "Library":
    distance = 350
elif source_place == "Parking" and destination_place == "Block A":
    distance = 200
elif source_place == "Block B" and destination_place == "Auditorium":
    distance = 250
else:
    distance = 100

st.info(f"📏 Auto-detected Distance: {distance} meters")

# ---------------- CHECKPOINT NAMES ----------------
st.markdown("### 🧭 Enter Checkpoint Names")
cp1 = st.text_input("Checkpoint 1 Name")
cp2 = st.text_input("Checkpoint 2 Name")
cp3 = st.text_input("Checkpoint 3 Name")

# ---------------- OBSTACLE SELECTION ----------------
obstacle = st.selectbox(
    "Select Obstacle Type",
    ["human", "animal", "vehicle", "wall", "none"]
)

# ---------------- DIRECTION & ACTION DECISION ----------------
if obstacle == "human":
    direction = st.selectbox("Choose Direction", ["left", "right", "straight"])
    action = "Slow and Move Safely"

elif obstacle == "animal":
    direction = st.selectbox("Choose Direction", ["left", "right"])
    action = "Move Carefully"

elif obstacle == "vehicle":
    direction = st.selectbox("Choose Direction", ["left", "right", "straight"])
    action = "Change Path"

elif obstacle == "wall":
    direction = st.selectbox("Choose Direction", ["left", "right"])
    action = "Avoid Wall"

else:
    direction = "straight"
    action = "Move Forward"

# ---------------- SPEED LOGIC ----------------
if obstacle == "human":
    speed = "Very Slow"
elif direction == "straight":
    speed = "Fast"
else:
    speed = "Slow"

# ---------------- CHECKPOINT ALLOCATION ----------------
checkpoints = []

if distance <= 50:
    checkpoints.append(cp1)
elif distance <= 100:
    checkpoints.extend([cp1, cp2])
else:
    checkpoints.extend([cp1, cp2, cp3])

# ---------------- START JOURNEY BUTTON ----------------
if st.button("🚀 Start Robot Journey"):

    st.success("Robot Journey Completed Successfully!")

    st.markdown("## 🧾 Trip Summary")
    st.write(f"**Robot Name:** {robot_name}")
    st.write(f"**Source Place:** {source_place}")
    st.write(f"**Destination Place:** {destination_place}")
    st.write(f"**Distance Covered:** {distance} meters")
    st.write(f"**Obstacle Encountered:** {obstacle}")
    st.write(f"**Action Taken:** {action}")
    st.write(f"**Direction Chosen:** {direction}")
    st.write(f"**Speed Mode:** {speed}")
    st.write(f"**Checkpoints Crossed:** {checkpoints}")

    st.markdown(
        f"""
        ### 📝 Final Statement  
        The robot **{robot_name}** travelled **{distance} meters** from **{source_place}**
        to **{destination_place}** by changing its direction to **{direction}**
        while encountering a **{obstacle}** obstacle.
        """
    )
