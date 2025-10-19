```json
{
  "id": "1d9c786fdb2eae68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286329,
  "host_pid": "9e6742732c60:1",
  "hash": "dfabcd769a4e3c3c417d85381d31590282ee414bf5e1327043edf5f25953fdba",
  "cid": "QmV1dfabcd769a4e3c3c417d85381d31590282ee414b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286329,
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
      "evaluated_at": 1760286329
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
  "sig": "82433989906fb0decff019258c3f60b3a90c25fd2e56ddebca1f4057f74d4a96"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156237747
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285763, 'matching_hash': 'b60e159429465bd2'}}}