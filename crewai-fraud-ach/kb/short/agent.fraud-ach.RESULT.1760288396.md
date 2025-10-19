```json
{
  "id": "ffbf5e5b9c3d711f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288396,
  "host_pid": "9e6742732c60:1",
  "hash": "bda8d90756b4eecbcfad46ad83d417915c990b47abd7d066fc698843da6cc209",
  "cid": "QmV1bda8d90756b4eecbcfad46ad83d417915c990b47",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288396,
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
      "evaluated_at": 1760288396
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
  "sig": "8c18c7af1949c310bd55bd27ce9aa62b35148d6a1037b146e54046875e6aeb87"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465124688
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 15138876, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285763, 'matching_hash': 'c4099eb9aeb13a11'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}