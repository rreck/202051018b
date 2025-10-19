```json
{
  "id": "69217e904d2ef758",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291040,
  "host_pid": "9e6742732c60:1",
  "hash": "2156cec33d253f9dcc0da5f81d4bc56803b56beb2fa26c83f0a5df63c4e84cab",
  "cid": "QmV12156cec33d253f9dcc0da5f81d4bc56803b56beb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291040,
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
      "evaluated_at": 1760291040
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
  "sig": "7972a6ad1ab0afe27ec4d6888359f925a4a135710a40ac86fe9ad87c9ed93f1c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155958228
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 69554430, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285765, 'matching_hash': '1e57f627a6d207f5'}}}