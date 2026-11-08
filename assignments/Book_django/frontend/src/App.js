import { useState } from "react";
import AddBook from "./pages/AddBook";
import Login from "./pages/Login";

function App() {
  const [authToken, setAuthToken] = useState(localStorage.getItem("access_token"));

  return (
    <div>
      {authToken ? <AddBook authToken={authToken} /> : <Login setAuthToken={setAuthToken} />}
    </div>
  );
}

export default App;
