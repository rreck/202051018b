```json
{
  "id": "57ae58ab332750b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287751,
  "host_pid": "9e6742732c60:1",
  "hash": "a7573670c012ec1a1a8d452e74b20e9bc1e7a8a5dc3018a487eee705a156fb41",
  "cid": "QmV1a7573670c012ec1a1a8d452e74b20e9bc1e7a8a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287751,
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
      "evaluated_at": 1760287751
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "73faf45173f5be225a2033e6d98ce21189acf1db67479dfac4e1548d11af4d61"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 044000032306947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285763, 'matching_hash': '0095d1181b74b3e8'}}}