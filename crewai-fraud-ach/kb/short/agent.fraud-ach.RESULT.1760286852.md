```json
{
  "id": "330323ad9485b131",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286852,
  "host_pid": "9e6742732c60:1",
  "hash": "09da399e33f634e52adc5ce57085eaeec98ac231fc10b3826f870a246f563403",
  "cid": "QmV109da399e33f634e52adc5ce57085eaeec98ac231",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286852,
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
      "evaluated_at": 1760286852
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
  "sig": "75a4edf4359ec74b4b4fcdaf791048a5e1bb76df6efff1adb95ff5705166b8ab"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009592096226
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 19251258, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285765, 'matching_hash': '5e92eb8585c87013'}}}