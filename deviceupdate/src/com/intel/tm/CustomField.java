package com.intel.tm;

public class CustomField implements ICustomField
{
	private String _name="";
	private String _value="";
	private CustomFieldType _type=null;

	
	public CustomField(String name, CustomFieldType type)
	{
		super();
		this._name = name;
		this._type = type;
	}

	@Override
	public void setValue(String value)
	{
		// TODO Auto-generated method stub
		this._value=value;
	}

	@Override
	public String getValue()
	{
		// TODO Auto-generated method stub
		return this._value;
	}

	@Override
	public void setName(String name)
	{
		this._name=name;

	}

	@Override
	public String getName()
	{
		// TODO Auto-generated method stub
		return this._name;
	}

	@Override
	public void setType(CustomFieldType ctype)
	{
		// TODO Auto-generated method stub
		this._type=ctype;

	}

	@Override
	public CustomFieldType getType()
	{
		// TODO Auto-generated method stub
		return this._type;
	}

}
