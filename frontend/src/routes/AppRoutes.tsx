import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import AuthenticationPage from '../src/pages/AuthPage/Authentication'
import Login from './components/AuthComponents/Login';
import Register from './components/AuthComponents/Register';

const AppRoutes : React.FC = () => {
    return(
        <BrowserRouter>
            <Routes>
                <Route path='/auth' element={<AuthenticationPage />}>
                    <Route path='/login' element={<Login />} />
                    <Route path='/login' element={<Register />} />
                </Route>
            </Routes>
        </BrowserRouter>
    )
}

export default AppRoutes;