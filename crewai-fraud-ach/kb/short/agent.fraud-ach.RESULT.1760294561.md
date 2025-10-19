```json
{
  "id": "3af595aaaf735ca4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294561,
  "host_pid": "9e6742732c60:1",
  "hash": "b2ff65073e98899c7d98e99ece82d42365a623e5b813048fd65eac647465ea3e",
  "cid": "QmV1b2ff65073e98899c7d98e99ece82d42365a623e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294561,
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
      "evaluated_at": 1760294561
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
  "sig": "bacceda3e46b2bfebf3f331df042e46d0dd4b12a1184099ec568279b18b83e0b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157447901
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 32452560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': '08b33f5611b85fcf'}}}}