```json
{
  "id": "faaf2dd6b9ef9512",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290266,
  "host_pid": "9e6742732c60:1",
  "hash": "4d478b6838f5b60bc2307d30d219c2227c51cae4d56aefde73b41af1a4c289f8",
  "cid": "QmV14d478b6838f5b60bc2307d30d219c2227c51cae4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290266,
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
      "evaluated_at": 1760290266
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
  "sig": "b8b432a66d027a237d754143f8493782228f9593db6889e7c9df8a52d51a1921"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271295485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 55685276, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': '1c5bb12c0a4cbea7'}}}