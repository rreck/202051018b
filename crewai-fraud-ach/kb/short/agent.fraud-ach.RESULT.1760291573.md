```json
{
  "id": "447b98d987f60f6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291573,
  "host_pid": "9e6742732c60:1",
  "hash": "4214383c66dd001f0ac1b9adbb93167aef056b7ea35925b430256631a9f1836d",
  "cid": "QmV14214383c66dd001f0ac1b9adbb93167aef056b7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291573,
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
      "evaluated_at": 1760291573
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
  "sig": "a823fe2c1d7c9808751bae15b155612bb49255259c3fac75d7df2c104f22056e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026682072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 59839150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285764, 'matching_hash': 'ef2983ea6f6c1303'}}}