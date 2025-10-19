```json
{
  "id": "cd261092e1033c52",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289378,
  "host_pid": "9e6742732c60:1",
  "hash": "bd3153b86d79e5082d95b3eef9c854d7822a58b83a9448d04bb995525a7cecf9",
  "cid": "QmV1bd3153b86d79e5082d95b3eef9c854d7822a58b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289378,
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
      "evaluated_at": 1760289378
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
  "sig": "febb6d3c78069548250293cb4730c387376f5b840d3add948f73a0e75ec59bc3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 38508008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}