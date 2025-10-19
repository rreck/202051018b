```json
{
  "id": "cbbe8e608d7d576d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285765,
  "host_pid": "9e6742732c60:1",
  "hash": "9479856604638798607d40d83ba4746d456b3995abedccc4e39939c4f44efc65",
  "cid": "QmV19479856604638798607d40d83ba4746d456b3995",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285765,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760285765
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "3cd3c4d5ae383584a3e94d24e9d84876769bb0f0d3804586492972ecceb44b8f"
}
```

Fraud detected: invalid_routing (score: 95)
Transaction: 649338001689495
Details: {'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '649338005', 'validation_error': 'Invalid routing number checksum'}}}