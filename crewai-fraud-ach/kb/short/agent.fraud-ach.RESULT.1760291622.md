```json
{
  "id": "f7239fc1fcc7121a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291622,
  "host_pid": "9e6742732c60:1",
  "hash": "c6e13cfc63c7b12b32e744d6fea75454a0c6664a0b9e8643a2e76f2c80d2ab0d",
  "cid": "QmV1c6e13cfc63c7b12b32e744d6fea75454a0c6664a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291622,
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
      "evaluated_at": 1760291622
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
  "sig": "9a03c713019236d2aaac9389720f4520e6a3fba2f93712fbb1969af88574f7ae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249286838
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 76615222, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': 'a3e7b01587d0e7c3'}}}