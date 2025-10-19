```json
{
  "id": "5303e0aa8d335bbe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286760,
  "host_pid": "9e6742732c60:1",
  "hash": "31878f88ff77db1f5526f1d7257ba72867349ed9e56c1415f3900044b6154f96",
  "cid": "QmV131878f88ff77db1f5526f1d7257ba72867349ed9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286760,
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
      "evaluated_at": 1760286760
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
  "sig": "3a49313bf7f75d694bbf126c31248d9e1b80c69122f1380d2e2973eedb9a722d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469922578
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285763, 'matching_hash': '96901979868c282a'}}}