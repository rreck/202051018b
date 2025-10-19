```json
{
  "id": "b4e573eb48d8ccb8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286486,
  "host_pid": "9e6742732c60:1",
  "hash": "7beb7690736d6307cf2a51ed158ffd80bbd75f3837a614520ab8b5faff62ef5e",
  "cid": "QmV17beb7690736d6307cf2a51ed158ffd80bbd75f38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286486,
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
      "evaluated_at": 1760286486
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "4eb298385441ecc521e63cd4b69822e56f9e9164f3729fea5740c82ca7b2641e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000242021792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11639808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285763, 'matching_hash': '6b62929422267286'}}}