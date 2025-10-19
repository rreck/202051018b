```json
{
  "id": "ff5c0e2061afa42e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286905,
  "host_pid": "9e6742732c60:1",
  "hash": "a4f645fce5db5c2902d1bf308a05ead94ffce16094620737207ed5b36fac0cfa",
  "cid": "QmV1a4f645fce5db5c2902d1bf308a05ead94ffce160",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286905,
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
      "evaluated_at": 1760286905
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
  "sig": "2a36d73633c95c21c0c91c04cf4f7860f8e664f4cb33f1916b05f108930103d0"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039663431
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285764, 'matching_hash': '33f644fe289ea89d'}}}