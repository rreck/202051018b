```json
{
  "id": "7e3ba41b1014881c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291011,
  "host_pid": "9e6742732c60:1",
  "hash": "30166b7e3d3e1ed86371898bc0d8b5c25773998d79a573668881743cc01c5779",
  "cid": "QmV130166b7e3d3e1ed86371898bc0d8b5c25773998d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291011,
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
      "evaluated_at": 1760291011
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
  "sig": "9d63c91726cf65d907440445290ac431c17ee552e8b3a8d4ed3a35744d5064da"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037990803
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 38403750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': 'be616144f18eac0b'}}}