```json
{
  "id": "3bbfa16e4b503616",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294901,
  "host_pid": "9e6742732c60:1",
  "hash": "2f2a79324a8db92f3799586e92745a64b1fb5b4f61d8831d722d1ce8d728cca4",
  "cid": "QmV12f2a79324a8db92f3799586e92745a64b1fb5b4f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294901,
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
      "evaluated_at": 1760294901
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
  "sig": "07dbff08c1543ea43432a6cb191b030e30101156f18bd06cf4f8a3aede374a18"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025339678
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 99289044, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': '57e7473926bfe00b'}}}