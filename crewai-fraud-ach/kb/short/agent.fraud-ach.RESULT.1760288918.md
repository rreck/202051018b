```json
{
  "id": "ef285376f443160a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288918,
  "host_pid": "9e6742732c60:1",
  "hash": "03590bd74b866d06fe988000c3fa47972973c13640c24d1672ec3e79809aa026",
  "cid": "QmV103590bd74b866d06fe988000c3fa47972973c136",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288918,
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
      "evaluated_at": 1760288918
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
  "sig": "164a181998809094463dd211eea9a6d6aa62b7e723d215e6af249d035b838e77"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465523405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 31609764, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285764, 'matching_hash': '5adc701fe9b49cb3'}}}