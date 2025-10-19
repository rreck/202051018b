```json
{
  "id": "c5266464337e5cd4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291096,
  "host_pid": "9e6742732c60:1",
  "hash": "a660d6e7a770cbfeb1b2caecb8efd65ba3fe76e96ba00f347f8a0fb325c5c3b9",
  "cid": "QmV1a660d6e7a770cbfeb1b2caecb8efd65ba3fe76e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291096,
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
      "evaluated_at": 1760291096
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
  "sig": "adca7591ad4cd3446b530a1d1b161bc6544a20828937e0578878417df7186c70"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466146132
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 66270777, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': '20fb82cc575104fa'}}}