```json
{
  "id": "5597fd0ed8a98a7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294682,
  "host_pid": "9e6742732c60:1",
  "hash": "a90fdca405fe041c40b7da515571f2afe6769d5da9a3a2d441df439a51106bb4",
  "cid": "QmV1a90fdca405fe041c40b7da515571f2afe6769d5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294682,
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
      "evaluated_at": 1760294682
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
  "sig": "28c9644b3986b9ace53b34a282e415fc3da1b07e47db75f52a5bd0fa147d35ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465822757
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 109553158, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285765, 'matching_hash': '1a67314a077331d2'}}}