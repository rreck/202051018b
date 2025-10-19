```json
{
  "id": "3bec7ef61d4ebbb8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288237,
  "host_pid": "9e6742732c60:1",
  "hash": "3d4bf2ec622911aa0fde2e8508aae22c007947d8e93fe1a0bb76d7ebeb6b3b82",
  "cid": "QmV13d4bf2ec622911aa0fde2e8508aae22c007947d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288237,
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
      "evaluated_at": 1760288237
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
  "sig": "579bf0e7957dc6678dd2d6af83e33bf87a5bfa65c75f27e82ad78c4c969bffda"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248255202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 35072397, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285764, 'matching_hash': 'c66fc0c5e7caab92'}}}