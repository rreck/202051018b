```json
{
  "id": "a75a196f97d63116",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288895,
  "host_pid": "9e6742732c60:1",
  "hash": "9db6973e8a5427589b206c95614ae9b28898426701e0cb1871b20e4bdeb8ce1b",
  "cid": "QmV19db6973e8a5427589b206c95614ae9b288984267",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288895,
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
      "evaluated_at": 1760288895
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
  "sig": "27304f9da512a8f18b8fe387e2d05fc47e65d80cebc0c39583ce80de2b79b5c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154990255
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 13268642, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': '800f0de895a214ba'}}}