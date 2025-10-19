```json
{
  "id": "217666926d9a60d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289841,
  "host_pid": "9e6742732c60:1",
  "hash": "e9f037e8c60ffff3351a865203bd863ff8ce878acb8c0f48306876d11b0a4085",
  "cid": "QmV1e9f037e8c60ffff3351a865203bd863ff8ce878a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289841,
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
      "evaluated_at": 1760289841
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
  "sig": "846324bd7626a44662e7766f51de6934bc8f769e4d0127492872cc44dcfb86d7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020143117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 33500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285765, 'matching_hash': '83c798d1c8d9cfec'}}}