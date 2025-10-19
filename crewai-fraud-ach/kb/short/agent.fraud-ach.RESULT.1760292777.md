```json
{
  "id": "b1927981062dbf23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292777,
  "host_pid": "9e6742732c60:1",
  "hash": "cd03992ce70852f600dfb167ab79b8c86dbf23e16b881f399154dc0292920303",
  "cid": "QmV1cd03992ce70852f600dfb167ab79b8c86dbf23e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292777,
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
      "evaluated_at": 1760292777
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
  "sig": "684f549633b2b829a7ded2da461f749ef8838d362cf1a23eadbbf6ff9e4f7831"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460168239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 16865145, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': 'c8b812a49265f53e'}}}