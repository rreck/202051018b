```json
{
  "id": "b50f7594a5d551af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292765,
  "host_pid": "9e6742732c60:1",
  "hash": "da4f7b1addbb5cbfb9a1e7b9c481650e200239bb3e9b6f44e8ed029a8130c59e",
  "cid": "QmV1da4f7b1addbb5cbfb9a1e7b9c481650e200239bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292765,
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
      "evaluated_at": 1760292765
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
  "sig": "c8b7322f989dbcb307ec5822c43592e957f1bd4c0c856c73df9d917cc8c2a800"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 64922592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}