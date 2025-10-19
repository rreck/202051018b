```json
{
  "id": "ea1286b502a116fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288620,
  "host_pid": "9e6742732c60:1",
  "hash": "d2bfb10aa19508ddc24fd748ad82a60d1778449ee86849bfe77b45b5bcecde79",
  "cid": "QmV1d2bfb10aa19508ddc24fd748ad82a60d1778449e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288620,
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
      "evaluated_at": 1760288620
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
  "sig": "93f8ee2f34499babe60613525406ad13ad37e4319d139aee437bf445e9706485"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469776996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 16265700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': '22919e1176d7109e'}}}