```json
{
  "id": "f85c8eebdce6e118",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286151,
  "host_pid": "9e6742732c60:1",
  "hash": "abe3b97a90e91ba90006159e798949c629fa6b30d9b6bd16ffd76119f45a35e2",
  "cid": "QmV1abe3b97a90e91ba90006159e798949c629fa6b30",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286151,
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
      "evaluated_at": 1760286151
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
  "sig": "46dcd8412ae965c9981cef13726796d9863db93c155aa9ec653f24f3cba73f3b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270910087
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285763, 'matching_hash': '020bc3c8298f3eb9'}}}