```json
{
  "id": "d0f19b88e93ab79c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291336,
  "host_pid": "9e6742732c60:1",
  "hash": "684ec4698c607502f81052a0fb3b100f0fa971ec10a2cacb397cb225cc4824f6",
  "cid": "QmV1684ec4698c607502f81052a0fb3b100f0fa971ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291336,
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
      "evaluated_at": 1760291336
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
  "sig": "beab297cc542a6b0e0c3b348342b467a42301994884a1c7a76a347d70f0f8884"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 54738656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}