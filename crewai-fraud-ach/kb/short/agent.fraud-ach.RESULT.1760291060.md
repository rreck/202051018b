```json
{
  "id": "ab32e60d528cbc20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291060,
  "host_pid": "9e6742732c60:1",
  "hash": "049035708f5ba066746d1a3afebb7f80123d9bd59f0852ee03b083888bbdb08d",
  "cid": "QmV1049035708f5ba066746d1a3afebb7f80123d9bd5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291060,
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
      "evaluated_at": 1760291060
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
  "sig": "47f8e9d573ecb745e8b437023164e2fd29c696997c08aad051dd9245cadef242"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247599870
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 52741686, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285764, 'matching_hash': '3d46d1edc4f67bfe'}}}