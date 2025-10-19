```json
{
  "id": "38155cd02fb9efea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293786,
  "host_pid": "9e6742732c60:1",
  "hash": "c0f0fc928ffcc3e18f56593b5a3564df6a82f368fb055dd263665d2549d8c7f1",
  "cid": "QmV1c0f0fc928ffcc3e18f56593b5a3564df6a82f368",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293786,
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
      "evaluated_at": 1760293786
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
  "sig": "772d7b9a115c9deb1409263c178750be7588cc19b3b3a5214a658539ed10c8a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 19926900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}