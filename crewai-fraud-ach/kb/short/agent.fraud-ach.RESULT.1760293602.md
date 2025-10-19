```json
{
  "id": "6832f833564de3af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293602,
  "host_pid": "9e6742732c60:1",
  "hash": "5f6fba42a7ce2ec64b8f65c696819ce2868e1a59761e1116cc3a516cdca29f94",
  "cid": "QmV15f6fba42a7ce2ec64b8f65c696819ce2868e1a59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293602,
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
      "evaluated_at": 1760293602
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
  "sig": "f55062da6def2bce943fb40204e9b8724e3bfd92285485680262b687dff3857d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150868994
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 92000574, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '612406b6271445a9'}}}