```json
{
  "id": "8815599b6f9ae0bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288868,
  "host_pid": "9e6742732c60:1",
  "hash": "a69f9c4f079463f07f215079355fdb27bfa356d65fdf49ff8426bc3a2c4bf6e6",
  "cid": "QmV1a69f9c4f079463f07f215079355fdb27bfa356d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288868,
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
      "evaluated_at": 1760288868
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
  "sig": "35ed4fdcc66799fbca2d918351510b7fe0e01ab4686bd856faded7731909a3b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241265060
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 48373206, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285765, 'matching_hash': '7bee400a4c5e15b1'}}}