```json
{
  "id": "d9658c364e69272d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291322,
  "host_pid": "9e6742732c60:1",
  "hash": "7509fa1c91e14ec3dc4891ab1cfe063417055d86519700a44347862241f8065d",
  "cid": "QmV17509fa1c91e14ec3dc4891ab1cfe063417055d86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291322,
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
      "evaluated_at": 1760291322
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
  "sig": "1e28242a5d68a96e7bc3a5e703b47d92ea403255e3116256f902787a59e6e3a5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023458666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 248, 'threshold': 50, 'total_amount': 101197144, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 247, 'first_seen': 1760284979, 'matching_hash': 'a7fb9dc83800d725'}}}