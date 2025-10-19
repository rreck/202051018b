```json
{
  "id": "b650bed4e7567167",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289750,
  "host_pid": "9e6742732c60:1",
  "hash": "2639c54f2d8f953703285f956ace968eefa377441e25727f1e207601d49e4a09",
  "cid": "QmV12639c54f2d8f953703285f956ace968eefa37744",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289750,
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
      "evaluated_at": 1760289750
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
  "sig": "83b930fe91bf9b4abd7ccb040a4636faa5e84a71be8d45c51e956f26d47d1734"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154361187
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 33000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285764, 'matching_hash': 'a57b8c5e7960514a'}}}