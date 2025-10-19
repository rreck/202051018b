```json
{
  "id": "aeaa6aa69ce9a4ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291585,
  "host_pid": "9e6742732c60:1",
  "hash": "dbfb24afd4a6825fe2f09773c46c572b1a73540c3a34beb8011e3a4333f9fb6e",
  "cid": "QmV1dbfb24afd4a6825fe2f09773c46c572b1a73540c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291585,
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
      "evaluated_at": 1760291585
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
  "sig": "7c275334cffdbbf74746c620c0086f932f6d41269c13fac3f39acde3901f8a0b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242075877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 22286490, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': '7e39a816a4a44fcc'}}}