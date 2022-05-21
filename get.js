

  import { getDatabase, set, ref, update } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-database.js";
  const db = getDatabase(app);

get(child(dbRef, `pictures/${1}`)).then((snapshot) => {
    if (snapshot.exists()) {
      console.log(snapshot.val());
    } else {
      console.log("No data available");
    }
  }).catch((error) => {
    console.error(error);
  });
  