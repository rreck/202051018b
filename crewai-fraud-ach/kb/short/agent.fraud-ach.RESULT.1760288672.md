```json
{
  "id": "69032c2246383a61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288672,
  "host_pid": "9e6742732c60:1",
  "hash": "e765886eefd74403b6aba7327ccb4dd6caea822cacbe3d58496cc34cfa18d15e",
  "cid": "QmV1e765886eefd74403b6aba7327ccb4dd6caea822c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288672,
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
      "evaluated_at": 1760288672
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
  "sig": "a4c12808b9593aebca4c3950feff2a9c94b12b25a52137b0846a8ce9b4a5648a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151005829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 27057400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285765, 'matching_hash': 'ea26f24e3d1967f5'}}}