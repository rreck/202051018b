```json
{
  "id": "ab10b6341598d48c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294705,
  "host_pid": "9e6742732c60:1",
  "hash": "583ea912dec672e83b6b945b01748de25e9aceaec3c46f21fa3d8eb0445b2483",
  "cid": "QmV1583ea912dec672e83b6b945b01748de25e9aceae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294705,
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
      "evaluated_at": 1760294705
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
  "sig": "0f57f862fd6b1dc80685f5e314b3cd87933a6ce1c747a5a992c85d0f9de7ed53"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020641018
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 39296016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '9cb08faa1a3d5c0e'}}}