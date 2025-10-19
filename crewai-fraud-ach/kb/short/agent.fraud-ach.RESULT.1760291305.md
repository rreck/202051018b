```json
{
  "id": "e5a1d70c346d28db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291305,
  "host_pid": "9e6742732c60:1",
  "hash": "9d5d80dde6c073501183036bc347cbcf643fa9c617e8e2dfe4fcc8db623be9d4",
  "cid": "QmV19d5d80dde6c073501183036bc347cbcf643fa9c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291305,
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
      "evaluated_at": 1760291305
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
  "sig": "71583fae9be412afb2770f383b63aa5feb735fe479e3f040d94aed86cb223967"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027962561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '3395f05250aaaeda'}}}een': 1760285763, 'matching_hash': 'cac17e8b7d36ee50'}}}