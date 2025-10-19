```json
{
  "id": "14086b650d9e1bd4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288502,
  "host_pid": "9e6742732c60:1",
  "hash": "0ce1bb6a1e21256719e8e2decd24c26fc82478c4a0115811c5a5efa4fac1c133",
  "cid": "QmV10ce1bb6a1e21256719e8e2decd24c26fc82478c4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288502,
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
      "evaluated_at": 1760288502
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
  "sig": "ffeea7c8ccd7dcf3061b3b9be8328e2b0d0887bda5515848685ad1daef64204c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029964192
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 28823475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}