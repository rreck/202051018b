```json
{
  "id": "919d65f0a2f9976a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288016,
  "host_pid": "9e6742732c60:1",
  "hash": "fac9506ccc928bf05494fb1a4c9f2fe3aab6b2de5682f4d35e562bde7da8e16d",
  "cid": "QmV1fac9506ccc928bf05494fb1a4c9f2fe3aab6b2de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288016,
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
      "evaluated_at": 1760288016
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
  "sig": "fb92e6fb9c819349fcb3b6dfc6128a84735f40187ebd76b28cd5d1eb729025f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272419137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 20678560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285763, 'matching_hash': '38281b9a763b4bf2'}}}