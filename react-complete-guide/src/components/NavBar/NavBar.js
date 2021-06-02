import React from "react"
import {Navbar, Nav, NavDropdown, Form,FormControl,Button} from 'react-bootstrap';
const navBar = () => (
    <Navbar bg="light" expand="lg">
        <Navbar.Brand href="http://127.0.0.1:5000/">ML&DM</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
                <Nav.Link href="/textclassify" >Text Classification</Nav.Link>
                <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                    
                    <NavDropdown.Item href="/about">About</NavDropdown.Item>
                    
                    
                </NavDropdown>
            </Nav>
            <Form inline>
                <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                <Button variant="outline-success">Search</Button>
            </Form>
        </Navbar.Collapse>
    </Navbar>
)
export default navBar;