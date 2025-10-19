```json
{
  "id": "f089717069b9ad3b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291389,
  "host_pid": "9e6742732c60:1",
  "hash": "ce0c9a34bb130876c7451b3308734fb65ac570393770f4e518619f05f736d412",
  "cid": "QmV1ce0c9a34bb130876c7451b3308734fb65ac57039",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291389,
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
      "evaluated_at": 1760291389
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
  "sig": "ac00bebda4198ac4350f1c84c9ba05babd81ffd18a119012efc84d92dcfc3878"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158127705
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 51109542, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': 'c9228fea95a929fd'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '261425248', 'validation_error': 'Invalid routing number checksum'}}}