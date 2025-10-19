```json
{
  "id": "11cc2e28dbaa9489",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288152,
  "host_pid": "9e6742732c60:1",
  "hash": "ab159974ef976021e49d8d56d1ffc3cd1bc5cb8774450a94ba49ec4b191579c3",
  "cid": "QmV1ab159974ef976021e49d8d56d1ffc3cd1bc5cb87",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288152,
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
      "evaluated_at": 1760288152
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
  "sig": "9741c90db44744b7d693659bbfcbfb2d36544a6eaaa52d5c628365d467e3be1a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594283807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 16931964, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285764, 'matching_hash': 'e41bbca7fc0ba663'}}}