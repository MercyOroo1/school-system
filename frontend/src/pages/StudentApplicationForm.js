import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StudentApplicationForm = () => {
    const [formData, setFormData] = useState({
        first_name: '',
        middle_name: '',
        surname: '',
        dob: '',
        gender: '',
        current_class: '',
        admission_class: '',
        residence_name: '',
        current_school: '',
        nationality: '',
        phone_number: '',
        alternative_number: '',
        email: '',
        sibling: false,
        sibling_num: 0,
        parent_names: '',
        parent_: 0,
    });

    const [siblingFields, setSiblingFields] = useState([]);
    const [useSiblingDetails, setUseSiblingDetails] = useState(false);
    const [parentGuardianType, setParentGuardianType] = useState('');
    const [message, setMessage] = useState('');
    const [isFormValid, setIsFormValid] = useState(false);

    useEffect(() => {
        // Validate form to check if all required fields are filled
        const isValid = Object.values(formData).every(value => value !== '') &&
                        (formData.sibling ? formData.sibling_num > 0 : true);
        setIsFormValid(isValid);
    }, [formData]);

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData({
            ...formData,
            [name]: type === 'checkbox' ? checked : value
        });
    };

    const handleSiblingNumChange = (e) => {
        const siblingNum = e.target.value;
        setFormData({ ...formData, sibling_num: siblingNum });
        setSiblingFields([...Array(parseInt(siblingNum)).keys()]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:5000/application/student_applications', formData);
            setMessage(response.data.message);
        } catch (error) {
            setMessage('An error occurred. Please try again.');
            console.error(error);
        }
    };

    const handleUseSiblingDetails = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/application/check_sibling/${formData.sibling_num}`);
            if (response.data.found) {
                setMessage('Sibling details found and applied successfully.');
            } else {
                setMessage('Sibling not found. Please enter parent/guardian details.');
                setUseSiblingDetails(false);
            }
        } catch (error) {
            setMessage('Error fetching sibling details.');
            console.error(error);
        }
    };

    return (
        <div className="student-application-form">
            <h2>Student Application Form</h2>
            {message && <p>{message}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>First Name:</label>
                    <input type="text" name="first_name" value={formData.first_name} onChange={handleChange} required />
                </div>
                <div>
                    <label>Middle Name:</label>
                    <input type="text" name="middle_name" value={formData.middle_name} onChange={handleChange} required />
                </div>
                <div>
                    <label>Surname:</label>
                    <input type="text" name="surname" value={formData.surname} onChange={handleChange} required />
                </div>
                <div>
                    <label>Date of Birth:</label>
                    <input type="date" name="dob" value={formData.dob} onChange={handleChange} required />
                </div>
                <div>
                    <label>Gender:</label>
                    <select name="gender" value={formData.gender} onChange={handleChange} required>
                        <option value="">Select Gender</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                <div>
                    <label>Current Class:</label>
                    <input type="text" name="current_class" value={formData.current_class} onChange={handleChange} required />
                </div>
                <div>
                    <label>Admission Class:</label>
                    <input type="text" name="admission_class" value={formData.admission_class} onChange={handleChange} required />
                </div>
                <div>
                    <label>Residence Name:</label>
                    <input type="text" name="residence_name" value={formData.residence_name} onChange={handleChange} required />
                </div>
                <div>
                    <label>Current School:</label>
                    <input type="text" name="current_school" value={formData.current_school} onChange={handleChange} required />
                </div>
                <div>
                    <label>Nationality:</label>
                    <input type="text" name="nationality" value={formData.nationality} onChange={handleChange} required />
                </div>
                <div>
                    <label>Phone Number:</label>
                    <input type="tel" name="phone_number" value={formData.phone_number} onChange={handleChange} required />
                </div>
                <div>
                    <label>Alternative Number:</label>
                    <input type="tel" name="alternative_number" value={formData.alternative_number} onChange={handleChange} required />
                </div>
                <div>
                    <label>Email:</label>
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                </div>
                <div>
                    <label>Sibling:</label>
                    <input type="checkbox" name="sibling" checked={formData.sibling} onChange={handleChange} />
                </div>
                {formData.sibling && (
                    <>
                        <div>
                            <label>Number of Siblings:</label>
                            <input type="number" name="sibling_num" value={formData.sibling_num} onChange={handleSiblingNumChange} required />
                        </div>
                        {siblingFields.map((_, index) => (
                            <div key={index}>
                                <label>Sibling Name {index + 1}:</label>
                                <input type="text" name={`sibling_name_${index}`} onChange={handleChange} required />
                                <label>Sibling Grade {index + 1}:</label>
                                <input type="text" name={`sibling_grade_${index}`} onChange={handleChange} required />
                            </div>
                        ))}
                        <div>
                            <label>Use sibling parent/guardian details:</label>
                            <input type="radio" name="use_sibling_details" onClick={handleUseSiblingDetails} />
                        </div>
                        {!useSiblingDetails && (
                            <>
                                <div>
                                    <label>Enter Parent/Guardian Details:</label>
                                    <input type="radio" name="enter_parent_guardian" onClick={() => setParentGuardianType('parent')} />
                                </div>
                                {parentGuardianType && (
                                    <>
                                        <div>
                                            <label>{parentGuardianType === 'parent' ? 'Parent' : 'Guardian'} Name:</label>
                                            <input type="text" name="parent_names" value={formData.parent_names} onChange={handleChange} required />
                                        </div>
                                        <div>
                                            <label>Parent Information:</label>
                                            <input type="number" name="parent_" value={formData.parent_} onChange={handleChange} required />
                                        </div>
                                    </>
                                )}
                            </>
                        )}
                    </>
                )}
                <button type="submit" disabled={!isFormValid}>Submit Application</button>
            </form>
        </div>
    );
};

export default StudentApplicationForm:

