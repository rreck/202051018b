```json
{
  "id": "15a76548040aa082",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289570,
  "host_pid": "9e6742732c60:1",
  "hash": "8d58686410fecf035d79c0b66db8b373d6a25203350fae4aa10ba4bcc3acfbbc",
  "cid": "QmV18d58686410fecf035d79c0b66db8b373d6a25203",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289570,
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
      "evaluated_at": 1760289570
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
  "sig": "06dc9d96aecca35ee8ad36d9df9e43135e0a242c0d63493f2e02ecdefd953c4a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159610548
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 41403905, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285764, 'matching_hash': '505487b98e445d12'}}}