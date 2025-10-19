```json
{
  "id": "1e93ccc21d0b2c87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294883,
  "host_pid": "9e6742732c60:1",
  "hash": "01efb73bbab9a140af9ba3d9eded6508dba6992d96ae1d953204aa52e1d4bb59",
  "cid": "QmV101efb73bbab9a140af9ba3d9eded6508dba6992d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294883,
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
      "evaluated_at": 1760294883
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
  "sig": "aa4be6a10b1c4177fd6336a8358422c2af7834bfc4b93cb5c4060f92edebcf00"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030595065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 74752266, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '3889a0f66c8870f8'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '671070002', 'validation_error': 'Invalid routing number checksum'}}}