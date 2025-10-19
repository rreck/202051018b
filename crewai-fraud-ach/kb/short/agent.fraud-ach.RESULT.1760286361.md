```json
{
  "id": "f4e43ae5e8053ee4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286361,
  "host_pid": "9e6742732c60:1",
  "hash": "6b645bf73ac63da627a5dcac4174415c80d2979c786caf904072fbc6c55726e5",
  "cid": "QmV16b645bf73ac63da627a5dcac4174415c80d2979c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286361,
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
      "evaluated_at": 1760286361
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
  "sig": "407beddf9ade4bfd6a7a85d0cc6a6a3d436f17ad058e2dc61017ca3eb1bf1860"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000027962561
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '3395f05250aaaeda'}}}