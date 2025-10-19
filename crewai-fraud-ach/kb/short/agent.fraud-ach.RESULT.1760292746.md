```json
{
  "id": "360637955714bf2d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292746,
  "host_pid": "9e6742732c60:1",
  "hash": "30b49fc1432e3b8772ea895d48f488ccd32f110f5a65ba1fc07f29a1f940d169",
  "cid": "QmV130b49fc1432e3b8772ea895d48f488ccd32f110f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292746,
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
      "evaluated_at": 1760292746
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
  "sig": "183529789bfefa6aec08999e9537b39412ad23bd3059ec5bbc07cfa054a93a1a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150540393
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 46041576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '5c99a38661a1ddcd'}}}