```json
{
  "id": "c8cdfbac4ceec95f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287265,
  "host_pid": "9e6742732c60:1",
  "hash": "c673fb2145ad7407b9bbf1847921ba70ca090f5ef078ba0f13e1790b2947223b",
  "cid": "QmV1c673fb2145ad7407b9bbf1847921ba70ca090f5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287265,
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
      "evaluated_at": 1760287265
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "a700bc42770c4e61ad03e6e1157b74c886d20407c7b5279a82aad540825731dc"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000030478037
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 11645640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285763, 'matching_hash': 'a92b61c306bd8c34'}}}