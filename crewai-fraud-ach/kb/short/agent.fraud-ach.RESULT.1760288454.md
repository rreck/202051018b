```json
{
  "id": "8a27f502dbd4e86e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288454,
  "host_pid": "9e6742732c60:1",
  "hash": "60c6dab1a018f5c3ab5dbb9d93985dce7896dc75263c200046026f99826558e6",
  "cid": "QmV160c6dab1a018f5c3ab5dbb9d93985dce7896dc75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288454,
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
      "evaluated_at": 1760288454
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
  "sig": "0fce3a0a4f852e9939cc753023fdd3a6225197f218271e33e1ecd0c3247c28b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244267355
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 14133840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '9a2cfa03d6a38585'}}}