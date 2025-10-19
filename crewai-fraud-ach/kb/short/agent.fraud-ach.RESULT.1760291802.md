```json
{
  "id": "244b3fe890d6366e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291802,
  "host_pid": "9e6742732c60:1",
  "hash": "b3d04780ca336b46f214f61b9933de991159820d4bcdea4fe6c27d91c8e4fc1c",
  "cid": "QmV1b3d04780ca336b46f214f61b9933de991159820d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291802,
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
      "evaluated_at": 1760291802
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
  "sig": "0b7d67541e191252077a508fdc3cac18936b79924e3bc8537d2ff3187f71c4e5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246182467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 59178357, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285765, 'matching_hash': '281ac37534aaceb9'}}}