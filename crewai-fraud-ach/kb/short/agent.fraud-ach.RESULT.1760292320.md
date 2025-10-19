```json
{
  "id": "730b7b80bf036be5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292320,
  "host_pid": "9e6742732c60:1",
  "hash": "b6dc1aa2c28ab1d1fe1cca4501675f7c4b8dc193c5bbcef0b02437d3f9de4a2a",
  "cid": "QmV1b6dc1aa2c28ab1d1fe1cca4501675f7c4b8dc193",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292320,
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
      "evaluated_at": 1760292320
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
  "sig": "c81338efefee50c2bf380945ef19e6ef9159556ccfe598c427ac72614d6ee43f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033750281
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 77020710, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285764, 'matching_hash': '57e27cf175445fc0'}}}