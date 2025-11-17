import React from 'react';
import {useUserLogin} from "../../hooks/userLogin";
import { Grid, Box, Typography, TextField, Button } from '@mui/material';

export const Login: React.FC = () => {
    const {formData, error, loading, handleChange, handleSubmit} = useUserLogin();

    return(
        <Grid container justifyContent="center" alignItems="center" style={{ minHeight: '100vh' }}>
            <Box p={4} boxShadow={3} borderRadius={2}>
                <Typography variant="h4" align="center" gutterBottom>
                    Login
                </Typography>
                {error && (
                    <Typography color="error" align="center" gutterBottom>
                        {error}
                    </Typography>
                )}
                <form onSubmit={handleSubmit}>
                    <TextField label="Email" name="email" type="email" fullWidth margin="normal" value={formData.email} onChange={handleChange} required />
                    <TextField label="Password" name="password" type="password" fullWidth margin="normal" value={formData.password} onChange={handleChange} required />
                    <Box mt={2}>
                        <Button type="submit" variant="contained" color="primary" fullWidth disabled={loading}>
                            {loading ? 'Logging in...' : 'Login'}
                        </Button>
                    </Box>
                </form>
            </Box>
        </Grid>
    );
}
export default Login;