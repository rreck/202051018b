```json
{
  "id": "06938544b4dcfe8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291876,
  "host_pid": "9e6742732c60:1",
  "hash": "bbf542f3846230d97b6e288d31b1882ec5f112613b66f6baa8e8b2e6adddf5e3",
  "cid": "QmV1bbf542f3846230d97b6e288d31b1882ec5f11261",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291876,
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
      "evaluated_at": 1760291876
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
  "sig": "25a2d6fc85e6616cbe92ac082dc1f688fd516e116c6a59a31feb6a3f8a4b403a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020823686
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 11505890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285764, 'matching_hash': '810bf9913cbceac2'}}}