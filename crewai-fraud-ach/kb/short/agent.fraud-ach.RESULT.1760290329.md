```json
{
  "id": "c7b81aea92fc5cf0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290329,
  "host_pid": "9e6742732c60:1",
  "hash": "230d9c04cdc62e32e27207ff86c772ce00058489bd6f1531edad5b7d68ee25eb",
  "cid": "QmV1230d9c04cdc62e32e27207ff86c772ce00058489",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290329,
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
      "evaluated_at": 1760290329
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
  "sig": "4a558587f29bae30e6c67e6740f4a3f58efa4f09768a2d47b42e4d1b2a1900cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274128098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 60977952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285765, 'matching_hash': 'e67ed82943972fb3'}}}