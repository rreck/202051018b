```json
{
  "id": "87923ba204ade6e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285310,
  "host_pid": "9e6742732c60:1",
  "hash": "a1ea6e4dbbb81433943659fdbd41ecebca0f1d93733e573c18b61f6c7f8b32a3",
  "cid": "QmV1a1ea6e4dbbb81433943659fdbd41ecebca0f1d93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285310,
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
      "evaluated_at": 1760285310
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
  "sig": "61a9e9cc77d08ed5050698729c195e00b7b53dec738e546244263b0849bd22b2"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13906002, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}