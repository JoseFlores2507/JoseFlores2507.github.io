/*   // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-app.js";
  
  import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-auth.js";

  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  
  const auth = getAuth();
 */
  const firebaseConfig = {
    apiKey: "AIzaSyC9Xo9zpXopjKxNsYijBWQQrYud5sQMhWw",
    authDomain: "naturalista-5dd33.firebaseapp.com",
    projectId: "naturalista-5dd33",
    storageBucket: "naturalista-5dd33.appspot.com",
    messagingSenderId: "666572871427",
    appId: "1:666572871427:web:43d9c5ad4115a55122fb36"
  };
    
  import { getDatabase, set, ref, update } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-database.js";
  const db = getDatabase(app);

  function array_txt(info){
    fetch(info)
    .then(response => response.text())
    .then(data => {
  	// Do something with your data
    var array = data.match(/[^\n]+/g);

    return array;
    
  });
  }

  var images = array_txt('./data/images.txt');
  var links = array_txt('./data/links.txt');
  var names = array_txt('./data/names.txt');
  var scinames = array_txt('./data/scinames.txt');
  var titles = array_txt('./data/titles.txt');

  images.forEach(e => {
    set(ref(db, 'pictures/' + e), {
      images: images,
      links: links,
      names: names,
      scinames: scinames,
      titles: titles
  });
  });


