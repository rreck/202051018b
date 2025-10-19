```json
{
  "id": "6659c4e685b63b76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285800,
  "host_pid": "9e6742732c60:1",
  "hash": "302419d01671a2d4d0d87c1474c93b1658d4b34e7d584b172c9ee838025ed368",
  "cid": "QmV1302419d01671a2d4d0d87c1474c93b1658d4b34e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285800,
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
      "evaluated_at": 1760285800
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
  "sig": "1abdccc3ef682d228f8b1ac3fa6696eb85530425bcd752248a3c9061f21d60dd"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 503193792297075
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285764, 'matching_hash': 'f478a6eb1bcd883b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '503193790', 'validation_error': 'Invalid routing number checksum'}}}