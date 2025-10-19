```json
{
  "id": "0e0ce5e951001ebd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291912,
  "host_pid": "9e6742732c60:1",
  "hash": "a230dfc80afb334bf1b29deece4466a9dd66c8b1f29562efb2bbb219fd9e57a3",
  "cid": "QmV1a230dfc80afb334bf1b29deece4466a9dd66c8b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291912,
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
      "evaluated_at": 1760291912
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
  "sig": "f6e0cc1670606c990311900964867f207f640f6e825f9ee86973adab4cacd1fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464999191
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 23627022, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': '0f07ea7feb264441'}}}