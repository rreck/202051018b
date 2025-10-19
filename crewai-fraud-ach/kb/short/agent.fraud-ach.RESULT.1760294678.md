```json
{
  "id": "7a7a96fe6240a3cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294678,
  "host_pid": "9e6742732c60:1",
  "hash": "6612ab0cebafe90b5c5cafd45da567479cec21099efbdb556abf0e582dd20ef8",
  "cid": "QmV16612ab0cebafe90b5c5cafd45da567479cec2109",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294678,
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
      "evaluated_at": 1760294678
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
  "sig": "74505d01f3fe3e8e18f62c6a3b0d2dd1ecdeb952d3e537287ec20fe91908cabd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025503816
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 94912400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285765, 'matching_hash': 'fc6cd7074b4844e3'}}}