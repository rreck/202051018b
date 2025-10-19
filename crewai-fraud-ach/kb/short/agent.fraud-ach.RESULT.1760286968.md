```json
{
  "id": "62621ff43cf67fdc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286968,
  "host_pid": "9e6742732c60:1",
  "hash": "b8d2647734a80ff54c96f3fc6b493cfb44d51b7e1d77c9c57644fd0b785547bf",
  "cid": "QmV1b8d2647734a80ff54c96f3fc6b493cfb44d51b7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286968,
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
      "evaluated_at": 1760286968
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
  "sig": "67447d7c7eb47b668957c7cc3a0957e6774f9d1f02664117a0efc5d111b04099"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13684664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}