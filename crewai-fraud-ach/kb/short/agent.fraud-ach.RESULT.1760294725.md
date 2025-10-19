```json
{
  "id": "c20e8a8d365e826d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294725,
  "host_pid": "9e6742732c60:1",
  "hash": "b57cc28246ba72efadbe6ec7af90f41c1ad104658f198cfbec68c839c000ce81",
  "cid": "QmV1b57cc28246ba72efadbe6ec7af90f41c1ad10465",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294725,
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
      "evaluated_at": 1760294725
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
  "sig": "1e1d975b5317e093225989d2be03b5baf5031750adc4cfa4500f5ce46601e9e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596687644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 24691959, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': 'eb3c042d8ede64d4'}}}