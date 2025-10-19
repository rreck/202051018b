```json
{
  "id": "c22e9046c7ecb662",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289609,
  "host_pid": "9e6742732c60:1",
  "hash": "e969cb0f8d416711fad1e7e20db75f909ce49f623ea243f2bb4f54fc7eaca1f1",
  "cid": "QmV1e969cb0f8d416711fad1e7e20db75f909ce49f62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289609,
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
      "evaluated_at": 1760289609
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
  "sig": "961ccbae93622e2aa9b721fe1606936e263dcd42fd864eb20adefa083d8e8ab1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020376030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 48403712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': '92ff62b724ca331a'}}}