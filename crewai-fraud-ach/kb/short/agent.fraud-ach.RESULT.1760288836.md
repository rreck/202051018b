```json
{
  "id": "446024b078a2ff40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288836,
  "host_pid": "9e6742732c60:1",
  "hash": "42188eba980406c0e4517356d7bd41716aa52c5b146eb3b8e88420c2744d9be1",
  "cid": "QmV142188eba980406c0e4517356d7bd41716aa52c5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288836,
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
      "evaluated_at": 1760288836
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
  "sig": "80a3d7f6781188bbce110cd12bc69c36b06eaed822083358b75fa06bc69397a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035927231
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 48710865, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285765, 'matching_hash': '0aeb814485d84e75'}}}