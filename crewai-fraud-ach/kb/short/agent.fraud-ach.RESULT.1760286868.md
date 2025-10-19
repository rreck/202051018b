```json
{
  "id": "eea90f567bdc8fa6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286868,
  "host_pid": "9e6742732c60:1",
  "hash": "dcdcb5808a21ede56442a928889d82cb7216e3beef328b36adcbc5b533ecb944",
  "cid": "QmV1dcdcb5808a21ede56442a928889d82cb7216e3be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286868,
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
      "evaluated_at": 1760286868
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
  "sig": "8d7be76ad816cf33c724045661c650e3fff862ba3e86358ac230def27ed23f8d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009591103574
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18711000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285763, 'matching_hash': 'b913753ac5280baa'}}}