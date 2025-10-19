```json
{
  "id": "d1b33c831e9ee06a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288341,
  "host_pid": "9e6742732c60:1",
  "hash": "57d90033a5ff52077022bec600e309a9f64ea68e81f2ea0364ec7cf592907e89",
  "cid": "QmV157d90033a5ff52077022bec600e309a9f64ea68e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288341,
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
      "evaluated_at": 1760288341
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
  "sig": "cc0cc72dd3a2e5dcd9f6a60d5d0b34544afa5f2b637b66114ee53223b470ad14"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027918613
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 10241280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285764, 'matching_hash': 'c11d1385920c0a28'}}}