```json
{
  "id": "57ad9ace25f29a65",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291885,
  "host_pid": "9e6742732c60:1",
  "hash": "6da1059cf8d3c51d273d9ffd72f6485ef37cc9b6361363b563d89e7ee6483b99",
  "cid": "QmV16da1059cf8d3c51d273d9ffd72f6485ef37cc9b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291885,
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
      "evaluated_at": 1760291886
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
  "sig": "497e917c8897ab3b392072de1d5892b99c3a249acbf9cd3b321a9d971ca979ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241978752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 41366555, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285765, 'matching_hash': '600b54b59692179b'}}}