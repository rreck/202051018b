```json
{
  "id": "982fa09ecd982187",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294630,
  "host_pid": "9e6742732c60:1",
  "hash": "62558a2f79e4a110e248da4b3b1f2c8c82e07cb40876295b20d98ca58ee45c8f",
  "cid": "QmV162558a2f79e4a110e248da4b3b1f2c8c82e07cb4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294630,
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
      "evaluated_at": 1760294630
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
  "sig": "c4105ab3cf909ed41b5a1659749719a296acf5be3960abb09aab8d573f15a787"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 76697768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}