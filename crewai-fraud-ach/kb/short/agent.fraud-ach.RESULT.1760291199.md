```json
{
  "id": "29e082fef615d17a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291199,
  "host_pid": "9e6742732c60:1",
  "hash": "35b8e49f9bd5d5e9c2110e8d451e48e4c03b5855cd432af07754c796ef6f3687",
  "cid": "QmV135b8e49f9bd5d5e9c2110e8d451e48e4c03b5855",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291199,
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
      "evaluated_at": 1760291199
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
  "sig": "1c679d40c3ad8297807aa360268b93a9106bfb5827827883692c6d2fa4f0c9dd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599036440
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 67420184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285765, 'matching_hash': '93c00e1af0416a0b'}}}