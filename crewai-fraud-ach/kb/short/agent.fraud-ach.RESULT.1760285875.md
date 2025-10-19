```json
{
  "id": "4aa8e4a95b25069e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285875,
  "host_pid": "9e6742732c60:1",
  "hash": "6b20e8d771c03bc31df0748a3a533fba80d4f21c325c194fc0634c744fa41f09",
  "cid": "QmV16b20e8d771c03bc31df0748a3a533fba80d4f21c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285875,
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
      "evaluated_at": 1760285875
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
  "sig": "87fdb99170544594350e18a14c0205dd8d362507228cb0bd0abb5c883be31c2f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}