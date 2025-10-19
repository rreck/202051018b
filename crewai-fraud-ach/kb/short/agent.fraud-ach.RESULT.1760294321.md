```json
{
  "id": "6838f5d5dddf4727",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294321,
  "host_pid": "9e6742732c60:1",
  "hash": "14785d886fa1efd6be73ee8c61028abf8b1ea0dd7b4b6157ada5a396807b6acc",
  "cid": "QmV114785d886fa1efd6be73ee8c61028abf8b1ea0dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294321,
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
      "evaluated_at": 1760294321
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
  "sig": "c951430b1adc8e84f10df53061b06a1888978652b280ab194efa57737eb194a0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270133099
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 90987440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '05f0f8ce03828c9b'}}}