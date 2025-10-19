```json
{
  "id": "e1a8e1c30bcffe58",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291455,
  "host_pid": "9e6742732c60:1",
  "hash": "ef6e636ffbce2bd3334f12f54eab2bfbb30037028ef46b0b116dbdc8981d5b40",
  "cid": "QmV1ef6e636ffbce2bd3334f12f54eab2bfbb3003702",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291455,
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
      "evaluated_at": 1760291455
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
  "sig": "2ad0ce51140494aa27b48ff596c35e44598be07037fa7f0b6c60c1f8423feaea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463568898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 52354225, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285764, 'matching_hash': '8016b691bce48ab1'}}}