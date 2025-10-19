```json
{
  "id": "8b11d292310dcbe7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293720,
  "host_pid": "9e6742732c60:1",
  "hash": "2455ac99ba38afbfe6c1739c94b4ec2586e9865e799df3f9e69efa9c8784eb74",
  "cid": "QmV12455ac99ba38afbfe6c1739c94b4ec2586e9865e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293720,
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
      "evaluated_at": 1760293720
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
  "sig": "eda6201fe636feaf517233775fa326ba119db2e47329dda2b06b94cfea138439"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028058978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 11200000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285764, 'matching_hash': '1bb3ef3babc34591'}}}