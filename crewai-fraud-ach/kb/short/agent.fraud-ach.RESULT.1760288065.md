```json
{
  "id": "95fc67d63245e2a3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288065,
  "host_pid": "9e6742732c60:1",
  "hash": "e6c4bc7c8cbdd52e245acf3d7ce3b59d4b8477cf9a603f2588c51c5718fa8637",
  "cid": "QmV1e6c4bc7c8cbdd52e245acf3d7ce3b59d4b8477cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288065,
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
      "evaluated_at": 1760288065
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
  "sig": "3635f44214adca791920c8127f4810cd9cad3cdc37a86f780caa6f4ab1166857"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245511773
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 15639075, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285765, 'matching_hash': '976242956abb43a6'}}}