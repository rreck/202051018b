```json
{
  "id": "191606ffd45c8313",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291763,
  "host_pid": "9e6742732c60:1",
  "hash": "73ae7891e2cda16f27a6e66070b098a818c0b52873036bb85c39a51ea99c04ed",
  "cid": "QmV173ae7891e2cda16f27a6e66070b098a818c0b528",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291763,
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
      "evaluated_at": 1760291763
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
  "sig": "48e68e3605f2b3c6031448a09a4eb74adcfc32e87a165e243ac386a51f12a107"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151363741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 78882258, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285765, 'matching_hash': 'ec824383c23ded7d'}}}