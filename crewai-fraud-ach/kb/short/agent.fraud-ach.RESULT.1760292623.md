```json
{
  "id": "a834cc3619eaaff1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292623,
  "host_pid": "9e6742732c60:1",
  "hash": "eec877bad083620efa08e86733c0e7bb4d88d51d037432220adcc039fd0ef1d3",
  "cid": "QmV1eec877bad083620efa08e86733c0e7bb4d88d51d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292623,
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
      "evaluated_at": 1760292623
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
  "sig": "b1d5beb3134592bf910813a369e11374e054064038e8efd93fb118d2beea8f4c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 63967848, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}