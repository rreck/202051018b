```json
{
  "id": "95c57310df6197ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292798,
  "host_pid": "9e6742732c60:1",
  "hash": "689b04c5acb7ffcbcd254bcf0a009f692eb2d6afe06e36d345fc0628fdb1a8e7",
  "cid": "QmV1689b04c5acb7ffcbcd254bcf0a009f692eb2d6af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292798,
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
      "evaluated_at": 1760292798
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
  "sig": "ed7151d0f593b065fcee7d967e4e4e91108f750df70980d7de74884ccc560af9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272268645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 90263755, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285765, 'matching_hash': '088fbc730f5432fe'}}}