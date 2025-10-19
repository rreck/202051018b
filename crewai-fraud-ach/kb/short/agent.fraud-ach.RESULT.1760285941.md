```json
{
  "id": "ced86a12df716101",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285941,
  "host_pid": "9e6742732c60:1",
  "hash": "db8ab03446e3678f43c8f9a1bae0315dbbfd08fad7ec2bb6b82e308fb9a5cf2b",
  "cid": "QmV1db8ab03446e3678f43c8f9a1bae0315dbbfd08fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285941,
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
      "evaluated_at": 1760285941
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
  "sig": "e0b1186883025c962cbe61d652783c11f673d97d2adbd3cfd219d093f0ca1e83"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 304701772219564
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285764, 'matching_hash': '19ec134c2c5b9271'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '304701776', 'validation_error': 'Invalid routing number checksum'}}}