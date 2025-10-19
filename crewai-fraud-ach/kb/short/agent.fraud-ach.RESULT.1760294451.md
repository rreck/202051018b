```json
{
  "id": "4e65f015a932eb92",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294451,
  "host_pid": "9e6742732c60:1",
  "hash": "8641156c239d3be81e437648118e163c6ee668a10e0f6d3cb7b718127685e348",
  "cid": "QmV18641156c239d3be81e437648118e163c6ee668a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294451,
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
      "evaluated_at": 1760294451
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
  "sig": "97c3a773bd093e31a3a72ae54acb5349c81edcfd4a02f4d9fd93b6d4dc52689a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023924602
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 95783814, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285764, 'matching_hash': '8a38ff5636f784bb'}}}