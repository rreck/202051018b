```json
{
  "id": "23cc371a81170c13",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290321,
  "host_pid": "9e6742732c60:1",
  "hash": "94cbda4ee221cbae851ac5b10b236a763394385e617606b214c4333e98f02e69",
  "cid": "QmV194cbda4ee221cbae851ac5b10b236a763394385e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290321,
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
      "evaluated_at": 1760290321
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
  "sig": "5ccff214fe0a2f42dc8fdbcc209c208e9a0e21c4f66030ae6ef3b1db6945e046"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025895266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 41733300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': '9ac81502eabc8fa5'}}}