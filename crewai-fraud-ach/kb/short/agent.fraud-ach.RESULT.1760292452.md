```json
{
  "id": "d071f1fdfeecaabb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292452,
  "host_pid": "9e6742732c60:1",
  "hash": "b78aca3f82034a7ad6d23420573ef1091d0d2ade4214b6d71dc9a064efb3319d",
  "cid": "QmV1b78aca3f82034a7ad6d23420573ef1091d0d2ade",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292452,
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
      "evaluated_at": 1760292452
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
  "sig": "e98a00dd8095c7bd03258f5c22a3394c5d7ad9de7f99fafae5782b9b556bd2bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154405665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 95434812, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': '36d51f87c7d176f1'}}}