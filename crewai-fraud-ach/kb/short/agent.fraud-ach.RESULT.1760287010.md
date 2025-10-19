```json
{
  "id": "a07227ef591dcecc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287010,
  "host_pid": "9e6742732c60:1",
  "hash": "0462790cdc7cbcde446372bbc3c02cdc6827e2312f6f1ff5d0da0cdd7df0e588",
  "cid": "QmV10462790cdc7cbcde446372bbc3c02cdc6827e231",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287010,
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
      "evaluated_at": 1760287010
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
  "sig": "339c77d7b464492d5a061b4b88d78c2a7c28e958f2af9c3b55a864e40d4ec783"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009597385398
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10994715, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285763, 'matching_hash': '354842811986f77e'}}}