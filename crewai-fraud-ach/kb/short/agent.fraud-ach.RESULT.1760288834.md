```json
{
  "id": "dd97524e1ca5b1da",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288834,
  "host_pid": "9e6742732c60:1",
  "hash": "34a28af4a2f31558882a76d54d508b2ca103aad8457b2d99b4fdc14bcee34a9c",
  "cid": "QmV134a28af4a2f31558882a76d54d508b2ca103aad8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288834,
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
      "evaluated_at": 1760288834
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
  "sig": "1864a492aa8e7642c256c0c4f3dc51998092c2135e8b607a6a8decada3b4241f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038099532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 42149310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285765, 'matching_hash': 'ac68ba9e81a65c72'}}}