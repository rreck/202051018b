```json
{
  "id": "6524fcd8de486dbf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286892,
  "host_pid": "9e6742732c60:1",
  "hash": "efd448aeb3e248353b2da00cb186c82e0138638b4bff87006eaa54dec6396802",
  "cid": "QmV1efd448aeb3e248353b2da00cb186c82e0138638b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286892,
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
      "evaluated_at": 1760286892
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
  "sig": "113de0ee716fdbe8d416de313d3e012c25fe22ab26c8784f5855b72e45921c89"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000020723596
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285763, 'matching_hash': 'ee402fb1f2eea4ea'}}}