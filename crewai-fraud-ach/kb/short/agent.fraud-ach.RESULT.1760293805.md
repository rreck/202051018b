```json
{
  "id": "e1a9c1e304e5a109",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293805,
  "host_pid": "9e6742732c60:1",
  "hash": "64f54986168fdf134085d8e49c32381b3378b0e2f03b7f8dc403fddbfb769928",
  "cid": "QmV164f54986168fdf134085d8e49c32381b3378b0e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293805,
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
      "evaluated_at": 1760293805
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
  "sig": "fec647293f006bd5e20cb7fae9db7293e363d22ab7c24050e8e849d7cb016f86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027419247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 106179546, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': 'f49fdb64c00c5aec'}}}