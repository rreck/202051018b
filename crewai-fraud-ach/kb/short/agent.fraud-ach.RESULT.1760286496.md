```json
{
  "id": "09c9e2a85d280b71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286496,
  "host_pid": "9e6742732c60:1",
  "hash": "5a8534460c8ac82db150fa72dc9dd2ec95a633163ef6ed1a2ffc63e1ef2e5b6a",
  "cid": "QmV15a8534460c8ac82db150fa72dc9dd2ec95a63316",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286496,
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
      "evaluated_at": 1760286496
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
  "sig": "bc02fbbd52c34aad9310644a43abe1ec6a2227fd1ea0aca8d54b9431e73abf4f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000248710981
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285763, 'matching_hash': '9a1c8fb9d78dcf4a'}}}