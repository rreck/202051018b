```json
{
  "id": "2b04afcf0b5d2995",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292058,
  "host_pid": "9e6742732c60:1",
  "hash": "db50e776b703b83cbfef16274c2887e294db7ade382f7784e6754898b753e284",
  "cid": "QmV1db50e776b703b83cbfef16274c2887e294db7ade",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292058,
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
      "evaluated_at": 1760292058
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
  "sig": "a6482bf8821a3ec6e42019061788b939a8251cf385cc1ec77228f8ed2a4311c8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270009801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 91457667, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': '0a6cdd943232be17'}}}