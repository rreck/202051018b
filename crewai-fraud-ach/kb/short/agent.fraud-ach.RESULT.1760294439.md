```json
{
  "id": "ca7c5e1eb995d605",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294439,
  "host_pid": "9e6742732c60:1",
  "hash": "601d94912d510c4e8a077a296eb74ebf0522c956adbd0fd23e1d16b71d1b4385",
  "cid": "QmV1601d94912d510c4e8a077a296eb74ebf0522c956",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294439,
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
      "evaluated_at": 1760294439
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
  "sig": "1e76a72b4b3b54759059d7a407f0124400385aef362c3aa8d2cd13f902323030"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244875332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 78101366, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '627c737035c8c8c8'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}