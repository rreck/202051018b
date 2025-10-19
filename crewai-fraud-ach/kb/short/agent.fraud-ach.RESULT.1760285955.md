```json
{
  "id": "8310aa84848d866a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285955,
  "host_pid": "9e6742732c60:1",
  "hash": "d99788c85dde177295c7d5b09d603b8fd8f618de260fa287796b6ecf0ce34355",
  "cid": "QmV1d99788c85dde177295c7d5b09d603b8fd8f618de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285955,
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
      "evaluated_at": 1760285955
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
  "sig": "e627fb6f22cf3645d5b2a992ac39c272b3a986aa543df2d2ce759a72e9529fe0"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009592096226
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285765, 'matching_hash': '5e92eb8585c87013'}}}