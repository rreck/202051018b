```json
{
  "id": "670a3ee084e541e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291983,
  "host_pid": "9e6742732c60:1",
  "hash": "1d3c1e26366a7fa080d9148f807fe000d3949ff390c69cd624d63421da686dcc",
  "cid": "QmV11d3c1e26366a7fa080d9148f807fe000d3949ff3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291983,
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
      "evaluated_at": 1760291983
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
  "sig": "0870bde29b3e1272dd214e0607d47989e652d0ebc622262209addd0df63d445d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151005829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 50597338, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285765, 'matching_hash': 'ea26f24e3d1967f5'}}}