```json
{
  "id": "9297bc536ab9a2b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288671,
  "host_pid": "9e6742732c60:1",
  "hash": "564240c1ad8431fbff6c251e48014660a5ad71d40e838893fd86c5a83142f9cb",
  "cid": "QmV1564240c1ad8431fbff6c251e48014660a5ad71d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288671,
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
      "evaluated_at": 1760288671
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
  "sig": "f9863d0fb4ae5abb32d092b223b7c828e0ff820eaa6c6f1f4e72d78980251a48"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592096226
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 49362200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285765, 'matching_hash': '5e92eb8585c87013'}}}