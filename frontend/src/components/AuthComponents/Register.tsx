import React from 'react';
import {useUserRegister} from "../../hooks/userRegister";
import { Grid, Box, Typography, TextField, Button } from '@mui/material';

export const Register: React.FC = () => {
    const {formData, error, loading, handleChange, handleSubmit} = useUserRegister();

    return (
        <Grid container justifyContent="center" alignItems="center" style={{ minHeight: '100vh' }}>
            <Box p={4} boxShadow={3} borderRadius={2}>
                <Typography variant="h4" align="center" gutterBottom>
                    Register
                </Typography>
                {error && (
                    <Typography color="error" align="center" gutterBottom>
                        {error}
                    </Typography>
                )}
                <form onSubmit={handleSubmit}>
                    <TextField label="Username" name="username" fullWidth margin="normal" value={formData.username} onChange={handleChange} required />
                    <TextField label="Email" name="email" type="email" fullWidth margin="normal" value={formData.email} onChange={handleChange} required />
                    <TextField label="First Name" name="firstName" fullWidth margin="normal" value={formData.firstName} onChange={handleChange} required />
                    <TextField label="Last Name" name="lastName" fullWidth margin="normal" value={formData.lastName} onChange={handleChange} required />
                    <TextField label="Password" name="password" type="password" fullWidth margin="normal" value={formData.password} onChange={handleChange} required />
                    <TextField label="Confirm Password" name="confirmPassword" type="password" fullWidth margin="normal" value={formData.confirmPassword} onChange={handleChange} required />
                    <Box mt={2}>
                        <Button type="submit" variant="contained" color="primary" fullWidth disabled={loading}>
                            {loading ? 'Registering...' : 'Register'}
                        </Button>
                    </Box>
                </form>
            </Box>
        </Grid>
    );
}
export default Register;