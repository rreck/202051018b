```json
{
  "id": "9935e5807aa29f76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288475,
  "host_pid": "9e6742732c60:1",
  "hash": "f433a806e5dc1a6b522d33b86adbfc0bb268b1c2203dd54d9935eef281f795cb",
  "cid": "QmV1f433a806e5dc1a6b522d33b86adbfc0bb268b1c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288475,
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
      "evaluated_at": 1760288475
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
  "sig": "adc056a1915f0dba03cea9abd57af78f969de76480053e4439fc7797ecc11462"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599169809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 27400248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285765, 'matching_hash': '606495659f158f1b'}}}