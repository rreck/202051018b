```json
{
  "id": "7aa3ef6db6f56862",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287604,
  "host_pid": "9e6742732c60:1",
  "hash": "30718cc34d2abb12c1a0b53905eb275973aa3e64107122b99f228e20a1a91e90",
  "cid": "QmV130718cc34d2abb12c1a0b53905eb275973aa3e64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287604,
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
      "evaluated_at": 1760287604
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
  "sig": "b71820e322cdeb8c2cdf8d62aa056ea387f0551b157329955e49c4b5c28030a0"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 031201461386979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 22416966, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285764, 'matching_hash': '1569de4be841c048'}}}