```json
{
  "id": "73d73e33b86fe8aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290314,
  "host_pid": "9e6742732c60:1",
  "hash": "fa4d12faa2b6e0c6ae52ca110830b7a963532cfc579279b01beff08a4a6eed4b",
  "cid": "QmV1fa4d12faa2b6e0c6ae52ca110830b7a963532cfc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290314,
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
      "evaluated_at": 1760290314
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
  "sig": "ead7f741fb9a3cf6a24ba4a517fa7a8155f986c10a02b82906b8378b3c406ec8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152772165
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 42719082, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285764, 'matching_hash': '9371db7725d4e0a9'}}}