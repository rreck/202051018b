```json
{
  "id": "aab9877683f2595a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292203,
  "host_pid": "9e6742732c60:1",
  "hash": "103d2934b09cb61d8379a77054676fff7763b3d9c2527477c920d22844753ad8",
  "cid": "QmV1103d2934b09cb61d8379a77054676fff7763b3d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292203,
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
      "evaluated_at": 1760292203
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
  "sig": "2e0214f8780dd6efd14004fbc3b3c70a5d31f8d2f15238cab98ef743ff08cf7d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246182467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 62088768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285765, 'matching_hash': '281ac37534aaceb9'}}}