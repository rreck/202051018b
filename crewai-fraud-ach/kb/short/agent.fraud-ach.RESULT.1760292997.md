```json
{
  "id": "1a9aa2578fc8d72c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292997,
  "host_pid": "9e6742732c60:1",
  "hash": "07218c9496d5d8d0439b455522037d15a4836f3ec52f4611314ae85ee7bc4f17",
  "cid": "QmV107218c9496d5d8d0439b455522037d15a4836f3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292997,
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
      "evaluated_at": 1760292997
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
  "sig": "8cd3c9fe3af5cbdfaa7df4a7e8a7a5dee275b276ea2901dad59fb23ed4e2be62"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029513246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 10586268, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285764, 'matching_hash': '556e5d87a3998e0a'}}}