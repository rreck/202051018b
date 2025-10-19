```json
{
  "id": "c526ed57b1b46d37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292437,
  "host_pid": "9e6742732c60:1",
  "hash": "76cb56174d684c11669059a317645e26606c66de429fdd75de9321521e0cd248",
  "cid": "QmV176cb56174d684c11669059a317645e26606c66de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292437,
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
      "evaluated_at": 1760292437
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
  "sig": "bd86040e11f1c33175915b1d7eb7ba35a2ec2231efe76a373d7871b2363af9c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 62694856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}