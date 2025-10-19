```json
{
  "id": "13ad0646ff9fa78e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288339,
  "host_pid": "9e6742732c60:1",
  "hash": "4c15a286813188936bb70f25cec3eedd5f4e9f563abbac7d40050b5eca954736",
  "cid": "QmV14c15a286813188936bb70f25cec3eedd5f4e9f56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288339,
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
      "evaluated_at": 1760288339
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
  "sig": "0ee5e12d6f1145601f84485f9cce753713dd411a8aa832fc5eb9566b1662c7f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025121499
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 11449170, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285763, 'matching_hash': 'a696ea0f650f1de2'}}}