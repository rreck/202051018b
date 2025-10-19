```json
{
  "id": "f3092821cd505c67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293125,
  "host_pid": "9e6742732c60:1",
  "hash": "0435062ab756b245de7de4fc137bb004f17991941ebccd36430e36b3a2821b04",
  "cid": "QmV10435062ab756b245de7de4fc137bb004f1799194",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293125,
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
      "evaluated_at": 1760293125
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
  "sig": "a501073833312a00de0a1920f25d4c8509bd88c0d928250008d322326248e97f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021906357
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 92810844, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285764, 'matching_hash': '507361b82f38c481'}}}