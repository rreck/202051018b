```json
{
  "id": "30a3be521d3f4613",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289498,
  "host_pid": "9e6742732c60:1",
  "hash": "9b296648c717715389ccc05b69e09d7c04bb8e995a0b7e87994286526c74ef61",
  "cid": "QmV19b296648c717715389ccc05b69e09d7c04bb8e99",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289498,
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
      "evaluated_at": 1760289498
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
  "sig": "5fbc1ba5bc0728cd20127c46c9a2fb3159b052aafe16aea06955aeb26113853f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029379143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 60841250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': '781972e95177ec49'}}}