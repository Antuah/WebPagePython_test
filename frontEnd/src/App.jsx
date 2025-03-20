import './App.css'
import { AnimatePresence } from 'framer-motion'
import {BrowserRouter as Router, Routes, Route, useLocation} from 'react-router-dom'
import axios from 'axios'
import Login from './components/Login'
import AboutUs from './pages/AboutUs'
import NotFound from './pages/404'
import Navbar from './components/Navbar'
import { useEffect, useState } from 'react'

const AnimatedRoutes = () => {
  const location = useLocation()

  return (
    <AnimatePresence mode='wait'>
      <Routes location={location} key={location.pathname}>
        <Route path='/login' element={<Login />} />
        <Route path='/about' element={<AboutUs />} />
        <Route path='/' element={<Home />} />
        <Route path='*' element={<NotFound />} />
      </Routes>
    </AnimatePresence>
  )
};

//To do 
//componente Home < -- Conexion con django (GET)
function Home() {
    const [data, setData] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
      axios 
        .get('http://localhost:8000/users/api/')
        .then((response) => {
          setData(response.data);
          setLoading(false);
        })
        .catch((error) => {
          setError('Error al cargar los datos de la API'+ error);
          setLoading(false);
        });
      }, []);
      if (loading) return 'Cargando...';

      if (error) return <div className='alert alert-danger'>{error}</div>;

      return (
        <div>
          <h1>Datos de usuarios</h1>
          <ul>
            {data.map((user) => (
              <li key={user.id}>{JSON.stringify(user)}</li>
            ))}
          </ul>
        </div>
      );
}


function App() {
  return (
    <Router>
      <Navbar/>
      <div className="container mt-4">
        <div className='row'>
        <div className='col'>
          <AnimatedRoutes />
        </div>
        </div>
      </div>
    </Router>
  );
}

export default App
