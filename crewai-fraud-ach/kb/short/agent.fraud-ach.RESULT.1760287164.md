```json
{
  "id": "13aca97ec98f38c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287164,
  "host_pid": "9e6742732c60:1",
  "hash": "923b0cdf110cd4ebe9c1304d08a46f8e818a3411be26265ce43844d9fa47faad",
  "cid": "QmV1923b0cdf110cd4ebe9c1304d08a46f8e818a3411",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287164,
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
      "evaluated_at": 1760287164
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "e29ecb0d28a0e67df7315601e42472b5e3a4c43d4ff2e2f9fb34b11f8a010a16"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201465368597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12436900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}