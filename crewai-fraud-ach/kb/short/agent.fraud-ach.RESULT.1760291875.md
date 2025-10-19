```json
{
  "id": "92b068e15a1d9034",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291875,
  "host_pid": "9e6742732c60:1",
  "hash": "59c781d1405cb1ecd31129c5d0dd7f7c3c6217b2da3f079411e19f5e4f69bdfd",
  "cid": "QmV159c781d1405cb1ecd31129c5d0dd7f7c3c6217b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291875,
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
      "evaluated_at": 1760291875
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
  "sig": "d60e4941b73f9c3bec411104ebd500b2613fd20274e596866d57b07f5a13050d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272056474
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': 'eb54a2a49d3a706d'}}} 1760285763, 'matching_hash': '38dcdd2f540d89c1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}