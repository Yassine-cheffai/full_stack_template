import './App.css'
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

function App() {
    return (
        <>
            <BasicButtons/>
        </>
    )
}

export default App


function BasicButtons() {
    return (
        <Stack spacing={2} direction="row">
            <Button variant="text">Text button blue</Button>
            <Button variant="contained">Contained</Button>
            <Button variant="outlined">Outlined</Button>
        </Stack>
    );
}
