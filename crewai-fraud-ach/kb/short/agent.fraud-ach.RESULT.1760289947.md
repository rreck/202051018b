```json
{
  "id": "01a5adfac6d7e14b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289947,
  "host_pid": "9e6742732c60:1",
  "hash": "0c4bdc3660640ccb3d0ebffecf7b8a5f7950d4980cfa41928f75c61aa9a4069b",
  "cid": "QmV10c4bdc3660640ccb3d0ebffecf7b8a5f7950d498",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289947,
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
      "evaluated_at": 1760289947
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
  "sig": "c27994d77ded9305fe6bfb8e255f013d45f9281a97e2b00376114e55f4b792cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248125638
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 60764843, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285764, 'matching_hash': '28ad2138639324d3'}}}