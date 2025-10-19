```json
{
  "id": "eaf1375414e8232f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293988,
  "host_pid": "9e6742732c60:1",
  "hash": "8ec061463e1b69b69eaa3a977e4be28ac84c5921d86c66d66bdc471dc255dd0b",
  "cid": "QmV18ec061463e1b69b69eaa3a977e4be28ac84c5921",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293988,
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
      "evaluated_at": 1760293988
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
  "sig": "fe365184503b16b2bdd05dbe021a2b2d3ea3035c0b5a8e6328ed5d0a9324a844"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038907358
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 49526975, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285764, 'matching_hash': '4f1b5532b664e41d'}}}