```json
{
  "id": "a9159168d2d5c886",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291436,
  "host_pid": "9e6742732c60:1",
  "hash": "788c6804e8817e59f0c0c57434a64fba4a1ae72a1f154e57272e023cbd744425",
  "cid": "QmV1788c6804e8817e59f0c0c57434a64fba4a1ae72a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291436,
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
      "evaluated_at": 1760291436
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
  "sig": "734127d90be258a139bc84bfb9b3c4179a09a3c63dae1980af315a9f94222e71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154437530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 60554550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '1df4316d53c749d8'}}}