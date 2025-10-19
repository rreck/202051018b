```json
{
  "id": "b0490b74c44723e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294782,
  "host_pid": "9e6742732c60:1",
  "hash": "be600818633a8a5fd778768f088fa628d61de16b91bf0cf3590a04596cd5c2e1",
  "cid": "QmV1be600818633a8a5fd778768f088fa628d61de16b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294782,
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
      "evaluated_at": 1760294782
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
  "sig": "7b15cdbf35821e15d4700802c8e531c6d979e4a2fe813abd649865851e184a21"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038607326
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 38777944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '23e85c6499cf881c'}}}