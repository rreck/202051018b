```json
{
  "id": "45053d8988a32b89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292504,
  "host_pid": "9e6742732c60:1",
  "hash": "dad8685ca0620f71e7cde7869520f020ab16db8d33b6518585cc7046f87d6515",
  "cid": "QmV1dad8685ca0620f71e7cde7869520f020ab16db8d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292504,
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
      "evaluated_at": 1760292504
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
  "sig": "7e80962c48d410eed9a1c2820b252d968f63f9c06bbb823a1f4969f977c4e32c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469045536
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 68226951, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': 'd92613c41315e1ec'}}}