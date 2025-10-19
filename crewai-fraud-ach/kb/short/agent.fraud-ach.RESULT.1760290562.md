```json
{
  "id": "00a7265cc874a931",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290562,
  "host_pid": "9e6742732c60:1",
  "hash": "7f686958f2e62c7caeedb7fba13fd363e3ffd5a7db37c05b5274f4f364f7e561",
  "cid": "QmV17f686958f2e62c7caeedb7fba13fd363e3ffd5a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290562,
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
      "evaluated_at": 1760290562
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
  "sig": "3c4194453d7c9c43e4d83d646b2235429080803b61a38c82b8515de37a8d58a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 48691944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}