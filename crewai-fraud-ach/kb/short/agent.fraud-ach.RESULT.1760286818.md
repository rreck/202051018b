```json
{
  "id": "5cf0971eb647b763",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286818,
  "host_pid": "9e6742732c60:1",
  "hash": "c8ac6885bb22f368c1ec6824fd21d07e1da0796186b06b6d87aa23f3cd0cc652",
  "cid": "QmV1c8ac6885bb22f368c1ec6824fd21d07e1da07961",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286818,
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
      "evaluated_at": 1760286818
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
  "sig": "93418c4a36984f69dc8803914db2dd5e5d24faed91506b848f1a3cd01ad8fcb2"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201463568898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11368346, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285764, 'matching_hash': '8016b691bce48ab1'}}}