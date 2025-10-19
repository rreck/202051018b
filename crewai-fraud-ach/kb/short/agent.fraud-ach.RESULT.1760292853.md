```json
{
  "id": "eceffbef8f743090",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292853,
  "host_pid": "9e6742732c60:1",
  "hash": "ca8e20d1a26aed955171befeb645f19b55f660f4403c131d5de759834934f4ca",
  "cid": "QmV1ca8e20d1a26aed955171befeb645f19b55f660f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292853,
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
      "evaluated_at": 1760292853
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
  "sig": "24e042659f5bd40a36f313880bd82b4b9084c675339f01a9e8805bdfce83ef5d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272414433
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 30866834, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285764, 'matching_hash': 'f489e4bd64364941'}}}