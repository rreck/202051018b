```json
{
  "id": "d426497bb51a8741",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290774,
  "host_pid": "9e6742732c60:1",
  "hash": "904c205d30490c5e697bbe376db755cf8837237cc3c6aebde8c209ce6103a85b",
  "cid": "QmV1904c205d30490c5e697bbe376db755cf8837237c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290774,
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
      "evaluated_at": 1760290774
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
  "sig": "79f2e9631dcc86d487151370dd793675f3e4e9cf584d476a0cebe51a63db5a5f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243793866
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 34586316, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': '3f378333472d9dcb'}}}