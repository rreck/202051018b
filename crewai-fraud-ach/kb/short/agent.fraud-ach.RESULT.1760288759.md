```json
{
  "id": "debe58fffffaa1ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288759,
  "host_pid": "9e6742732c60:1",
  "hash": "057712f7e93a380ff08c8c79049f1e22ce792b7d4b6ede8bc6d95640baaf3d34",
  "cid": "QmV1057712f7e93a380ff08c8c79049f1e22ce792b7d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288759,
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
      "evaluated_at": 1760288759
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
  "sig": "12888346646aee4e023fd86da3603217c93fcdf80fd3afba0f04bb3f5556a8e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157869633
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 13104072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285763, 'matching_hash': '3a805d178d839f31'}}}