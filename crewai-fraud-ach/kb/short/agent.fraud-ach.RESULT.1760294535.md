```json
{
  "id": "386c41d5122af2b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294535,
  "host_pid": "9e6742732c60:1",
  "hash": "660a0facdd3e1da7cb72b63b2e7e1d6af719e04af76c57b01162388b89385283",
  "cid": "QmV1660a0facdd3e1da7cb72b63b2e7e1d6af719e04a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294535,
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
      "evaluated_at": 1760294536
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
  "sig": "cca2cda406e773e986929e272054eaef55400136136cda7e0b10fa5178bc7b9c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592077072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 56133360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '86add4fc1587ca1b'}}}