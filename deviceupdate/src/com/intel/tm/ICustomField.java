package com.intel.tm;

public interface ICustomField
{
	void setValue(String value);
	String getValue();
	void setName(String name);
	String getName();
	void setType(CustomFieldType ctype);
	CustomFieldType getType();
	
	

}
