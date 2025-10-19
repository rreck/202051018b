```json
{
  "id": "5fa5eebea3078c03",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294816,
  "host_pid": "9e6742732c60:1",
  "hash": "23b9e511d4f8f01701d57d7635deaaa187ed1ca6ac91d20245644e225fd24e9a",
  "cid": "QmV123b9e511d4f8f01701d57d7635deaaa187ed1ca6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294816,
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
      "evaluated_at": 1760294816
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
  "sig": "7dbceb0a06776e6fb54c41b6e3587aa127cff27daf9ae8a36e383e60e19f8954"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027669266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 20362685, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285764, 'matching_hash': 'fbd07eed8562f9d2'}}}