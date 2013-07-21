package com.intel.tm;

import java.util.Hashtable;

public class Device 
{
	private String name="";
	private String lab="";
	private String serialnumber="";
	private Dmengine dmengine=null;
	private Hashtable<String,ICustomField> customfields;
	
	public String getName()
	{
		return name;
	}
	public void setName(String name)
	{
		this.name = name;
	}
	public String getLab()
	{
		return lab;
	}
	public void setLab(String lab)
	{
		this.lab = lab;
	}
	public Dmengine getDmengine()
	{
		return dmengine;
	}
	public void setDmengine(Dmengine dmengine)
	{
		this.dmengine = dmengine;
	}
	public void addCustomField(ICustomField cf)
	{
		this.customfields.put(cf.getName(), cf);
	}
	public ICustomField getCustomField(String cfname)
	{
		return this.customfields.get(cfname);
	}
	public boolean removeCustomField(String cfname)
	{
		if (this.customfields.containsKey(cfname))
		{
			this.customfields.remove(cfname);
			return true;
		}
		else
		{
			return false;
		}
	}
	public String getSerialnumber()
	{
		return serialnumber;
	}
	public void setSerialnumber(String serialnumber)
	{
		this.serialnumber = serialnumber;
	}
}
