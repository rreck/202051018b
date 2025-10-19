```json
{
  "id": "ea8057e94e004f2f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289789,
  "host_pid": "9e6742732c60:1",
  "hash": "d694eca566051b7ef3d0af07038e0ce052b38ed946bd28e87d89580c95996884",
  "cid": "QmV1d694eca566051b7ef3d0af07038e0ce052b38ed9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289789,
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
      "evaluated_at": 1760289789
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
  "sig": "20aade238f5c9d9b4d1709e3d91bdbf887c5566d19507d5c3a174d198921333e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274546383
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 35189140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': '76da04c5629ac502'}}}