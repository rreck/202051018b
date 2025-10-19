```json
{
  "id": "d7dea2a91dca4c46",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288492,
  "host_pid": "9e6742732c60:1",
  "hash": "df4e19fa1040aa40bf550c40f054093414e1116abe9ddffd7600ad793cc7a41e",
  "cid": "QmV1df4e19fa1040aa40bf550c40f054093414e1116a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288492,
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
      "evaluated_at": 1760288492
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
  "sig": "68ee5d6a7d67978707cf3b9f1611d925679b14e5d30def77901183647e6c877e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023914154
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 45441160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285764, 'matching_hash': '45ff85674ff7fdbe'}}}