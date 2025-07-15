import React from 'react';

const InputField = ({ label, type, value, onChange }) => {
    return (
        <div className="input-field">
            <label>
                {label}
                <input
                    type={type}
                    value={value}
                    onChange={(e) => onChange(e.target.value)}
                    required
                />
            </label>
        </div>
    );
}

export default InputField;
